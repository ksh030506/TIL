# DI (Dependency Injection) : 의존성 주입

- Spring의 Container들은 Bean객체들을 관리하는데 있어서 DI를 이용해 Life Cycle을 용이하게 관리할 수 있다.

- 즉, 프레임워크 레벨의 관리를 통해 개발자는 객체들간의 의존성에 신경을 덜 쓰고 Coupling 을 줄일 수 있으며 높은 재사용성과 가독성있는 코드를 만들어낼 수 있다.


이를 제어의 역전(Inversion Of Control) 이라 하며, 이것이 스프링 프레임워크의 특징적인 개념인 IOC 이다.

(클래스 관리의 주체가 개발자가 아닌 프레임워크라는 뜻이다.)


- Dependency Injection 을 통해 얻을 수 있는 장점 -



 (1) Dependency Reduction : 객체 상호 간 의존성 관계를 줄여준다.



 (2) Reusable Structure : 코드의 재사용과 조합이 용이하다.



 (3) Readability : 코드들이 분리되다보니 가독성이 뛰어나진다.



 (4) Loose Coupling & Easy to change : 구조는 변화에 민감하지 않을 수 있다.



그 외에 테스트가 용이하고 다양한 패턴을 적용하는 데 유연하다는 점도 큰 장점이 될 수 있다.
