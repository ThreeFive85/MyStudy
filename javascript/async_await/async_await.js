const delayP = (sec) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
                    resolve(new Date().toISOString());
                }, sec * 1000);
    })
}

const myFunc = () => {
    return 'func';
}

// const myAsync = async() => {
//     await delayP(3).then((time) => {
//         console.log(time);
//     })
//     return 'async';
// }

// const myAsync = async() => {
//     const time = await delayP(3);
//     console.log(time);
//     return 'async';
// }

// const myAsync = async() => {
//     const result = await delayP(3).then((time) => {
//         return 'x';
//     });
//     console.log(result);
//     return 'async';
// }

const normalFun = () => {
    return 'wow';
}
const myAsync = async() => {
    const result = await normalFun();
    console.log(result);
    return 'async';
}

// console.log(myFunc());
// console.log(myAsync());

// myAsync().then((result) => {
//     console.log(result);
// })
myAsync()