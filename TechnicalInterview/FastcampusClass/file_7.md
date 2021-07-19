# 웹 프로그래머 면접 예상질문_2

## 1) 자바의 특징에 대해 말해보시오.
- 1) OOP(객체 지향 언어) : 부품에 해당하는 객체들을 먼저 만들고, 이것들을 하나씩 조립해 전체 프로그램을 완성하는 개발 기법
- 2) "가비지 컬렉션"에 의한 메모리 자동 관리
- 3) "멀티 쓰레드"를 지원한다.
- 4) JVM 위에서 동작하기 때문에 특정 OS에 종속적이지 않고 이식성이 좋으며, 보안성이 좋다.
- 5) 다양한 Open 라이브러리들이 존재한다.

## 3) 변수란?
- "하나의 값을 저장할 수 있는 메모리 공간"

## 4) 객체와 클래스의 차이점에 대해 설명해 보시오.
- 클래스(Class) : 현실 세계의 객체의 속성과 동작을 추려내 필드와 메서드로 정의한 것으로 "아직 메모리가 할당되지 않은 상태"
- 객체(Object) : 이 Class라는 설계도를 기반으로 실제 메모리가 잡힌 것을 의미하며 이런 객체를 조합해 전체 프로그램을 완성해 나가는 방식을 OOP(객체지향 프로그래밍)이라고 한다.

## 5) 객체 지향 PG이란? 또 그 특징은?
- 현실세계의 객체를 필드와 메서드로 정의한 Class를 기반으로 실제 메모리가 잡혀 만들어진 부품과 같은 객체들을 조합해 전체 프로그램을 완성해 나가는 개발 기법으로

    ### 특징)
      - 캡슐화, 은닉화 : 외부 객체에서 구현방식은 알 수 없도록 숨기고 별도로 접근할 수 있는 getter/setter 메서드를 통해 접근하도록 하는 방식
      - 상속 : 부모 Class를 자식이 접근할 수 있도록 물려 받는 방식
      - 다형성 : 부모 클래스 타입으로 해당 부모를 상속받는 여러 자식 class를 대입할 수 있는 성질 등을 들 수 있다.

## 6) 다형성이란?
- 서로 다른 클래스로부터 만들어진 객체지만 같은 부모의 Class 타입으로 이들을 관리할 수 있는(=대입될 수 있는) 성질

## 7) 자바의 메모리 영역(간단하게 설명)
  1. 메서드 영역 : static 변수, 전역변수, 코드에서 사용되는 Class 정보 등이 올라간다. 또한 코드에서 사용되는 class들을 로더로 읽어 클래스별로 런타임 필드데이터, 메서드 데이터 등을 분류해 저장한다.
  2. 스택(Stack) : 지역변수, 함수(메서드) 등이 할당되는 LIFO(Last In First Out) 방식의 메모리
  3. 힙(Heap) : new 연산자를 통한 동작할당된 객체들이 저장되며, 가비지 컬렉션에 의해 메모리가 관리되어 진다.

## 8) 추상메서드? 추상 클래스?
- 추상메서드 : 메서드의 정의부만 있고 구현부는 있지 않은 메서드
- 추상 클래스 : 추상메서드를 적어도 하나 이상 가지고 있는 클래스로 자식클래스에서 오버라이딩(재정의)가 필요한 추상메서드를 가지고 있기 때문에 객체화 할 수 없다.

## 9) 인터페이스(Interface)란? 또 왜 사용하나?
- 인터페이스는 모든 메서드가 구현부가 없는 추상메서드로 이루어진 클래스로, abstract 키워드를 붙이지 않아도 자동으로 모든 메서드는 추상메서드로 정의가 된다. 또한 변수도 자동으로 final static 키워드가 붙게 된다.

    ### 왜 인터페이스를 사용하는가? 
      - 팀작업시 개발코드 부분과 객체가 서로 통신하는 접점 역할을 지원하게 되는데, 이는 개발코드에선 객체의 내부 구조를 모르더라도 인터페이스의
      - 메서드 명만 알고 있으면 되기 때문이다. 이를 통해 얻을 수 있는 장점은 해당 메서드를 통해 나오는 결과물을 알고 있기 때문에 다른 팀의
      - 작업을 기다리고 있지 않아도 되며, 또한 해당 객체가 수정될 경우 개발 코드 부분은 수정을 하지 않아도 된다. 또한, 부가적으로 객체를 파일에 쓰기 위해 Serializable 인터페이스를 구현하거나, Collections.sort()를 하기 위해서 Comparable 인터페이스를 상속하는 것, Cloneable 을 구현하는 것처럼 특정 작업을 하겠다라는 "Mark"역할을 해주기도 한다.

## 10) 프로세스(Process) 와 쓰레드(Thread)의 차이점에 대해 아는가?
- 프로세스 : OS가 메모리 등의 자원을 할당해준 실행중인 프로그램을 가리킨다. 이때, 각각의 프로세스는 서로 메모리 공간을 독자적으로 갖기 때문에 서로 메모리 공간을 공유하지 못한다. 따라서 공유하기 위해서는 IPC(InterProcess Communication)과 같은 방식이 필요하다.
- 쓰레드 : 쓰레드는 프로세스 내에서 프로세스의 자원을 가지고 실제로 일하는 "일꾼"과 같으며 각 쓰레드는 독자적인 Stack 메모리를 갖고 그 외의 자원(메모리)는 프로세스 내에서 공유하게 된다.

## 11) 컬렉션프레임워크(CollectionFramework)에 대해 아는만큼 말해 보시오.
- Collection 인터페이스 
  - List 인터페이스 : 배열과 유사하되, 추가할때마다 자동으로 Boundary를 늘려주는 구조로, 중복된 데이터를 허용하며, 순서가 존재한다.
    ex) - ArrayList : 배열로 구현됬으며, 인접해 있기 때문에 데이터 조회에 매우 빠르다 하지만, 빈번한 삽입, 삭제시 새로 배열을 만들고 데이터를 옮겨야 하기 때문에 LinkedList에 비하여 속도가 느리다.
  - LinkedList : 링크 구조로 되어 있기 때문에 조회는 ArrayList에 비해 느리지만, 삽입 삭제시 링크를 끊고 새로 추가되는 데이터에 링크만 연결하면 되기 때문에 삽입, 삭제에 유리하다.
  - Vector : 구현 방식은 ArrayList와 유사하지만 Vector를 개선한 것이 ArrayList이다. 또한 Vector의 경우에는 ArrayList와 달리 Synchronized(동기화)가 걸려 있어 여러 쓰레드에서 동시에 접근할 수 없다.

- Set 인터페이스 : 집합처럼 중복된 데이터를 허용하지 않으며, 순서가 없다. 또한, 객체 내부의 중복된 데이터를 배제하고 싶은 경우 Object 클래스의 equals 메서드와 hashCode 메서드의 재정의가 반드시 필요하다.
    ex) - HashSet
      - TreeSet : 순서가 있는 HashSet으로 이진 트리 구조로 만들어 졌다. 순서에 맞게 정렬되어 저장되기 위해서 Comparable을 구현해야한다.

- Map 인터페이스 : key와 value 쌍으로 데이터를 저장하며, key는 중복될 수 없고, value는 중복 저장이 가능하다.
    ex) - HashMap

        - TreeMap

        - Properties : key value 쌍으로 저장되지만 value의 타입이 String만 가능하다.

        - Hashtable : HashMap과 구조는 같으며, 단지 Synchronized(동기화) 되어져 있다는 점이 다른점이다.