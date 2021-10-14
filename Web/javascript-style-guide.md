
### 참조
**1. 모든 참조는 const 이용**  

**2. 참조를 재할당 해야한다면 let 이용**  

**3. let과 const는 블록스코프 이므로 블록안에서만 사용**  


### 오브젝트
**4. 오브젝트를 작성할때는 리터럴 구문 이용**
```javascript
const item = {};
```  

**5. 예약어 대신 동의어 이용**  

**6. 메소드 단축 구문 이용**
```javascript
const atom = {
  value: 1,

  addValue(value) {
    return atom.value + value;
  },
};
```  

**8. 프로퍼티 단축구문 사용**
```javascript
const lukeSkywalker = 'Luke Skywalker';

const obj = {
    lukeSkywalker
};
```  

**9. 프로퍼티 단축구문은 오브젝트 선언의 시작부분에서 그룹화**  

### 배열
**10. 배열은 피터럴 구문을 이용**  

**11. 직접 배열에 배입하지 않고 push 사용**  

**12. 배열을 복사할때는 확장 연잔자 ... 사용**
```javascript
const itemsCopy = [...items];
```

**13. array-like 오브젝트를 배열로 변환하는 경우는 Array.form 사용**
```javascript
const foo = document.querySelectorAll('.foo');
const nodes = Array.from(foo);
```

### 구조화대입
**14. 하나의 오브젝트에서 복수의 프로퍼티를 사용 할 때는 오브젝트 구조화대입 사용**
```javascript
const obj = {
    "firstName" : "a",
    "lastName" : "a"
};

function getFullName({ firstName, lastName }) {
  return `${firstName} ${lastName}`;
}
```

**15. 배열의 구조화 대입 사용**
```javascript
const arr = [1, 2, 3, 4];
const [first, second] = arr;
```

**16. 복수의 값을 반환하는 경우는 오브젝트의 구조화대입 사용**
```javascript
function processInput(input) {
    return {left, right, top, bottom};
}

// 호출처에서는 필요한 데이터만 선택하면 됩니다.
const { left, right } = processInput(input);
```

### 문자열
**17. 문자열에는 '' 사용**
**18. 프로그램에서 문자열을 사용하는 경우는 template strings 사용, eval() 사용 X**
```javascript
function sayHi(name) {
  return `How are you, ${name}?`;
}
```

### 함수
**19. 함수선언 사용**
```javascript
function foo() {
}
```

**20. 조건문 안에 함수를 사용할 수는 없지만 함수식을 이용해 변수에 함수를 대입**
```javascript
let test;
if (currentUser) {
  test = () => {
    console.log('Yup.');
  };
}
```

**21. 파라미터에 arguments 지정 X, args 사용**

