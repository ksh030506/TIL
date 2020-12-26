# AOP(1)

# 문제 상황
- 해당 프로젝트는 SpringBoot + JPA + H2 + Gradle로 구현되었습니다.
- 게시글 전체 조회, 단일 조회 기능이 있는 서비스입니다.

**build.gradle**
```java
buildscript {
    ext {
        springBootVersion = '1.4.2.RELEASE'
    }
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}")
    }
}

apply plugin: 'java'
apply plugin: 'eclipse'
apply plugin: 'org.springframework.boot'

jar {
    baseName = 'aop'
    version = '0.0.1-SNAPSHOT'
}
sourceCompatibility = 1.8
targetCompatibility = 1.8

repositories {
    mavenCentral()
}


dependencies {
    compile('org.springframework.boot:spring-boot-starter-aop')
    compile('org.springframework.boot:spring-boot-starter-web')
    compile('org.springframework.boot:spring-boot-starter-data-jpa')

    runtime('org.springframework.boot:spring-boot-devtools')
    runtime('com.h2database:h2')

    testCompile('org.springframework.boot:spring-boot-starter-test')
}
```

**Board.java**
```java
@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Board {

    @Id
    @GeneratedValue
    private Long idx;

    @Column
    private String title;

    @Column
    private String content;
}
```

**BoardService.java**
```java
@Service
public class BoardService {

    @Autowired
    private BoardRepository repository;

    public List<Board> getBoards() {
        return repository.findAll();
    }
}
```

**BoardRepository.java**
```java
@Repository
public interface BoardRepository extends JpaRepository<Board, Long>{}
```

- Board외에 User도 추가해보겠습니다.

**User.java**
```java
@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class User {
    @Id
    @GeneratedValue
    private long idx;

    @Column
    private String email;

    @Column
    private String name;
}
```

**UserService.java**
```java
    @Service
public class UserService extends UserPerformance{

    @Autowired
    private UserRepository repository;

    @Override
    public List<User> getUsers() {
        return repository.findAll();
    }
}
```

**UserRepository.java**
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long>{}
```

**Application.java**
```java
@SpringBootApplication
@RestController
public class Application implements CommandLineRunner{

    @Autowired
    private BoardService boardService;

    @Autowired
    private BoardRepository boardRepository;

    @Autowired
    private UserService userService;

    @Autowired
    private UserRepository userRepository;

    @Override
    public void run(String... args) throws Exception {
        for(int i=1;i<=100;i++){
            boardRepository.save(new Board(i+"번째 게시글의 제목", i+"번째 게시글의 내용"));
            userRepository.save(new User(i+"@email.com", i+"번째 사용자"));
        }
    }

    @GetMapping("/boards")
    public List<Board> getBoards() {
        return boardService.getBoards();
    }

    @GetMapping("/users")
    public List<User> getUsers() {
        return userService.getUsers();
    }

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

