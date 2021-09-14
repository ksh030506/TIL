# Valut

## Valut 란 무엇일까?

- **Secrets에 안전하게 접근할 수 있도록 하는 도구 (Tool)**
  - API key, PW, Certificates 등 내가 관리하고자 하는 모든 것을 포함한다.
  
- Vault는 어떠한 Secrets에 대해서도 단일화된 인터페이스를 제공하고, 이 과정에서 엄격한 접근 제어 및 상세한 audit logging을 제공한다.

```md
- 시스템들은 여러 종류의 Secrets(DB credential, 외부 서비스를 위한 API Key, 등...)을 필요로 한다.

- 누가 어떤 Secrets에 접근할 수 있는지 이해하는 것은 이미 매우 어려운 일이며, 특정 플랫폼에 종속되기도 쉽다.

- 나아가 Key Rolling을 추가하거나 저장소를 보호하고, 상세한 Audit logging을 제공하는 것은 Custom Solution을 배제했을 때 사실상 불가능한 일에 가깝다. Vault는 이러한 수요를 해결하기 위해 도입될 수 있다.
```

## Valut의 주요 기능

### Secure Secret Storage - 안전한 Secret 저장소

- 임의의 Key/Value Secrets를 Vault에 저장할 수 있다.
- Vault는 이러한 Secrets를 저장소에 쓰기 전에 우선적으로 암호화하고, RAW 스토리지가 Data에 얻어내더라도 Secrets 내용에 접근할 수 없도록 한다.
- Vault는 물리적인 Disk이외에도 Consul이나, 다른 클라우드 스토리지와 통합되어 쓰기 작업을 수행할 수 있다.

### Dynamic Secrets - 동적 Secrets

- Vault는 AWS나 SQL DB와 같은 경우, 온디맨드 방식에 따른 Secret 생성이 가능하다.
- App이 S3 버킷에 접근할 필요가 있을 경우 :
    1. App 은 Vault에게 접근을 위한 Credential을 요구한다.
    2. Vault는 요구에 맞는 유효한 권한을 포함한 AWS Keypair를 생성한다.
    3. App은 Vault가 동적으로 생성한 AWS Keypair를 통해 일정 시간 동안 S3 버킷에 접근한다.
- 동적 Secret을 생성한 후, Vault는 lease 기간을 측정하여 자동으로 자신이 생성한 동적 Secrets를 폐기(revoke)한다.

### Data Encryption - Data 암호화

- Vault는 Data를 저장하지 않더라도 암호화하거나 복호화할 수 있다.
- 보안 담당자가 암호화 파라미터를 정의하고, 개발 담당자가 자신만의 암호화 방식을 설계할 필요 없이 암호화된 Data를 SQL과 같은 장소에 저장할 수 있도록 한다.

### Leasing and Renewal - 임대 및 갱신

- Vault의 모든 Secrets은 그들과 관련된 `lease`를 갖는다.
- lease 기간이 끝나면, Vault는 자동으로 Secret을 폐기(revoke)한다.
- Client들은 필요에 따라 Built-in renew APIs(Vault에 내장된 갱신 API들)를 통해 lease 기간을 갱신할 수 있다.

### Revocation - 폐기

- Vault는 Secret 폐기에 대해 내장된 기능을 제공한다.
- Vault는 단일 Secrets 뿐만 아니라, Secrets Tree를 폐기할 수도 있다.
  - 예를 들어, 특정 User에게만 읽기 권한이 있는 모든 Secrets나, 특정 유형의 모든 Secrets등을 포함할 수 있다.
- 폐기 기능은 Key Rolling은 물론, 침입 상황 발생시 System Lock-down에도 큰 도움이 될 수 있다.

```md
참고: key rotation (또는 key rolling) 이란?
- 보호하려고 하는 데이터가 모두 하나의 key로 암호화 되어있는 경우 해당 key가 유출되면 모든 데이터가 유출되게 된다. 
- 이러한 위험성을 줄이기 위해서 위해서 주기적으로 key를 변경하는 것을 key rotation 이라고 한다. 
- 이 경우 특정 key가 유출되더라도, 특정 기간동안에 생성된 데이터만 유출되고, 다른 key로 암호화된 데이터는 안전하다.
```


## Vault 아키텍처

<img src="../img/vault_architecture.png">

## Vault의 전체적인 흐름

- Vault를 사용하기 위해서는 `unsealing`과 `초기화 작업`이 필요하다.
- Vault 서버 초기화 시 Vault는 `sealed` 상태이다.
- `Unsealed-Key`는 `sealed` 상태를 `unsealed` 상태로 전이할 수 있다.
- `unsealed` 상태가 되면 Barrier안에 있는 Vault의 모든 기능 및 구성요소에 원활하게 접근할 수 있다.
- Vault에서 실질적으로 Secret을 암/복호화하는 키는 `Encryption-Key`이다.
    ```
    1) "Master-Key"는 “Encryption-Key”를 암호화한다.

    2) "Unsealed-Key"는 “Master-Key”를 암호화한다.

    3) “Unsealed-key”는 SSS(Shamir Secret Sharing) 알고리즘으로분할 보관한다.
    ```

- 키들의 관계는 다음과 같다.
    <img src="../img/Vault%20Crypto-Key%20mechanism.png">
    - `Encryption-Key`는 `Secret`을 안전하게 암/복호화한다. 
    - `Secret`들은 `Storage backend`에 보관하며, `Secret`에 접근하기 위해서는 `REST API`를 사용한다. 
    - REST API는 `Create, Register, Rotate, Destroy` 등의 명령을 제공하며, `Secret`을 제어할 수 있다. 
    - REST API를 사용하기 위해서는 `토큰 인증`과 `토큰에 상응하는 정책 인가` 작업이 필요하다.

