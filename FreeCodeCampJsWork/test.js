let userLeft = false 
let userWatchingCatMeme = false


// function watchTutorialCallback(callback, errorCallback) {

//     if (userLeft) {
//       errorCallback({
//         name: 'User Left', 
//         message: ':('
//       })
//     } else if (userWatchingCatMeme) {
//       errorCallback({
//         name: 'User Watching Cat Meme',
//         message: 'WebDevSimplified < Cat' 
//       })
//     } else {
//       callback('Thumbs up and Subscribe')
//     }
//   }
  

// watchTutorialCallback(message => {
//     console.log(message)
//     }, error => {
//     console.log(error.name + ' ' + error.message)
//     })
  

const watchTutPromise = new Promise((resolve, reject) => {
    if (userLeft){
        reject('kekw') 
    }
    else if (userWatchingCatMeme) {
        reject('megakekw')
    }
    else {
        resolve('😂😂😂😊😊')
    }
}
)

watchTutPromise.then((message) => {console.log("resolved " + message)})
    .then(console.log('this came after'))
    .catch((message) => console.log('caught '+ message))
    .finally(console.log(`this is the finally clause`))