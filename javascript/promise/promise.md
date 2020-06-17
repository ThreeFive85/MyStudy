자바스크립트의 promise는 콜백지옥을 해결하기 위해 사용되어진다.  
  
콜백지옥의 예 :  
만약 비동기적인 setTimeout을 순차적으로 진행해보고 싶을때  
```js
const delay = (sec, callback) => {
    setTimeout(() => {
        callback(new Date().toISOString());
    }, sec * 1000);
}

delay(1, (result) => {
    console.log(1, result);
    delay(1, (result) => {
        console.log(2, result);
        delay(1, (result) => {
            console.log(3, result);
        })
    })
})
```
첫번째 콜백 안에 1초를 걸고 다시 2번째 콜백안에 다시 1초는 거는 방법으로 비동기 형식을 1초마다 순차적으로 실행하고 있다. 하지만 여기서 코드의 순서를 조금 바꿔보자.  
```js
delay(1, (result) => {
    console.log(1, result);
    delay(1, (result) => {
        delay(1, (result) => {
            console.log(3, result);
        })
        console.log(2, result);
    })
})
```
결과값은 동일하게 나오지만 위에서 아래로 코드를 보았을 때 헷갈리기 쉽다. 그래서 좀 더 나은 가독성을 위해 promise를 사용하게 된다.  
그럼 위의 코드를 promise를 사용하여 동작하게 만들어 보자.  
```js
const delayP = (sec) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
                    resolve(new Date().toISOString());
                }, sec * 1000);
    })
}

delayP(1).then((result) => {
    console.log(1, result);
    return delayP(1);
}).then((result) => {
    console.log(2, result);
    return delayP(1);
}).then((result) => {
    console.log(3, result);
})
```
delayP라는 함수는 promise를 리턴한다. 그리고 promise를 생성할 때 콜백을 하나 넘기는데 (resolve,reject)라는 2가지 인자를 받는 콜백을 넘긴다. resolve는 할 일을 다 했을때 호출하게 되는 것이고, reject는 할 일을 하다가 예외가 발생했을 때 처리를 하게 된다.  
앞선 코드에서는 callback을 호출하였지만 여기서는 resolve를 호출하게 된다. resolve를 통해서 어떠한 결과값을 넘기게 되면 .then()에서 사용하는 함수에서 사용하게 된다. 그리고 다시 promise인 delayP(1)을 리턴하게 되면 다시 .then()으로 사용할 수 있게 된다.  
```js
delayP(1).then((result) => {
    console.log(1, result);
    return delayP(1);
}).then((result) => {
    console.log(2, result);
    return delayP(1);
}).then((result) => {
    console.log(3, result);
}).then((result) => {
    console.log(result)
})
```
위 코드에서 처럼 마지막에 promise를 리턴하지 않고 다음 .then()의 result를 console에 찍어보면 3번째 log가 찍히고 동시에 undefined가 나온다. 이것은 마지막에 아무것도 리턴하지 않아도 결국에 then의 return 값은 promise고 아무것도 리턴하지 않았다면 resolve가 된 promise를 return한다고 생각하면 된다. 그래서 바로 실행이 되는 것이다. 만약 
```js
delayP(1).then((result) => {
    console.log(1, result);
    return delayP(1);
}).then((result) => {
    console.log(2, result);
    return delayP(1);
}).then((result) => {
    console.log(3, result);
    return 'hello';
}).then((result) => {
    console.log(result)
})
```
 'hello'를 리턴하게 되면 3번째 로그 출력과 동시에 hello가 찍히게 된다. 왜냐하면 비동기 연산인 promise를 리턴하지 않았기 때문에 지연없이 마지막 로그가 찍히게 되는 것이다. 
