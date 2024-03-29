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

## 예시 코드
```java
package com.gsm.jupjup.domain;

import com.gsm.jupjup.dao.AuthRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;

import java.time.LocalDateTime;
import java.util.List;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;


public class AuthDomainTest {

    @Autowired
    private AuthRepository authRepository;

    //insert Test
    @Test
    public void insert(){
        final AuthDomain authDomain = AuthDomain.builder()
                .email("s19066@gsm.hs.kr")
                .password("123")
                .classNumber("9999")
                .name("김상현")
                .build();

        final String email = authDomain.getEmail();
        final String password = authDomain.getPassword();
        final String classNumber = authDomain.getClassNumber();
        final String name = authDomain.getName();

        assertThat(email, is("s19066@gsm.hs.kr"));
        assertThat(password, is("123"));
        assertThat(classNumber, is("9999"));
        assertThat(name, is("김상현"));
    }

    //Auth LapTop 연관관계 테스트
    @Test
    public void Auth_Laptop(){
        final LaptopDomain laptopDomain = LaptopDomain.builder()
                .laptopName("Mac Pro")
                .laptopbrand("Apple")
                .laptopSerialNumber("1234h12kj34hkl123h4kl123jh4")
                .build();
        final AuthDomain authDomain = AuthDomain.builder()
                .email("s19066@gsm.hs.kr")
                .password("123")
                .classNumber("9999")
                .name("김상현")
                .laptopDomain(laptopDomain)
                .build();

        final String username = authDomain.getName();
        final String laptopName = authDomain.getLaptopDomain().getLaptopName();

        assertThat(username, is("김상현"));
        assertThat(laptopName, is("Mac Pro"));
    }

    //Auth Equipment_Allow 연관관계 테스트
    @Test
    public void Auth_EquipmentAllow(){
        final EquipmentAllowDomain equipmentAllowDomain = EquipmentAllowDomain.builder()
                .name("김상현")
                .amount(9)
                .reason("이유")
                .equipmentEnum(EquipmentEnum.ROLE_Accept)
                .build();
        final AuthDomain authDomain = AuthDomain.builder()
                .email("s19066@gsm.hs.kr")
                .password("123")
                .classNumber("9999")
                .name("김상현")
                .equipmentAllowDomain(equipmentAllowDomain)
                .build();

        final String email = authDomain.getEmail();
        final String why = authDomain.getEquipmentAllowDomain().getReason();

        assertThat(email, is("s19066@gsm.hs.kr"));
        assertThat(why, is("이유"));
    }
}
```

# Repository Test
## 장점
- Repository 관련된 Bean들만 등록하기 때문에 통합 테스트에 비해서 빠릅니다.
- **Repository에 대한 관심사만 갖기 때문에 테스트 범위가 작습니다.**

## 단점
- 테스트 법위가 작기 때문에 실제 환경과 차이가 발생합니다.

## 예시 코드
```java
@RunWith(SpringRunner.class)
@DataJpaTest
@ActiveProfiles(TestProfile.TEST)
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@Ignore
public class RepositoryTest {
}
```
- `@DataJpaTest` 어노테이션을 활용하여 `Repository`에 대한 Bean만 등록합니다
- `@DataJpaTest`는 기본적으로 메모리 데이터베이스에 대한 테스트를 진행합니다.
- `@AutoConfigureTestDatabase` 어노테이션을 활용하여 profile에 등록되 데이터베이스 정보로 대체할 수 있습니다.
- `JpaRepository`에서 기본적으로 제공해주는 `findById`, `findByAll`, `deleteById`등은 테스트를 하지 않습니다.
  - 기본적으로 `save()` null 제약조건등의 테스트는 진행
  - 주로 커스텀하게 작성한 쿼리 메서드, `@Query`으로 작성된 JQPL등의 커스텀하게 추가된 메서드를 테스트합니다.


### Test Code
```java
public class MemberRepositoryTest extends RepositoryTest {

    @Autowired
    private MemberRepository memberRepository;

    private Member saveMember;
    private Email email;

    @Before
    public void setUp() throws Exception {
        final String value = "cheese10yun@gmail.com";
        email = EmailBuilder.build(value);
        final Name name = NameBuilder.build();
        saveMember = memberRepository.save(MemberBuilder.build(email, name));
    }

    ...
    @Test
    public void existsByEmail_존재하는경우_true() {
        final boolean existsByEmail = memberRepository.existsByEmail(email);
        assertThat(existsByEmail).isTrue();
    }

    @Test
    public void existsByEmail_존재하지않은_경우_false() {
        final boolean existsByEmail = memberRepository.existsByEmail(Email.of("ehdgoanfrhkqortntksdls@asd.com"));
        assertThat(existsByEmail).isFalse();
    }
}
```
- **setUp() 메서드를 통해서 Member를 데이터베이스에 insert** 합니다.
  - setUp() 메서드는 메번 테스트 코드가 실행되기전에 실행됩니다. **즉 테스트 코드 실핼 할 때마다 insert -> rollback이 자동으로 이루어집니다.**
- 추가 작성한 쿼리 메서드 existsByEmail을 테스트 진행합니다.
  - **실제로 작성된 쿼리가 어떻게 출력되는지 show-sql 옵션을 통해서 확인 합니다.** ORM은 SQL을 직접 장성하지 않으니 실제 쿼리가 어떻게 출력되는지 확인하는 습관을 반드시 가져야합니다.