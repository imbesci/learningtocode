//// PIG LATIN //// 
function translatePigLatin(str) {
    let regexvowels = /[aeiou]/
    let firstVowelLoc = str.search(regexvowels)
  
  
    if (firstVowelLoc === -1){
      return str + 'ay'
    } else if (firstVowelLoc === 0) {
      return str+ 'way'
    } else {
      let prevowel = str.slice(0, firstVowelLoc)
      let postvowel = str.slice(firstVowelLoc)
      return postvowel + prevowel + 'ay'
    }
  }
  
  console.log(translatePigLatin(""));



///// SEARCH AND REPLACE //////
function myReplace(str, before, after) {

    let isUppercase = before.slice(0,1).search(/[A-Z]/) === -1 ? false : true;
    let replacement = after.toLowerCase();
    if (isUppercase){
      replacement = replacement.slice(0,1).toUpperCase() + replacement.slice(1)
    }
  
    return str.replace(before, replacement)
  
  }
  
  console.log(myReplace("A quick brown fox Jumped over the lazy dog", "Jumped", "leaped"))
  

  //FIND LETTER NOT IN ORDER 
  function fearNotLetter(str) {
    let alphabet = 'abcdefghijklmnopqrstuvwxyz';
    var startpoint = alphabet.indexOf(str.slice(0,1));
  
    for (let i = 0; i<str.length; i++){
      let strLetter = str.slice(i,i+1);
      let alphaLetter = alphabet.slice((startpoint+i),(startpoint+i+1));
      console.log([strLetter, alphaLetter])
      if (strLetter != alphaLetter) {
        return alphaLetter
      }
    }
  
  
    return undefined 
  }
  
  console.log(fearNotLetter("abcdefghijklmnopqrstuvwxyz"));