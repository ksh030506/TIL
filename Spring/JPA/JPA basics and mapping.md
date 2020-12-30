# 객체 매핑 하기
- `Entitly` : JPA가 관리할 객체를 엔티티라고 한다
- `@Id` : DB PK와 매핑할 필드

```java
@Entity
public class Member {
    @Id
    private Long id;
    private String name;
}
```
```sql
create table Member (
    id bigint not null,
    name varchar(255),
    primary key (id)
);
```

# 데이터베이스 방언
```properties
spring.jpa.database-platform=org.hibername.dialect.MySQL5InnoDBDialect
```
- JPA는 특정 데이터베이스에 종속적이지 않은 기술
- 각각의 데이터베이스가 제공하는 SQL문법과 함수는 조금씩 다르다
  - 가변 문자 : MySQL은 `varchar`, Oracle은 `varchar2`
  -문자열을 자르는 함수 : SQL 표준은 `substring()`, Oracle은 `substr()`
  - 페이징 : MySQL은 `Limit`, Oracle은 `Rownum`
 > 방언 : SQL 표준을 지키지 않거나 특정 데이터베이스만의 고유한 기능

<img src="/img/img2.png">

# 사용해보기
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persistence
    xmlns="http://xmlns.jcp.org/xml/ns/persistence"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/persistence http://xmlns.jcp.org/xml/ns/persistence/persistence.xsd">
 
    <persistence-unit name="persistence-unit"
        transaction-type="RESOURCE_LOCAL">
        <provider>org.hibernate.ejb.HibernatePersistence</provider>
        <properties>
            <property name="hibernate.diarect" value="${hibernate.dialect}" />
            <property name="hibernate.hbm2ddl.auto" value="${hibernate.hbm2ddl.auto}" />
            <property name="javax.persistence.jdbc.driver" value="${db.driver}" />
            <property name="javax.persistence.jdbc.url" value="${db.url}" />
            <property name="javax.persistence.jdbc.user" value="${db.user}" />
            <property name="javax.persistence.jdbc.password" value="${db.password}" />
        </properties>
    </persistence-unit>
</persistence>
```

```java
public class Main {
    public static void main(String[] args){
        EntityManagerRactory emf = 
                Persisgence.createEntityManagerFactory("hello");

        EntityManager em = emf.createEntityManager();
        EntityTransaction = tx = em.getTransaction();
        tx.begin();

        try {
            Member member = new Member();
            member.setId(100L);
            member.setName("김상현");

            em.persist(member);
            tx.commit();
        } catch(Exception e){
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }
}
```
# 주의
> 엔티티 매니저 팩토리는 하나만 생성해서 애플리케이션 전천에서 공유
> 엔티티 매니저는 쓰레드간에 공유하면 안된다(사용 => 버림)
> JPA의 모든 데이터 변경은 트랜잭션 안에서 실행
