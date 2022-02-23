function countdown(n){ //define function

    //base case is n = 0
    if (n < 1) {
      return []; //when the base case is hit, we return an empty array
    } else {

        /* this is the recursive step that goes until we hit the base case
        which makes an empty array. So when the base case hits, 
        we intitialize countArray as an empty list */
      const countArray = countdown(n - 1); 

      /*after hitting the base case, we are able to get actual numbers for the output of the recursion
        which we append to the array*/

      countArray.unshift(n);
      return countArray;
    }
  }
  
  console.log(countdown(10))



  //Same principles just different function that has range limits//

  function rangeOfNumbers(startNum, endNum) {
    if (endNum < startNum){
    return [];
    } else {
      const rangeArray = rangeOfNumbers(startNum, endNum-1)
      rangeArray.push(endNum)
      return rangeArray
    }
  };

console.log(rangeOfNumbers(1,15))