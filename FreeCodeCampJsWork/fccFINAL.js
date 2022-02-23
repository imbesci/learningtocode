// Palindrome Checker
// Return true if the given string is a palindrome. Otherwise, return false.
// A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing.
// Note: You'll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) and turn everything into the same case (lower or upper case) in order to check for palindromes.
// We'll pass strings with varying formats, such as racecar, RaceCar, and race CAR among others.
// We'll also pass strings with special symbols, such as 2A3*3a2, 2A3 3a2, and 2_A3*3#A2.
function palindrome(str) {
    let regex = /[a-zA-Z0-9]+/g
    let matches = str.match(regex)
    console.log(matches)
    let lettersOnly = matches.join('').toLowerCase()
    let forwards= lettersOnly
    console.log(lettersOnly)
    let backwards = lettersOnly
      .split('')
      .reverse()
      .join('')
    return backwards === forwards
  }

// Roman Numeral Converter
// Convert the given number into a roman numeral.
// All roman numerals answers should be provided in upper-case.
function convertToRoman(num) {
    //Arrays in parallel
    let levelOne = ['I','II','III','IV','V','VI','VII','VIII','IX']
    let levelTwo = ['X','XX','XXX','XL','L','LX','LXX','LXXX', 'XC']
    let levelThree = ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    let remainder = parseInt(num.toString().slice(-1))
    num = num - remainder
    //Final Return Value
    let roman = '';
    //Figure out the amount of each denomination we need, in descending order
    let thousands = Math.floor(num/1000)
    num = num - (thousands * 1000)
    for (let i=0;i<thousands;i++)
      roman+='M'
    let hundreds = Math.floor(num/100)
    num = num - (hundreds * 100)
    if (hundreds !=0)
      roman+= levelThree[hundreds-1]
    let tens = Math.floor(num/10)
    num = num - (tens * 10)
    if (tens !=0)
      roman+= levelTwo[tens-1]
    if(remainder!=0)
      roman+=levelOne[remainder-1]
    return roman 
  }
//Caesars Cipher
// One of the simplest and most widely known ciphers is a Caesar cipher, also known as a shift cipher. In a shift cipher the meanings of the letters are shifted by some set amount.
// A common modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places. Thus A ↔ N, B ↔ O and so on.
// Write a function which takes a ROT13 encoded string as input and returns a decoded string.
// All letters will be uppercase. Do not transform any non-alphabetic character (i.e. spaces, punctuation), but do pass them on.
function rot13(str) {
    //alphabet reference guide
    let alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    let strLetters = str.split('')
    console.log(strLetters)
    for (let ind in strLetters){
        //make sure the current index is a letter before trying to convert it. We want to preserve punctuation marks.
      if(/\w+/g.test(strLetters[ind])){
        let index = alphabet.indexOf(strLetters[ind]) - 13
        if (index<0){
        index += 26
        } 
        strLetters[ind] = alphabet.slice(index, index+1)
      }
    }
    return strLetters.join('')
  }
  
//   Telephone Number Validator
//   Return true if the passed string looks like a valid US phone number.
//   The user may fill out the form field any way they choose as long as it has the format of a valid US number. The following are examples of valid formats for US numbers (refer to the tests below for other variants):
//   555-555-5555 , (555)555-5555,  (555) 555-5555, 555 555 5555,  5555555555,  1 555 555 5555
//   For this challenge you will be presented with a string such as 800-692-7753 or 8oo-six427676;laskdjf. Your job is to validate or reject the US phone number based on any combination of the formats provided above. The area code is required. If the country code is provided, you must confirm that the country code is 1. Return true if the string is a valid US phone number; otherwise return false.

function checkCountryCode(numsFound){
    let numLen = numsFound.length
    if (numLen===11 && numsFound[0] === '1'){
      return true
    }
    return false
  }
  function checkFormat(str){
    let noWhitespaces = str.split(' ').join('')
    console.log(noWhitespaces)
    let regex = /^1{0,1}\(\d{3}\)\d{3}-{0,1}\d{4}$|^1{0,1}\d{3}-{0,1}\d{3}-{0,1}\d{4}$/g
    console.log(regex.test(noWhitespaces) +' here')
    return regex.test(noWhitespaces)
  }
  
  function telephoneCheck(str) {
    let numReg = /\d+/g
    let numsFound = str.match(numReg).join('').split('')
    if (numsFound.length<10 || numsFound.length>11)
      return false
    if (numsFound.length === 11)
      if (!checkCountryCode(numsFound))
        return false
    if(!checkFormat(str)){
      return false}
    return true
  }

// Cash Register
// Design a cash register drawer function checkCashRegister() that accepts purchase price as the first argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument.
// cid is a 2D array listing available currency.
// The checkCashRegister() function should always return an object with a status key and a change key.
// Return {status: "INSUFFICIENT_FUNDS", change: []} if cash-in-drawer is less than the change due, or if you cannot return the exact change.
// Return {status: "CLOSED", change: [...]} with cash-in-drawer as the value for the key change if it is equal to the change due.
// Otherwise, return {status: "OPEN", change: [...]}, with the change due in coins and bills, sorted in highest to lowest order, as the value of the change key.

function calcRegisterTotal(reg){
    let total = 0.00
    for (let i=0; i<reg.length;i++){
      total += reg[i][1]
    }
    return total
  }
  
  function calculateChange(due, reg){
    console.log(due)
    let valueArr = [.01, .05, .1, .25, 1, 5, 10, 20, 100]
    let moneyGiven = []
    for (let i=reg.length-1; i>=0; i--){
      //make sure we have some # of bills, and that the bills arent too big to use as change
      if(reg[i][1] === 0 || due < valueArr[i]){
        continue}
      let numBills = Math.floor(reg[i][1]/valueArr[i])
      let usableBills = Math.floor((due+.01)/valueArr[i])
      let billsUsed = Math.min(numBills, usableBills)
      due = due - (billsUsed * valueArr[i])
      moneyGiven.push([reg[i][0], (billsUsed*valueArr[i])])
    }
  
    if (due <= 0){
      return ({status: 'OPEN', change: [...moneyGiven]})
    } else {
      return ({status: "INSUFFICIENT_FUNDS", change: []})
    }
  }
  
  function checkCashRegister(price, cash, reg) {
    let changeNeeded = cash-price;
    let totalMoney = calcRegisterTotal(reg)
    //console.log(totalMoney)
    if (changeNeeded > totalMoney){
      return ({status: "INSUFFICIENT_FUNDS", change: []})
    }
    if (changeNeeded === totalMoney) {
      return ({status:'CLOSED', change:[...reg]})
    }
    if(changeNeeded < totalMoney){
      let change = calculateChange(changeNeeded, reg)
      console.log(change) 
      return change
    }
};