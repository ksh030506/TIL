# 매핑 정보가 포함된 회원 클래스

```java 

package jpabook.start;

import javax.persistence.*;

@Entity
@Table(name="MEMBER")
public class Member {
    @Id
    @Column(name="ID")
    private String id;

    @Column(name="NAME")
    private String username;

    //매핑 정보가 없는 필드
    private Integer age;
}
```

- `@Entity`
  - 이 클래스를 테이블과 매핑한다고 JPA에게 알려준다. 이렇게 `@Entity`가 선언된 클래스를 엔티티 클래스라 한다.
- `@Table`
  - 엔티티 클래스에 매핑할 테이블의 정보를 알려준다. `name`속성을 이용하여 `Member`엔티티를 `MEMBER`테이블에 매핑하였다. 생략하면 클래스 이름을 테이블 이름으로 매핑한다.
- `@Id`
  - 엔티티 클래스의 필드를 테이블의 기본 키에 매핑한다. 여기서는 테이블의 ID 기본 키에 매핑하였다. 이렇게 `@id`가 사용된 필드를 식별자 필드라고 한다.
- `@column`
  - 필드를 칼럼에 매핑한다. 여기서는 `name`속성을 이용하여 `Member` 엔티티의 `username`필드를 `MEMBER`테이블의 `NAME`컬럼에 매핑하였다.
- 매핑 정보가 없는 필드
  - `age`필드에는 매핑 어노테이션이 없다. 이렇게 어노테이션을 생갹하면 필드명을 사용하여 컬럼명으로 매핑된다. 데이터베이스가 대소문자를 구분하지 않는다고 가정하였지만, 만약 대소문자를 구별한다면 `@column`를 사용하여 매핑시켜야한다.

