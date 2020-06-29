// const sum = (x, y) => {
//     return x + y
// }
// console.log(sum(1,2))

// const sum = (x, y) => {
//     if(typeof x !== 'number' || typeof y !== 'number'){
//         throw '숫자가 아닙니다'
//     }
//     return x + y
// }
// console.log(sum('1',2))

// const f2 = () => {
//     console.log('f2 start');
//     throw 'error';
//     console.log('f2 end');
// }

// const f1 = () => {
//     console.log('f1 start');
//     try{
//         f2();
//     } catch(e) {
//         console.log(e);
//     }
//     console.log('f1 end')
// }

// console.log('will : f1');
// f1();
// console.log('did : f1');

const f2 = () => {
    console.log('f2 start');
    throw new Error('error');
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