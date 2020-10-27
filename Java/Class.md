# **Java Class**

## **객체 지향 프로그래밍**
- **객체란?**
  - 물리적으로 존재하거나 추상적으로 생각할 수 있는 것 중에서 자신의 속성을 가지고 있고 다른 것과 식별 가능한 것
        ex) 학과, 강의, 주문
  - 객체는 속성(필드)과 동작(메서드)으로 구성
  <br/>
    <img src="https://lh3.googleusercontent.com/proxy/2rOAUKpwMn8Po8cxKhHf5zTA1rFashSgMXGRYTG5QsOO2qe0qauAxrXlg3smmrTJImuS9o50gGAm3ZdmpgOJBrzNvbH29btvM3lI2zVI5y5_R7wlq1GyzMV26cHGgXITzpo3ngsqsUApGq3t-Ky5tReixY6qPb__aaExAIwYvT56pDSlBPgwxR-Nyb1CSuU0laVo2GI">

    <br/>
    - 리턴 값 저장 예시
    <br/>

    ```java
    int result = Calculator(10, 20)
    ```
    

## **객체 지향 프로그래밍의 특징**
  1. 캡슐화 :
        객체의 필드, 메소드를 하나로 묶고, 실제 구현 내용을 감추는 것을 말한다. => 접근 제한자 사용
  2. 상속 :
        상위 객체 : 자신이 가지고 있는 필드와 메소드를 하위 객체에게 물려줌
        하위 객체 : 상위 객체가 물려준 필드와 메소드를 사용
  3. 다형성 :
        같은 타입이지만 실행 결과가 다양한 객체를 이용할 수 있는 성질을 말한다.

        ```java
        interface OverWatch { // 인터페이스
	        void name(); // 추상 메소드
	        void lClick(); // 추상 메소드
	        void rClick(); // 추상 메소드
	        void shiftButton(); // 추상 메소드
	        void eButton(); // 추상 메소드
	        void qButton(); // 추상 메소드
        }
        ```

        <br/>

        ```java
        class Mei implements OverWatch { // 인터페이스 구현 클래스
	       public void name() { // 오버라이딩
	    	    System.out.println("이름 : 메이");
	       }
	       public void lClick() { // 오버라이딩
	    	    System.out.println("좌클릭 : 냉각총");
	        }
	        public void rClick() { // 오버라이딩
		        System.out.println("우클릭 : 고드름 투사체");
	        }
	        public void shiftButton() { // 오버라이딩
		        System.out.println("shift : 급속 빙결");
	        }
	        public void eButton() { // 오버라이딩
		        System.out.println("e : 빙벽");
	        }
	        public void qButton() { // 오버라이딩
		        System.out.println("q : 눈보라(궁극기)");
	        }
        }
        ```

        <br/>

        ```java
        class Reaper implements OverWatch { // 인터페이스 구현 클래스
	        public void name() { // 오버라이딩
	        	System.out.println("이름 : 리퍼");
        	}
        	public void lClick() { // 오버라이딩
	        	System.out.println("좌클릭 : 헬파이어 샷건");
	        }
        	public void rClick() { // 오버라이딩
	        	System.out.println("우클릭 : 없음");
	        }
        	public void shiftButton() { // 오버라이딩
        		System.out.println("shift : 망령화");
        	}
        	public void eButton() { // 오버라이딩
	        	System.out.println("e : 그림자 밟기");
	        }
	        public void qButton() { // 오버라이딩
	        	System.out.println("q : 죽음의 꽃(궁극기)");
	        }
        }
        ```

        <br/>

        ```java
        class Mccree implements OverWatch { // 인터페이스 구현 클래스
	        public void name() { // 오버라이딩
		        System.out.println("이름 : 맥크리");
        	}
	        public void lClick() { // 오버라이딩
	        	System.out.println("좌클릭 : 피스키퍼");
        	}
        	public void rClick() { // 오버라이딩
	        	System.out.println("우클릭 : 모든 총알 발사");
	        }
	        public void shiftButton() { // 오버라이딩
	        	System.out.println("shift : 구르기");
	        }
	        public void eButton() { // 오버라이딩
	        	System.out.println("e : 섬광탄");
	        }
	        public void qButton() { // 오버라이딩
	        	System.out.println("q : 황야의 무법자(궁극기)");
	        }
        }
        ```

        <br/>

        ```java
        public class PolymorphismEx01 {
	        public static void main(String[] args) { // main 메소드
	        	OverWatch ow; // 인터페이스 객체 선언

	        	System.out.println("플레이할 캐릭터 번호 선택(1. 메이, 2. 리퍼, 3. 맥크리)");
	        	Scanner sc = new Scanner(System.in); // 스캐너 객체
	        	int n = sc.nextInt();

	        	if(n==1){
	        		ow = new Mei(); // 업캐스팅
	        	} 
                else if(n==2){
	        		ow = new Reaper(); // 업캐스팅
	        	}
                else{
	       		    ow = new Mccree(); // 업캐스팅
	        	}
                // 선택한 조건에 따라서 부모 객체로 자식 메소드 사용(하나의 타입으로 다양한 결과를 얻어냄 / 다형성)
	        	ow.name();
	        	ow.lClick();
	        	ow.rClick();
	        	ow.shiftButton();
	        	ow.eButton();
	        	ow.qButton();
	        }
        }
        ```

## **생성자**
- **기본 생성자**
  - 생성자 :
        필드 초기화
  - 기본 생성자 : 
        모든 클래스는 생성자가 반드시 존재한다<br/>
        기본 생성자는 바이트 코드에 자동 추가시킨다<br/>
        new 연산자 뒤에 기본 생성자를 호출해서 객체를 생성한다
  - 생성자 선언 :
        명시적으로 선언 가능하다
  - 생성자 오버로딩
        생성자의 다양성

    
    ```java
    public class Car {

        private String name;
        private String color;
        private int cc;

        Car(String name, String color, int cc){
            this.name = name;
            this.color = color;
            this.cc = cc;
        }

        Car(String color, int cc){
            this.color = color;
            this.cc = cc;
        }
    }
    ```

    <br/>

    ```java
    public class CarExample {
        public static void main(String[] args){
            Car myCar = new Car("김상현", "검정", 1000);
            Car myCar = new Car("검정", 1000);
            Car myCar = new Car();  //에러 - 기본 생성자를 호출할 수 없음
        }
    }
    ```

- **메소드 오버로딩**
  - 클래스 내에 같은 이름의 메소드를 여러 개 선언하는 것
  - 