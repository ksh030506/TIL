# TDD (테스트 전략)

### 소개
> 스프링은 다양한 테스트 전략을 제공한다. 대표적으로 **Slice Test**라는 것으로 특정 래아어에 대해서 Bean을 최소한으로 등록시켜 테스트 하고자 하는 부분에 최대한 단위 테스트를 지원합니다

> 다양하게 지원해주는 만큼 테스트 코드를 통일성 있게 관리하는 것이 중요

## 테스트 전략
|어노테이션|설명|부모 클래스|Bean|
|-------|----|----------|----|
|`@SpringBootTest`|통합 테스트, 전체|IntegrationTest|Bean 전체|
|`@WebMvcTest`|단위 테스트, Mvc 테스트|MockApiTest|MVC 관련된 Bean|
|`@DataJpaTest`|단위 테스트, Jpa 테스트|RepositoryTest|JPA 관련 Bean|
|`None`|단위 테스트, Service 테스트|MockTest|JPA 관련 Bean|
|`None`|POJO, 도메인 테스트|None|None|

# POJO Test
## 설명
> **각 엔티티 객체들이 기능을 제대로 하는지 확인해야합니다.** 예를 들어 Name 필드가 **Getter/Setter** 메서드를 제공해 주지 않으면 **Getter/Setter** 메서드를 만족시키는 메서드들이 다른 계층에서 구현하게 되고 중복 코드가 발생하게 됩니다.

## 장점
- POJO 객체이므로 테스트하기 편합니다. **외부에서 주입 받을 의존성도 없고 Mocking할 대상**도 없습니다.
- **엔티티 객체는 사용하는 계층이 많으므로 테스트의 효율성**이 높습니다.

