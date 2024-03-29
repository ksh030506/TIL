# AWS Route 53

## PerView
- 확장성이 뛰어난 Domain Name System (DNS) 서비스
- "www.example.com" 와 같은 사람이 읽을 수 있는 이름을 **192.0.2.1** 이와 같은 IP 주소로 변환하여 서로 통신할 수 있도록 변환합니다.

### HTTPS?
- 기존의 HTTP는 전송하는 데이터를 암호화하지 않고 평문으로 통신을 하기 때문에 도청, 변조 등의 보안에 매우 취약한 프로토콜입니다.
- HTTPS는 SSL 증명서를 통해 서버 또는 클라이언트의 신원을 확인하고, 데이터를 암호화, 인증, 안정성을 제공해주기 때문에 기존의 HTTP 프로토콜보다 안전합니다.

## AWS Route 53 왜 써야하는데?
- 높은 가용성과 안전성
  - 트래픽 흐름 및 라우팅 제어 통해 장애 조치가 가능하다.
- 유연성
  - 엔드포인트 상태, 지리적 위치, 지연 시간등을 기반으로 트래픽을 라우팅한다.
- 간편성, 신속성
  - AWS Management Console를 통해 간단한 API를 활용하여 작업 가능하다.
- 확장성
  - 대규모 쿼리 볼륨을 처리할 수 있도록 자동 확장한다.


## 요금?
- https://aws.amazon.com/ko/route53/pricing/ 참고

## "www.example.com" 를 검색하면 어떻게 될까? (AWS DNS 동작 원리)
<img src="./route53.png">

1. 사용자가 웹 브라우저를 열어 www.example.com을 검색합니다.

2. 케이블 인터넷 공급업체, DSL 광대역 공급업체 또는 기업 네트워크 같은 인터넷 서비스 제공업체(ISP)가 관리하는 DNS 해석기로 라우팅됩니다.

3. ISP의 DNS 해석기는 www.example.com에 대한 요청을 DNS 루트 이름 서버에 전달합니다. (해당 도메인의 확장자(.com,. net, .org, etc.)에 따라 재귀 확인자를 TLD 네임서버에 보내 응답합니다.)

4. com 도메인의 TLD 이름 서버 중 하나에 다시 전달합니다. com 도메인의 이름 서버는 example.com 도메인과 연관된 4개의 Amazon Route 53 네임 서버의 이름을 사용하여 요청에 응답합니다. (예를 들어 TLD 네임서버는 ‘.com’으로 끝나는 모든 웹사이트의 정보를 갖고 있습니다.)

5. ISP의 DNS 해석기는 Amazon Route 53 네임 서버 하나를 선택해 www.example.com에 대한 요청을 해당 이름 서버에 전달합니다.

6. Amazon Route 53 네임 서버는 example.com 호스팅 영역에서 www.example.com 레코드를 찾아 웹 서버의 IP 주소 192.0.2.44 등 연관된 값을 받고 이 IP 주소를 DNS 해석기로 반환합니다.

7. ISP의 DNS 해석기가 마침내 사용자에게 필요한 IP 주소를 확보하게 됩니다. 해석기는 이 값을 웹 브라우저로 반환합니다. 또한, DNS 해석기는 다음에 누군가가 example.com을 탐색할 때 좀 더 빠르게 응답할 수 있도록 사용자가 지정하는 일정 기간 example.com의 IP 주소를 캐싱(저장)합니다.

8. 웹 브라우저는 DNS 해석기로부터 얻은 IP 주소로 www.example.com에 대한 요청을 전송합니다. 여기가 콘텐츠가 있는 곳으로, 예를 들어 웹 사이트 엔드포인트로 구성된 Amazon S3 버킷 또는 Amazon EC2 인스턴스에서 실행되는 웹 서버입니다.

9. 192.0.2.44에 있는 웹 서버 또는 그 밖의 리소스는 www.example.com의 웹 페이지를 웹 브라우저로 반환하고, 웹 브라우저는 이 페이지를 표시합니다.

## AWS Elastic Beanstalk에서 HTTPS를 적용하는 방법
- 사전 준비 : 도메인 구하기
> ✔ Amazon 서비스에서 발급해주는 SSL 인증서는 무료인 대신에, 해당 도메인의 DNS 서버로 Route 53을 사용해야하며 Route 53을 사용하기 위해서는 도메인이 필요합니다.
1. Route 53에 구매한 도메인 등록하기
   - **호스팅 영역으로 들어가서 구매한 도메인을 등록합니다. -> 퍼블릭, 프라이빗 결정**
2. 등록을 완료하고 **편집**을 눌러 AWS Route 53에서 제공되는 **네임서버(NS) 레코드**를 도메인을 구매한 홈페이지로 들어가서 네임서버 정보를 입력해주어야합니다.
   - 도메인 이름과 IP의 상호변환을 가능하게 해주는 서버
3. AWS Certificate Manager를 이용하여 무료로 SSL 인증서를 발급받는다.
   - 해당 도메인에 대해 인증서를 발급한다.
   - 이 서비스에서는 공인인증서, 사설인증서 등을 모두 생성할 수 있고 이곳에서 생성된 공인인증서를 통해서 HTTPS를 적용할 수 있습니다.
4. AWS Elastic Beanstalk에 ACM 인증서 등록
    - **구성** 버튼을 눌러 이동 -> 로드밸런서 탭으로 이동
    - **리스너 추가** 버튼 눌러서 추가 -> 443, HTTPS, SSL 인증서
<<<<<<< HEAD
## 트레바리 Route 53 분석 (Route 53은 프리티어가 아닙니다ㅠㅠ)
=======

## 트레바리 Route 53 분석
>>>>>>> 2511fb38c7075b327902906b2075a4bdc1d8987e
**trevari.co.kr -> 퍼블릭**
**trevari.net -> 프라이빗**

- trevari.co.kr 
  - NS : 네임 서버
  - 서비스 : admin, b2b2, backend, dev, partners, user, www.trevari.co.kr
- trevari.net
  - NS : 네임 서버
  - 서비스 : api 같은 사용자가 알면 안되는 서비스


## 용어
  - 호스팅 == 도메인
  - NS : 네임 서버 역할 
  - SOA : 도메인 영역을 표시하는 역할 (네임서버에게 어떤 기준에 의해 이 도메인을 관리하여야 하는지 알려주는 역할)
  - A : Address (domain name에 하나의 IP Address가 있음을 의미합니다)
  - CNAME : 하나의 도메인에 다른 이름을 부여하는 방식
  - 