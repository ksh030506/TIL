# JPA 객체 지향 쿼리

## JPA는 다양한 쿼리 방법을 지원
- JPQL
- JPA Criteria
- QueryDSL
- 네이티브 SQL
- JDBC API 직접 사용, Mybatis, StringJdbcTemplate 함께 사용


## JPQL
- SQL과 문법 유사 select, from, where, group by, having, join 지원
- JPQL은 엔티티 객체를 대상으로 쿼리
- SQL은 데이터베이스 테이블을 대상으로 쿼리
- 테이블이 아닌 객체를 대상으로 검색하는 객체 지향 쿼리 
- SQL을 추상화해서 특정 데이터베이스 SQL에 의존 X
- JPQL을 한마다로 정의하면 객체 지향 SQL

```java
String jpql = "select m From Member m where m.name like '%hello%'";
List<Member> result = em.createQuery(jqpl, Member.class).getResultList();
```
<img src="/img/img27.png">

## JPQL 문법
- select m from Member m where m.age > 18
- 엔티티와 속성은 대소문자 구분
- JPQL 키워드는 대수문자 구분 안함
- 엔티티 이름을 사용, 테이블 이름이 아님
- 별칭은 필수

## 결과 조회 API
- query.getResultList() : 결과가 하나 이상, 리스트 반환
- query.getSingleResult() : 결과가 정확히 하나, 단일 객체 반환

## 파라미터 바인딩 - 이름 기준, 위치 기준
```java
String jpql = "select m From Member m where m.username=:username";
query.setParameter("username", usernameParam);

String jpql2 = "select m From Member m where m.username=?1";
query.setParameter(1, usernameParam);
```

## 프로젝션
```java
String jpql = "select m From Member m"; //엔티티 프로젝션
String spql2 = "select m.team From Member m"; //엔티티 프로젝션
String spql3 = "select username, age From Member m"; //단순 값 프로젝션
String spql4 = "select new jpabook.jpql.UserDTO(m.username, m.age) From Member m"; //new : 단순 값을 DTO로 바로 조회
//Distinct는 중복 제거 
```

## 페이징
- JPA는 페이징을 두 API로 추상화
- setFirstResult(int startPosition) : 조회 시작 위치
- setMaxResults(int maxResult) : 조회할 데이터 수

<img src="/img/img28.png">
<img src="/img/img29.png">
<img src="/img/img30.png">

## 집합과 정렬
- count(m)
- sum(m.age)
- avg(m.age)
- max(m.age)
- min(m.age)
- group by, having, order by

## 조인
- 내부 조인 : select m From Member m [inner] Join m.team t
- 외부 조인 : select m From Member m left [outer] Join m.team t
- 세타 조인 : select count(m) from Member m, Team t where m.username = t.name
- **참고 : 하이버네이트 5.1부터 세타 조인도 외부 조인 가능**

## 패치 조인
- 엔티티 객체 그래프를 한번에 조회하는 방법
- 별칭을 사용할 수 없다
- JPQL : select m from Member m join **fetch** m.team
- SQL : select M.*, T.& from Member M Inner join Team T on M.Team_id = T.Id

```java
String spql = "select m from Member m join fetch m.team";

List<Member> members = em.createQuery(spql, Member.class).getResultList();

for(Member member : members){
    //패치 조인으로 회원과 팀을 함께 조회해서 지연 로딩 발생 안함
    System.out.println("username = " + member.getUsernaem() + ", " + 
                        "teamname = " + member.getTeam().name());
}
```

**... 기본적인 SQL 함수 및 서브 쿼리 지원**