// setTimeout(function(){
//     console.log('hello');
// }, 1000)

function fakeSetTimeout(callback, delay){
    callback();
}

// console.log(0);
// fakeSetTimeout(() =>
//  console.log('hello') 
// , 0);
// console.log(1)

console.log(0);
setTimeout(() =>
 console.log('hello') 
, 0);
console.log(1)