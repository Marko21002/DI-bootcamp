function isDivisible() {
    var sum = 0;
  
    for (var i = 0; i <= 500; i++) {
      if (i % 23 === 0) {
        console.log(i);
        sum += i;
      }
    }
  
    console.log("Sum of numbers divisible by 23: " + sum);
  }
  
  //ex2
  const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

const shoppingList = ["banana","orange","apple"]
function myBill() {
    let totalPrice = 0;
  
    for (let i = 0; i < shoppingList.length; i++) {
      const item = shoppingList[i];
  
      if (item in stock && stock[item] > 0) {
        totalPrice += prices[item];
        stock[item]--;
      }
    }
  
    return totalPrice;
  }
const totalBill = myBill();
console.log("Total Bill:", totalBill);

//ex3
function changeEnough(itemPrice, amountOfChange){
    let sum = (amountOfChange[0] * 0.25) + (amountOfChange[1] * 0.10) + (amountOfChange[2] * 0.05) + (amountOfChange[3] * 0.01)
    if (sum >= itemPrice){
        return true
    }
    else{
        return false
    }
}
//ex4 
function hotelCost() {
    let nights;
    while (true) {
      nights = prompt("Please enter the number of nights:");
      if (!isNaN(nights)) {
        break;
      }
      alert("Invalid input. Please enter a valid number of nights.");
     }
     return nights * 140;
  }
  function planeRideCost(){
    let destination;
    do {
        destination = prompt("");
      } while (destination === null || typeof destination !== "string" || destination.trim() === "");
    const lowercasedDestination = destination.toLowerCase();

    if (lowercasedDestination === "london") {
        return 183;
      } else if (lowercasedDestination === "paris") {
        return 220;
      } else {
        return 300;
      }
    }
function rentalCarCost(){
    let days;
    while (true) {
        days = prompt("Please enter the number of nights:");
        if (!isNaN(days)) {
          break;
        }
        alert("Invalid input. Please enter a valid number of nights.");
       }
    let totalPrice = 40 * days;
    if (days >= 10){
        totalPrice -= totalPrice * discount;
    }
    return totalPrice;
}
function totalVacationCost() {
    const hotelCost = hotelCost();
    const planeCost = planeRideCost();
    const carRentalCost = rentalCarCost();
  
    const totalCost = hotelCost + planeCost + carRentalCost;
  
    console.log(`The car cost: $${carRentalCost}, the hotel cost: $${hotelCost}, the plane tickets cost: $${planeCost}.`);
    return totalCost;
  }
//ex5

const containerDiv = document.getElementById('container');
console.log(containerDiv);

const peteElement = document.querySelector('.list:first-child li:nth-child(2)');
peteElement.textContent = 'Richard';

const sarahElement = document.querySelector('.list:last-child li:nth-child(2)');
sarahElement.remove();

for (let i = 1; i < 3; i++) {
    const Myname = document.querySelector('.list:first-child li:nth-child(' + i + ')');
    Myname.textContent = 'Marko';
  }

const ulElements = document.querySelectorAll('ul');
ulElements.forEach((ulElement) => {
    ulElement.className += ' student_list';
  });
  
const firstUlElement = document.querySelector('ul:first-of-type');
firstUlElement.classList.add('university', 'attendance');

const containrDiv = document.getElementById('container');
containerDiv.style.backgroundColor = 'pink';
containerDiv.style.padding = '10px';

const danLiElement = document.querySelector('ul:last-of-type li:last-of-type');
danLiElement.style.display = 'none';

const richardLiElement = document.querySelector('ul li:nth-child(2)');
richardLiElement.style.border = '1px solid black';

document.body.style.fontSize = '16px';

//ex6
const divElement = document.getElementById('navBar');
divElement.setAttribute('id', 'socialNetworkNavigation');

const newListItem = document.createElement('li');

const textNode = document.createTextNode('Logout');

newListItem.appendChild(textNode);

const ulElement = document.querySelector('#socialNetworkNavigation ul');
ulElement.appendChild(newListItem)

const ulElements1 = document.querySelectorAll('ul');

ulElements.forEach((ulElement) => {
  // Retrieve the first <li> element and display its text
  const firstLiElement = ulElement.firstElementChild;
  console.log(firstLiElement.textContent);

  // Retrieve the last <li> element and display its text
  const lastLiElement = ulElement.lastElementChild;
  console.log(lastLiElement.textContent);
});

