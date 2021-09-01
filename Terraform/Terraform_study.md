# Terraform Study

**Terraform : 인프라스트럭처 도구 (프로비저닝 도구)**
- 코드소서의 인프라스트럭처를 지향하고 있는 도구
- GUI나 웹 콘솔을 통해 서비스 실행에 필요한 리소스를 관리하는 대신 필요한 일소스들을 선언적인 코드로 작성해 관리할 수 있도록 해줍니다.

### 테라폼 설치
- `Mac`에서는 `Homebrew`를 사용해 간단히 설치 가능합니다.
  ```
    $ brew install terraform
  ```

- 버전 확인
  ```
    $ terraform version
  ```

### 테라폼 버전 관리
- 특정 버전의 테라폼을 사용하고 싶거나, 여러 버전을 사용할 필요가 있을 때는 `tfenv`를 사용하면 편리합니다.
- `tfenv`는 테라폼 버전 매니저로 `Mac`, `Linux`, `Windows`를 지원하고 있습니다.
  <br>
  ```
    $ brew install tfenv
    $ tfenv install 0.12.23
    $ tfenv use 0.12.23
    $ terraform version
  ```

### 테라폼을 사용한 웹 애플리케이션 인프라스트럭처 프로비저닝
