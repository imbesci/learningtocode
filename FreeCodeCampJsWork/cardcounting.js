let count = 0;

function cc(card) {

    let posCards = [2,3,4,5,6];
    let negCards = [10, 'J', 'Q', 'K', 'A'];

    if (posCards.includes(card)){
        count++;
    } else if (negCards.includes(card)) {
        count--;
    } else {
        count+=0;
    }

    if (count>0){
        return count.toString() + ' Bet'
    } else {
        return count.toString() +' Hold'
    }
}

console.log(cc(2)); //cc(3); cc(7); cc('K'); cc('A');





class Thermostat {
    constructor(fahrenheit) {
      this.fahrenheit = fahrenheit;
    }
    
    get temperature() {
      return (5 / 9) * (this.fahrenheit - 32);
    }
    
    set temperature(celsius) {
      this.fahrenheit = (celsius * 9.0) / 5 + 32;
    }
  }






// Only change code below this line
class Thermostat {
    constructor(temperatureF){
      this.temperature = temperatureF;
      }
    get getCelsius(){
      return (5/9) * (this.temperature - 32);
      }
    set getCelsius(temperatureC) {
      this.temperature = (temperatureC * 9.0) / 5 + 32;
      }
  }





















