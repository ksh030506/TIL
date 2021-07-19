## 팩토리 메소드 패턴

- 객체의 생성은 일반적으로 new를 사용해 구체적인 클래스 이름을 지정한다. 팩토리 메소드 패턴은 사람이 직접무엇인가를 만드는 것이 아니라 공장(Factory)에서 지정된 방식으로 대신 클래스를 생성해주는 방식이다.
- 클래스에서 객체를 생성한다

## 팩토리 매소드를 사용해야되는 경우
- 생성하려고 하는 객체의 상위개념 클래스나 인터페이스가 존재하고, 이런 상위개념 클래스나 인터페이스를 바탕으로 다양한 하위 클래스들이 존재할때

## 팩토리 메소드 장점
- 관리용이성 - 클래스 이름대신 팩토리 메소드를 사용해 객체를 생성하기 때문에, 추후 실제 생성되는 객체가 바뀌거나 추가되어도 문제가 없다.
- 보안성 - 클래스의 대부분의 내용은 숨기고 싶을때, 인터페이스나 abstract를 통해서만 객체에 접근하게 할수 있다.
- 리소스재활용성 - 팩토리 메소드가 반드시 객체를 새로 생성할 필요는 없고, 상황에 따라 새로 생성될수도, 기존의 것을 리턴할수도 있다

## Java Factory Method Pattern 구조

<img src="https://www.programcreek.com/wp-content/uploads/2013/02/factory-design-pattern.png">

## Java Factory Method Pattern 예제 소스 코드

- Shape.java
    ```java
    public interface Shape{
        void draw();
    }
    ```

- Circle.java
    ```java
        public class Circle implements Shape {
            @Override
            public void draw(){
                System.out.println("Circle - draw() Method");
            }
        }
    ```

- Circle.java
    ```java
        public class Circle implements Shape {
            @Override
            public void draw(){
                System.out.println("Circle - draw() Method");
            }
        }
    ```
- Rectangle.java
    ```java
        public class Rectangle implements Shape {
            @Override
            public void draw(){
                System.out.println("Rectangle - draw() Method");
            }
        }
    ```

- Square.java
    ```java
        public class Square implements Shape {
            @Override
            public void draw() {
                System.out.println("Square - draw() Method");
            }
        }
    ```

- ShapeFactory.java
    ```java
        public class ShapeFactory {
            //팩토리 매소드 - 객체 생성 후 반환
            public Shape getShape(String shapeType){
                if(shapeType == null){
                    return null;
                }
                if(shapeType.equalsIgnoreCase("CIRCLE")){
                    return new Circle();
                }
                else if(shapeType.equalsIgnoreCase("RECTANGLE")){
                    return new Rectangle();
                }
                else if(shapeType.equalsIgnoreCase("SQUARE")){
                    return new Square();
                }
                return null;
            }
        }
    ```

- FactoryPatternTest.java
    ```java
        public class FactoryPatternTest {
            public static void main(String[] args){
                //팩토리 클래스에서 객체를 생성후 반환
                ShapeFactory shapeFactory = new ShapeFactory();

                Shape shape1 = shapeFactory.getShape("CIRCLE");
                shape1.draw();

                Shape shape2 = shapeFactory.getShape("RECTANGLE");
                shape2.draw();

                Shape shape3 = shapeFactory.getShape("SQUARE");
                shape3.draw();
            }
        }
    ```

## 정리
- 객체 생성을 담당 및 처리하는 팩토리 클래스가 존재
- 팩토리 클래스만 관리하면 되므로 객체 생성에 관한 확장도 쉽게 구성할 수 있다
- 의존성 원칙 및 추상 팩토리, 정적 팩토리 ....