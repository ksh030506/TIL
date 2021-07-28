# 양방향 매핑

- mappedBy : JPA의 맨붕.... => 객체와 테이블간에 연관관계를 맺는 차이를 이해해야 한다

## 객체와 테이블이 관계를 맺는 차이

- 객체 연관관계
  - 회원 => 팀 연관관계 1개 (단방향)
  - 팀 => 회원 연관관계 1개 (단뱡향)
- 테이블 연관관계
  - 회원 <=> 팀의 연관관계 1개 (양방향)

## 객체의 양방향 관계

- 객체의 **양방향 관계는 사실 양방향 관계가 아니라 서로 다른 단방향 관계 2개이다**
- 객체를 양방향으로 참조하려면 단방향 연관관계를 2개 만들어야한다.
<img src="/img/img7.png">

## 테이블의 양방향 관계

- 테이블은 외래 키 하나로 두 테이블의 연관관계를 관리
- Member.Team_ID 외래 키 하나로 양방향 연관관계를 가짐 (양쪽으로 조인할 수 있다.)
<img src="/img/img8.png">

<img src="/img/img9.png">

# 연관관계 주인(Owner)

## 양방향 매핑 규칙

- 객체의 두 관계중 하나를 연관관계 주인으로 지정
- **연관관계의 주인만이 외래 키를 관리(등록, 수정)**
- **주인이 아닌쪽은 읽기만 가능**
- 주인은 mappedBy 속성 사용 X
- 주인이 아니면 mappedBy 속성으로 주인 지정

## 누구글 주인으로????

- 외래 키가 있는 곳을 주인으로 정해라
- 여기서는 Member.team이 연관관계의 주인
<img src="/img/img10.png">

## 양방향 매핑시 가장 많이 하는 실수 (연관관계 주인에 값을 입력하지 않음)

```java
Team team = new Team();
team.setName("TeamA");
em.persist(team);

Member member = new Member();
member.setName("member1");
//역방향(주인이 아닌 방향)만 연관관계 설정
team.getMembers().add(member);

em.persist(member);
```

<img src="/img/img11.png">

## 양방향 매핑시 연관관계 주인에 값을 입력해야한다 (순수한 객체 관계를 고려한다면 항상 양쪽다 값을 입력해야한다)

```java
Team team = new Team();
team.setName("TeamA");
em.persist(team);

Member member = new Member();
member.setName("member1");
team.getMembers().add(member);
//연관관계의 주인에 값 설정
member.setTeam(team);

em.persist(member);
```

<img src="/img/img12.png">

## 양방향 매핑의 장점

- **단방향 매핑만으로도 이미 연관관계 매핑은 완료**
- 양방향 매핑은 반대 방향으로 조회(객체 그래프 탐색) 기능이 추가된 것 뿐
- JPQL에서 역방향으로 탐색할 일이 많음
- 단방향 매핑을 잘하고 양방향은 필요할 때 추가해도 아무 상관없음 (테이블에 영향을 주지 않음)

### 연관관계 매핑 어노테이션

- 다대일(@ManyToOne)
- 일대다(@OneToMany)
- 일대일(@OneToOne)
- 다대다(@ManyToMany)
- @JoinColumn, @JoinTable

### 상속 관계 매핑 어노테이션

- @Inheritance
- @DiscriminatorColumn
- @DiscriminatorValue
- @MappedSuperclass(매핑 속성만 상속)

### 복합키 어노테이션

- @IdClass
- @EmbeddedId
- @Embeddable
- @MapsId