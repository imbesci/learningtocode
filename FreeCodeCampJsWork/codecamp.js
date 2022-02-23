function booWho(bool) {
    return bool === true || bool === false;
  }
  
booWho(null);


//---------------------------//


function titleCase(str) {
  let words = str.split(" ");
  for (let index in words) {
    let current = words[index];
    words[index] = current.charAt(0).toUpperCase() + current.slice(1).toLowerCase(); 
  }
  let final = words.join(' ');
  return final;
};


//----------------------------//


console.log(titleCase("I'm a LITTLE tea pot"));