## 고가용성

- **Vault는 HA를 구성할 수 있다.**
  - HA의 구조는 Active-Standby 구조이다. 
- 오픈 소스 버전의 경우 Standby는 Read-Only 기능을 제공하지 않는다.
- Standby에 요청이 들어오면 요청을 Active에 포워딩한다.
- 제일 큰 단점은 Standby의 read-only의 미지원이다. Product 레벨에서 Vault를 사용하기 위해서는 해당 기능이 제일 필요할 것 같다.
- **Replication 방식은 PostgreSQL의 방식과 같이 Active-Standby 구성이며,** Active의 변경/추가/삭제된 것에 대한 로그(WAL, Write Ahead Log)를 Standby에 전송한다.
- 데이터 처리에 있어 보통의 DBMS과 같이 WAL 기법을 사용한다.

## 보안 특성

- Vault와 클라이언트 상호 인증은 제공하지 않는다. 다만 서버에서 제공하는 네트워크 계층 보안, TLS를 제공한다.
- 정상 토큰을 보유한 주체는 리소스("Secret")에 접근할 수 있다.
- 토큰 인가 정책은 리소스에 접근하는 주체를 제어한다.
- Secret에 접근하는 모든 행위를 감사 로깅한다.
- "Secret"을 암호화하여 Storage Backend에 저장한다.
- Vault의 Barrier를 통과하는 모든 요청과 반환은 AES-256(GCM)으로 암호화한다. IV의 경우, 자동으로 임의로 생성한다.
- SSS(Shamir Secret Sharing) 알고리즘으로 MasterKey를 분리 보관한다.

## Key 회전(갱신)

- rekey 명령은 Unsealed-Key와 Master-Key를 갱신한다.
- 갱신된 Master-Key는 Encryption-Key를 재암호화하며, 갱신된 Unsealed-Key는 SSS에 의해 다시 분리하여 보관하여야 한다.
- rotate 명령은 Encryption-Key를 갱신한다.
- 기존 Encryption-Key는 별도의 keyring에 보관한다. 후의 요청들은 새로운 Encryption-Key로 암호화를 한다.
- Keyring에 있는 Encryption-Key는 복호화 용도에만 사용한다. 이와 같이 사용하면 re-encryption을 수행하지 않아도 괜찮다.

## Vault 용어 정리

### Barrier

- Barrier는 Vault를 감싸듯이 설계된 `암호화 장벽`이다.
- Vault와 스토리지 백엔드 사이에 흐르는 모든 data는 barrier를 통한다.
- Barrier는 암호화된 data만 밖으로 기록될 수 있도록 보장하며, 그 과정에서 data가 확인되고 복호화될 수 있도록 돕는다.
- Vault 내부에 접근하고자 할 때, Barrier는 Unsealed 상태가 되어야 한다.
  - Sealed : Vault가 Barrier에 의해 보호되는 상태
  - Unsealed : Vault의 Barrier가 해제되어 내부 data에 접근이 가능한 상태

### Storage Backend

- **암호화된 data를 저장할 책임이 있는 저장소**이다.
- 스토리지는 Vault에 의해 신뢰되지 않는다.
  - Vault는 스토리지 백엔드에 의해 스토리지의 지속성(durability)만 제공한다.
- 스토리지 백엔드는 Vault Server가 시작될 때 설정되어야만 한다.

### Secrets

- Vault에 의해 반환 요소 중 **암호화되어야할 요소를 일컫는 용어**이다.
  - Vault로부터 반환되는 요소 중에는 시스템 설정이나 상태 정보, 정책 등도 있기 때문에, Vault의 모든 정보를 Secret이라고 표현하지는 않는다.
- Secrets는 언제나 Lease와 연관된다.
  - Client는 Secret이 무한히 지속될 것이라고 생각해서는 안된다.

### Secrets Engine

- **Secrets 관리에 책임을 갖는 주체이다.**
- kv와 같은 간단한 시크릿 엔진은 쿼리 발생시 적절한 Secret을 리턴
- 몇몇 시크릿 엔진은 쿼리된 시점마다 동적인 Secret을 생성하기 위한 정책 할당 기능을 지원
  - 예를 들면, **MySQL 시크릿 엔진에 대해 web 정책을 할당했다고 가정**
    1. 웹 서버가 web secret에 대해 읽기 작업(Read)을 수행할 때마다  
       1. 일정 시간 동안만 사용이 가능하고, 제한된 권한을 갖는 MySQL User / PW 페어가 반환된다.  
       2. 웹 서버는 반환된 ID / PW 페어를 통해 MySQL에 접근한다.

### Auth Method

- **Vault에 연결된 사용자나 App을 인증(Authentication)하기 위해 사용된다.**
- 한 번 인증된 후에, auth method는 적용되어야 할 정책들 중 사용 가능한 목록을 반환한다.
- Vault는 인증된 사용자를 확인한 후, 이후의 요청에서 사용될 Client Token을 반환한다.  
  1. UserPass Auth method는 사용자 인증에 username / PW를 사용한다.
  2. github auth method는 사용자에 대해 GitHub을 통한 인증을 허용한다.

### Audit Device

- **모든 Vault의 Request/Respones는 Audit Device에 의해 감사 로깅이 된다.**
  
### Client Token

- **HTTP에서의 세션 ID와 같은 토큰을 반환한다.**
- Vault의 REST API를 사용하는 경우 `HTTP 헤더에 토큰`을 적재한다.

## Valut & Consul Docker 다운로드

[다운로드 링크](https://github.com/ksh030506/docker_consul_vault)

