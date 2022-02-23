const names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"];

function golfScore(par, strokes) {

  let difference = par - strokes

  if (strokes === 1){
    return names[0]
  } else if (difference >= 2){
    return names[1]
  } else if (difference <= -3){
    return names[names.length-1]
  } else {
    return names[names.indexOf('Par')-difference]
  }
}

console.log(golfScore(5, 8));

