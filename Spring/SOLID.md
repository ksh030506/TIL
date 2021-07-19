# 좋은 객체 지향 설계의 5원칙 (SOLID)

## SOLID
> 클린코드로 유명한 로버트 마틴이 좋은 객체 지향 설계의 5가지 원칙을 정리

- SRP : 단일 책임 원칙(Single Responsibility Principle)
- OCP : 개발-폐쇄 원칙(Open/Closed Principle)
- LSP : 리스코프 치환 원칙(Liskov Substitution Principle)
- ISP : 인터페이스 분리 원칙(Interface Segregation Principle)
- DIP : 의존관계 역전 원칙(Dependency Inversion Principle)

## SRP : 단일 책임 원칙(Single Responsibility Principle)
- 한 클래스는 하나의 책임만 가져야 한다
- 하나의 책임은 모호
  - 클 수도 있고 작을 수 있다
  - 문맥과 상황에 따라 다르다
- **중요한 기준은 변경!!**
  - 변경이 있을 때 파급 효과가 적으면 단일 책임 원칙을 잘 따른 것
  - UI 변경, 객체의 생성과 사용을 분리


## OCP : 개발-폐쇄 원칙(Open/Closed Principle)
- 소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다
- 확장을 하려면, 당연히 기존 코드를 변경??
- **다형성 활용**
  - 인터페이스를 구현한 새로운 클래스를 하나 만들어서 새로운 기능을 구현 

## OCP : 개발-폐쇄 원칙(Open/Closed Principle) - 문제점 
- MemberService 클라이언트가 구현 클래스를 직접 선택 
- ```java
    MemberRepository m = new MemoryMemberRepository(); //기존 코드 
    MemberRepository m = new JdbcMemberRepository(); //변경 코드
  ``` 
- **구현 객체를 변경하려면 클라이언트 코드 변경**
- **분명 다형성을 사용했지만 OCP 원칙을 지킬 수 없다**
> 문제 해결 : **객체를 생성하고, 연관관계를 맺어주는 별도의 조립, 설정자가 필요**

## LSP : 리스코프 치환 원칙(Liskov Substitution Principle)
- 프로그램의 객체는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야한다
- **다형성에서 하위 클래스는 인터페이스 규약을 다 지켜야 한다는 것, 다형성을 지원하기 위한 원칙**, 인터페이스를 구현한 구현체는 믿고 사용하려면, 이 원칙이 필요
- 예시 : 자동자 인터페이스의 엑셀은 앞으로 가는 기능, 뒤로 가게 구현한다면 LSP 위반

## ISP : 인터페이스 분리 원칙(Interface Segregation Principle)
- 특정 클라이언트를 위한 인터페이스 여러 개가 범용 인터페이스 하나 보다 낫다
- 자동차 인터페이스 => 운전 인터페이스, 정비 인터페이스로 분리
- 사용자 클라이언트 => 운전자 클라이언트, 정비사 클라이언트로 분리
- 분리하면 정비 인터페이스 자체가 변해도 운전자 클라이언트에 영향을 주지 않음
- **인터페이스가 명확해지고, 대체 가능이 높아짐**

## DIP : 의존관계 역전 원칙(Dependency Inversion Principle)
- 프로그래머는 "추상화에 의존해야지, 구체화에 의존하면 안된다."
- 구현 클래스에 의존하지 말고, 인터페이스에 의존하라는 뜻
- 역할(Role)에 의존하게 해야 한다는 것과 같다. 객체 세상도 클라이언트가 인터페이스에 의존해야 유연하게 구현체를 변경할 수 있다
- 구현체에 의존하게 되면 변경이 아주 어려워진다.

## 정리
- 객체 지향의 핵심은 다형성
- 다형성 만으로는 쉽게 부픔을 갈아 끼우듯이 개발할 수 없다
- 다형성 만으로는 구현 객체를 변경할 때 클라이언트 코드도 함께 변경된다.
- **다형성 만으로는 OCP, DIP를 지킬 수 없다**
- 뭔가 더 필요함