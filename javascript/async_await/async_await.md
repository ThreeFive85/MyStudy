**async/await**은 promise처럼 비동기를 다룬다. 그러나 promise와는 조금 다른 사용법을 가지고 있고 promise를 이용해서 비동기처리를 한다.  
  
```js
const myFunc = () => {
    return 'func';
}

const myAsync = async() => {
    return 'async';
}

console.log(myFunc());
console.log(myAsync());

=============================
리턴값:
func
Promise { 'async' }
```
  첫번째 myFunc함수에서는 리턴은 문자열로 했기때문에 결과값이 문자열이 나오게 된다. 두번째 myAsync함수는 async를 선언하고 리턴을 문자열로 하였다. 그러면 myAsync함수는 promise를 리턴한다.  
  그럼 promise를 리턴하니 promise에서 사용했던 then을 쓸 수 있다는 이야기다. 
```js
myAsync().then((result) => {
    console.log(result);
})
// result는 'async'가 된다.
```
즉 **async**는 pomise를 리턴하는 함수로 만들어 준다. 기존의 promise 사용은 명시적으로 **new Promise**를 사용하여 promise를 리턴하여야 했지만 **async**를 사용하면 그럴 필요가 없다. 
  
promise에서는 비동기 연산을 하되 비동기 연산이 끝나면 resolve함수를 실행하고 실패하면 reject함수를 실행했다면 async에서는 resolve로 넘기는 값을 최종적으로 리턴하면 되고 만약 reject를 해야 한다면 async함수 안에서 에러를 throw하면 된다.  
    
await은 이름에서부터 알 수 있듯이 무언가를 기다린다. promise가 resolve되서 결과값이 넘어 올때까지 기다린다. 
```js
const delayP = (sec) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
                    resolve(new Date().toISOString());
                }, sec * 1000);
    })
}

const myAsync = async() => {
    delayP(3).then((time) => {
        console.log(time);
    })
    return 'async';
}

myAsync().then((result) => {
    console.log(result);
})
```
위 코드에서 순서는 어떻게 될까? delayP함수가 비동기이므로 그래서 바로 리턴이 먼저 일어나고 3초 뒤에 시간이 찍힌다. 근데 여기서 3초 동안 기다리게 하고 싶다면? 이때 await을 사용하면 된다. 
```js
const myAsync = async() => {
   await delayP(3).then((time) => {
        console.log(time);
    })
    return 'async';
}
```
그러면 3초를 기다렸다가 시간과 'async'가 동시에 출력된다. 즉 promise가 resolve 될 때까지 코드가 다음 줄로 넘어가지 않는 것이다.  
await을 사용하면 promise가 resolve되서 받은 결과값을 마치 일반 함수의 리턴값을 받듯이 사용할 수도 있다.
```js
const time = await delayP(3);
```
  
```js
const delayP = (sec) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
                    resolve(new Date().toISOString());
                }, sec * 1000);
    })
}

const myAsync = async() => {
    const result = await delayP(3).then((time) => {
        return 'x';
    });
    console.log(result);
    return 'async';
}

myAsync()
```
여기서 리턴값은 무엇이 될까? 3초 뒤 'x'가 찍히게 된다. 왜냐하면 await 뒤에 붙은 
```js
delayP(3).then((time) => {
        return 'x';
    });
```
까지의 코드에서 delayP()에 결과값을 받아 최종적으로 리턴하는 값이 result에 들어가게 된다.  
  
또 한가지의 특징은 일반함수 앞에 await을 넣어도 잘 동작한다. 꼭 Promise를 리턴하지 않아도 된다.
```js
const normalFun = () => {
    return 'wow';
}
const myAsync = async() => {
    const result = await normalFun();
    console.log(result);
    return 'async';
}
```
  
정리를 해보자면 new Promise를 사용하는 것이나 async를 사용하는 것이나 둘 다 Promise를 리턴하는 것이기 때문에 동작하는 방법은 같다. 호출해서 then을 통해서 resolve된 값을 받는 것이다. Promise를 명시적으로 쓸 때는 resolve함수를 파라미터로 받아서 결과값을 resolve로 넘기게 되는데 async는 우리가 일반함수를 사용하듯이 쓴다. 하지만 그것의 리턴값이 결국엔 promise의 resolve값이 되는 것이다. 그리고 async과 쌍을 이루는 await은 기다리는 함수다. 그것이 promise면 promise가 resolve되기를 기다리고 그냥 함수면 그냥 리턴되는 것이다. 


