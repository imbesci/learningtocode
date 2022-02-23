let p = new Promise((resolve, reject) => {
    let a = 1 + 1
    if (a==2) {
        resolve('Passed the test.')
    } else {
        reject('Failed the test.')
    }
});



p.then((message) =>{
    console.log('This is in the then: ' + message)
}).catch((message) => {
    console.log('This is in the catch: ' + message)
});