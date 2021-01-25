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


