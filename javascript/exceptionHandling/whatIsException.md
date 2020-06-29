# 예외의 개념

예외는 정해진 규칙에서 벗어남을 뜻한다.  
  
자바스크립트에서도 문법이라는 정해진 규칙에 있다. 그래서 이 규칙을 지키면서 자바스크립트에서 코드를 작성해야 한다. 그리고 실질적으로 코드가 실행될 때 문법은 맞아도 정의되지 않은 코드를 참조 한다거나 정의되지 않은 함수를 참조할 때 이런 예외가 발생한다.  
  
```js
const sum = (x, y) => {
    return x + y
}
console.log(sum(1,2))
```
sum() 함수는 인자들을 더해 값을 출력한다. 하지만 인자에 문자열이 들어가게 된다면 문법상의 오류는 없지만 우리가 원하는 숫자의 합을 구할 수가 없다. 그래서 이때 발생할 수 있는 에러를 코드로 미리 잡아준다. 
```js
const sum = (x, y) => {
    if(typeof x !== 'number' || typeof y !== 'number'){
        throw '숫자가 아닙니다'
    }
    return x + y
}
console.log(sum('1',2))
```
이때 예외는 자바스크립트 내부에서 만든 것이 아니라 우리가 코드로 작성한 것이다. 우리가 정해 놓은 규칙에 어긋났으니 예외를 발생시킨 것이다.  

# try/catch, Error 객체 사용  
  
```js
const f2 = () => {
    console.log('f2 start');
    console.log('f2 end');
}

const f1 = () => {
    console.log('f1 start');
    f2();
    console.log('f1 end')
}

console.log('will : f1');
f1();
console.log('did : f1');

==============================
will : f1
f1 start
f2 start
f2 end
f1 end
did : f1
```
위 코드에서 f2() 함수에 예외를 한 번 발생시켜보자.  
```js
const f2 = () => {
    console.log('f2 start');
    throw 'error';
    console.log('f2 end');
}

const f1 = () => {
    console.log('f1 start');
    f2();
    console.log('f1 end')
}

console.log('will : f1');
f1();
console.log('did : f1');

==============================
will : f1
f1 start
f2 start
error
```
위 코드처럼 throw 밑으로는 코드가 출력되지 않는 것을 볼 수 있다. f2()에서 에러가 발생하고 처리를 하지 않으면 콜스택에 쌓여있던 f2() 실행 정보가 파괴되고 그 다음 f1() 함수에 throw가 넘겨진다. f1()에서도 에러 처리가 없으면 콜스택에 f1()의 실행 정보가 파괴되고 마지막으로 f1()을 호출한 main으로 넘어가게 된다. 위 코드에서는 어디에도 에러 처리를 하지 않았기 때문에 콜스택에 쌓여있던 실행 정보들이 모두 파괴되어 에러가 발생하기 전까지의 코드들만 실행되어 진다.  
그러면 여기서 예외 처리를 해보자.  
```js
const f2 = () => {
    console.log('f2 start');
    throw 'error';
    console.log('f2 end');
}

const f1 = () => {
    console.log('f1 start');
    try{
        f2();
    } catch(e) {
        console.log(e);
    }
    console.log('f1 end')
}

console.log('will : f1');
f1();
console.log('did : f1');

==============================
will : f1
f1 start
f2 start
error   
f1 end  
did : f1
```
console.log('f2 start') 다음 예외가 발생하였기 때문에 그 뒷부분인 console.log('f2 end') 부분은 실행되지 않는 것을 볼 수 있다. 그리고 catch 구문으로 에러를 콘솔에 출력하는 행위를 하는 것으로 에러 처리를 했기 때문에 나머지 코드들은 잘 동작한다.  
그럼 다른 곳에서 에러 처리를 해보자.  
```js
const f2 = () => {
    console.log('f2 start');
    throw 'error';
    console.log('f2 end');
}

const f1 = () => {
    console.log('f1 start');
    f2();
    console.log('f1 end')
}

console.log('will : f1');
try{
    f1();
} catch(e) {
    console.log(e);
}
console.log('did : f1');

=============================
will : f1
f1 start
f2 start
error   
did : f1
```
f2() 함수에서 예외가 발생해서 f1() 함수 안에 있는 f2()로 넘어왔는데 거기서도 처리를 하지 않았기 때문에 그 다음 코드인 console.log('f1 end')가 실행되지 않는다.  
  
throw를 사용할 때는 보통 new Error() 객체를 사용한다. 그 안에 어떠한 메시지를 전달한다. 
```js
throw new Error('error');
```
new Error 객체에는 해당하는 콜스택 정보가 담겨져 있다. 위 코드 같은 경우에는 
```
Error : error
     at f2 (파일 위치 : 코드줄넘버)
     at f1 (파일 위치 : 코드줄넘버)
     at 파일 위치 : 코드줄넘버
```
와 같은 콜스택 정보가 담겨져 나온다. 콜스택이기때문에 역순으로 읽으면 호출한 순서를 좀 더 쉽게 이해할 수 있다. 