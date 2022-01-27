### 디자인 패턴
- 쉬운 말로 설명하면 **소프트웨어개발 과정에서 발견된 설계의 노하우를 축적하고 이름을 붙어** 이후에 재사용성하기 좋은 형태로 **특정 규약**을 정의한 것입니다.

## 왜 디자인 패턴을 사용하는데?
1. 여러 사람이 협업하는 과정에서 각각의 코딩 스타일을 이해하지 못하고 수정하게 된다면,
2. 의도치 않는 버그를 발생시키기 쉽고, 성능을 최적화 시키기 어렵다. -> 커뮤니케이션 및 예산 증가 초래
3. XXXClass를 만들고 이렇게 엮고 저렇게 엮고 새로운 인터페이스를 만들어 한번에 처리하는 것으로 설계해보자......라는 말보다
4. **팩토리 메소드 패턴** 이라는 것을 사용해 설계해보자 라는 말로 치환하여 불필요한 의사소통을 줄일 수 있습니다.

> 하지만 과유불급이라는 단어를 잘 생각하자. 디자인 패턴 적용이 굳이 필요가 없을 것 같은 부분은 적용하지 않는게 좋다.
> 디자인 패턴은 상황에 따라 정리한 코딩 방법론이며, 해결책이 될 수 없다.
> 막 사용하려 드는 것보다, 이 패턴이 왜 효율적인 방식인지에 집중해야한다.

## 팩토리 메소드 패턴
- 객체 생성 처리를 서브 클래스로 분리하여 처리하도록 캡슐화하는 패턴
    - 객세 생성의 변화에 대비하는데 유용하다
    - 기능 구현은 특정 개별 클래스를 통해 클라이언트에게 제공된다.

### 언제 팩토리 메소드를 사용하는데?
- 생성하려고 하는 객체의 상위개념이 존재하고, 상위 개념 바탕으로 다양한 하위 클래스들이 존재할때
    - Notification => SMS, Slack, Email ...

### 왜 팩토리 메소드를 사용하는데?
- 객체만 생성하는 공장을 통해 간접적으로 생성, 실제 구현 내용은 클라이언트가 모르게 되므로 **객체 간 결합도 낮춤**
- 객체 간 결합도가 낮아진다는 말은 유연하고 확장성 있는 구조와 비슷하므로 추가와 변경의 유지보수가 용의하게 된다는 결과를 낳게된다.
- 다양한 하위 객체들을 한 곳에서 관리할 수 있다.
- 생성자가 아닌 메소드로 작동하기 때문에 **상황에 따라 다른 객체를 반환 할 수 있는 장점**이 있다. -> 객체 선택 유연
- 클래스의 대부분의 내용은 숨기고 싶을때, 상위 개념을 통해서만 객체에 접근하게 할 수 있어 클라이언트에게 실질적인 내용을 숨길 수 있다.

### 장점도 있으면 단점도 있겠지?
- 계속해서 새로운 하위 클래스를 정의한다는 점에서 불필요하게 많은 클래스가 생겨 날 수 있다.

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