# Spring Data JPA와 QueryDSL

### 반복되는 CRUD
```java
public class MemberRepository {
    public void save(Member member){...}
    public Member findOne(Long id){...}
    public List<Member> findAll(){...}
    public Member findByUsername(String username){...}
}

public class ItemRepository {
    public void save(Item item){...}
    public Member findOne(Long id){...}
    public List<Member> findAll(){...}
}
```

## 스프링 데이터 JPA 소개
- 지루하게 반복되는 CRUD 문제를 세련된 방법으로 해결
- 개발자는 인터페이스만 작성
- 스프링 데이터 JPA가 구현 객체를 동적으로 생성해서 주입

```java
public class MemberRepository extends JpaRepository<Member, Long>{
    public Member findByUsername(String username){...}
}

public class ItemRepository extends JpaRepository<Item, Long>{
    //비어있음
}
```

### 스프링 데이터 JPA 적용 후 클래스 다이어그램
<img src="/img/img31.png">

### 스프링 데이터 JPA가 구현 클래스 생성
<img src="/img/img32.png">

### 공통 인터페이스 기능
- JpaRepository 인터페이스 : 공통 CRUD 제공
- 제네릭은 <엔티티, 식별자>로 설정

## 메서드 이름으로 쿼리 생성
- 메서드 이름만으로 JPQL 쿼리 생성
```java
public class MemberRepository extends JpaRepository<Member, Long>{
    public Member findByUsername(String username);
}
```

- 메서드 이름으로 쿼리 생성 => 사용 코드
```java
List<Member> member = MemberRepository.findByName("hello");
```
> 실행된 SQL
> select * from Member m where m.name = 'hello' 

## 이름으로 검색 + 정렬
```java
public class MemberRepository extends JpaRepository<Member, Long>{
    public Member findByUsername(String username, Sort sort);
}
```
> 실행된 SQL
> select * from Member m where m.name = 'hello' order by age desc

## 이름으로 검색 + 정렬 + 페이징
```java
public class MemberRepository extends JpaRepository<Member, Long>{
    public Member findByUsername(String username, Pageable pageable);
}
```

<img src="/img/img33.png">

### @Query, JPQL 정의
- @Query를 사용해서 직접 JPQL 지정

```java
public class MemberRepository extends JpaRepository<Member, Long>{
    @Query("select m from Member m where m.username = ?1")
    public Member findByUsername(String username, Sort sort);
}
```

### 반환 타입
```java
List<Member> findByName(String name); //컬레션
Member findByEmail(String email); //단건
```

## Web 페이징과 정렬 기능
- 컨트롤러에서 페이징 처리 객체를 바로 받을 수 있음
- page : 현재 페이지
- size : 한 페이지에 노출할 데이터 건수
- sort : 정렬 조검
```
/members?page=0&size=20&sort=name,desc
```
```java
@RequestMapping(value="/members", memthod = RequestMethod.GET)
String list(Pageable pageable, Model model){...}
```

### Web 도메인 클래스 컨버터 기능
- 컨트롤러에서 식별자로 도메인 클래스 찾음
- /members/100
```java
@RequestMapping(value="/members{memberId}")
Member member(@PathVariable("memberId") Member member){
    return member;
}
```

# QueryDSL 소개
- SQL, JPQL을 코드로 작성할 수 있도록 도와주는 빌더 API
- JPA 크리테리아에 비래서 편리하고 실용적임
- 오픈 소스


## SQL, JPQL의 문제점
- SQL, JPQL은 문자, Type-check 불가능
- 해당 로직 실행 전까지 작동여부 확인 불가
<img src="/img/img34.png">

## QueryDSL 장점
- 문자가 아닌 코드로 작성
- **컴파일 시점에 문법 오류 발견**
- 코드 자동완성 (IDE 도움)
- 단순하고 쉬움 : 코드 모양이 JPQL과 거의 비슷
- 동적 쿼리

## QueryDSL 동적원리 쿼리타입 생성
<img src="/img/img35.png">

## QueryDSL
```java
//JPQL
//select m from Member m where m.age > 18

JPAFactoryQuery query = new JPAFactoryQuery(em);
QMember m = QMember.member;

List<Member> list = query.selectFrom(m).where(m.age.gt(18))
.orderBy(m.name.desc())
.fetch();
```

## QueryDSL - 조인
```java
JPAFactoryQuery query = new JPAFactoryQuery(em);
QMember m = QMember.member;
QTeam t = QTeam.team;

List<Member> list = query.selectFrom(m)
.join(m.team, t)
.where(t.name.eq("teamA"))
.fetch();
```

## QueryDSL - 조인
```java
JPAFactoryQuery query = new JPAFactoryQuery(em);
QMember m = QMember.member;

List<Member> list = query.selectFrom(m)
.orderBy(m.age.desc())
.offset(10)
.limit(20)
.fetch();
```

## QueryDSL - 동적 쿼리
```java
String name = "member";
int age = 9;

JPAFactoryQuery query = new JPAFactoryQuery(em);
QMember m = QMember.member;

BooleanBuilder builder = new BooleanBuilder();
if(name != null){
    builder.and(m.name.contains(name));
}
if(age != 0){
    builder.and(m.age.gt(age));
}

List<Member> list = query.selectFrom(m)
.where(builder)
.fetch();
```

## 예시 코드
```java
return query.selectFrom(coupon)
.where(
    coupon.type.eq(typeParam),
    coupon.status.eq("LIVE"),
    marketing.viewConut.lt(markting.maxCount)
).fetch();
```

- 제약 조건 조립 가능
- 가독성 재사용

```java
return query.selectFrom(coupon)
.where(
    coupon.type.eq(typeParam),
    isServiceable();
).fetch();

private BooleanExpression isServiceable(){
    return coupon.status.eq("LIVE")
        .and(marketing.viewConut.lt(markting.maxCount));
}
```