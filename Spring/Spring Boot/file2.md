# 스프링부트 만들기_1

## 롬복(Lombok)
- 자바 프로젝트 필수 라이브러
- 클래스에서 필수적으로 작성해야하는 접근자/설정자, ToString, equalsAndHashCode, 생성자 등을 자동 생성
- 코드 간결
- 배포버전을 확인하고 결합이 있는지 확인


## 애플리케이션 계층(layerd Spring Application)
- 계층(Layer) : @Component
- 표현(Persentation) : @Controller
- 서비스(Service) : @Service
- 영속화(Persistence) : @Repository

<img src="/img/img37.png">


## 업무(=비즈니스 로직) 구현에만 집중해라!!!
- 영속화 계층(@repository)에서는 엔티티 관리만
- 비즈니스 로직 구현은 도메인 영역에서
- 서로 다른 도메인 사이에 연계는 서비스 계층(@Service)에서
- 외부요청에 대한 처리는 컨트롤러 계층(@Controller)에서


## @Service
- 트랜잭션(@Transactional) 관리영역
- 서로 다른 도메인 연계(DI, @Autowired)작업 영역
- @Controller와 @Repository 사이의 중계


<img src="/img/img38.png">

## Rest API
- 시스템의 자원(Resource)에 대한 접근 및 제어를 제공하는 API

## Spring REST DOCs
- Spring MVC test와 Asciidoctor 조합을 통해서 RESTful 서비스에 대한 문서화 지원
- 작성된 테스트코드에 대한 아스키독 조각 생성
- 개발자가 아스키독 조각을 모아 아스키독 문서를 작성
- 코드에 침투적이지 않은 노력에 따라 고품질의 코드가 될 수 있음

## 프로젝트 모듈 구성
- common : 프로젝트에서 공통으로 사용하는 유틸리티, 예외
- core : 프로젝트 도메인(@Entity, @Repository)
- api : 외부에 정보를 제공하는 Rest API 모듈
- admin : 서비스를 관리하기 위한 백오피스
- batch : 정기적으로 실행할 배치 프로그램 모음
- message : 알림톡, SMS, 메일 발송 등 담당

## 프로젝트 구성시 필수조건
- README를 작성해라
- 실행 절차를 설명해라
- 실행절차에 따라 빌드하고 실행되도록 하라
- 커밋 및 푸쉬는 테스트 및 빌드가 성공되었을때 하라
- 코딩 (Convention, 관례)은 팀원들과 함께 만들자


