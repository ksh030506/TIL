# 데이터베이스 스카마(테이블) 자동 생성하기
- DDL을 애플리케이션 실행 시점에 자동 생성
- 테이블 중심 => 객체 생성
- 데이터베이스 방언을 활용해서 데이터베이스에 맞는 적절한 DDL 생성
- 이렇게 생성된 DDL은 개발 장비에서만 사용
- 생성된 DDL은 운영서버에서는 사용하지 않거나, 적절히 다듬은 후 사용


```xml
hibernate.hbm2ddl.auto
```
- `create` : 기존테이블 삭제 후 다시 생성 (Drop + Create)
- `create-drop` : create와 같으나 종료시점에 테이블 Drop
- `update` : 변경된 부분만 반영 (운영DB에서는 사용하면 안됨)
- `validate` : 엔티티와 테이블이 정상 매핑되었는지 확인
- `none` : 사용하지 않음

> **운영 장비에는 절대 create, create-drop, update를 사용하면 안된다**

- 개발 초기 : create AND update
- 테스트 : update AND validate
- 스테이징 운영과 운영 서버 : validate AND none

 # 매핑 어노테이션
```java
@Getter
@Setter
@Entity
public class Member {
    @Id
    private Long id;

    @Colum(name = "USERNAME")
    private String name;

    private int age;

    @Temporal(TemporalType.TIMESTAMP)
    private Date regDate;

    @Enumerated(EnumType.STRING)
    private MemberType memberType;
}
```



 - `@Column`
   - name : **필드와 매핑할 테이블의 컬럼 이름**
   - insertable, updatable : 읽기 전용
   - nullable : null 허용여부 결정, DDL 생성시 사용
   - unique : 유니크 제약 조건, DDL 생성시 사용
   - columnDefinition, length, precision, scale (DDL)
 - `@Temporal`
   - @Temporal(TemporalType.DATE) : 날짜
   - @Temporal(TemporalType.TIME) : 시간
   - @Temporal(TemporalType.DATE) : 날짜와 시간
 - `@Enumerated`
   - 열거형 매핑
   - EnumType.ORDINAL : 순서를 저장(기본값)
   - EnumType.STRING : **열거형 이름을 그대로 저장, 가급적 이 것을 사용**
 - `@Lob`
   - CLOB : String, char[], java.sql.CLOB
   - BLOB : byte[], java.sql.BLOB
   - ```java
        @Lob
        private String lobString; //CLOB

        @Lob
        private byte[] lobyte; //BLOB
     ```
 - `@Transient` : 이 필드는 매핑하지 않는다, 애플리케이션에서 DB에 저장하지 않는 필드

# 식별자 매핑 어노테이션

```java
@Id
@GeneratedVaue(strategy = GenerateionType.AUTO)
private Long id;
```

- `@Id`
- `@GeneratedValue`
  - `IDENTITY` : 데이터베이스에 위힘, MySQL
  - `SEQUENCE` : 데이터베이스 시퀀스 오브젝트 사용, Oracl
    - `@SequenceGenerator` 필요
  - `TABLE` : 키 생성용 테이블 사용, 모든 DB에서 사용
    - `@TableGenerator` 필요
  - `AUTO` : 방언에 따라 자동 지정, 기본값

# 권장하는 식별자 전력
- 기본키 제약 조건 : Null 아님, 유일, **변하면 안된다**
- 미래까지 이 조건을 만족하지 자연키는 찾기 어렵다. 대리키(대체키)를 사용하자
- 예를 들어 주민등록번호도 기본 키로 적절하지 않다.
- **권장 : Long + 대체키 + 키 생성전략 사용**