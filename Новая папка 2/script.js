// Ex1
const people = ["Greg", "Mary", "Devon", "James"];

people.shift() //removes greg

const indexToReplace = people.indexOf("James");
if (indexToReplace !== -1) {
  people[indexToReplace] = "Jason";
} //replaces James with jason

people.push('Marko')// added my name to the end

const maryIndex = people.indexOf("Mary");
console.log(maryIndex); // Output: 0

const copy = people.slice(1, 3);// copy without Mary end my name

const FooIndex = people.indexOf("Foo");// return -1 because we dont have Foo in array

const last = people[people.length - 1];// indexes in array starts from zero so index of last is lenght-1

var lits = [1,2,3,4]

//Pt2
for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
  }
for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
    if (people[i] === "Devon") {
      break;
    }
  }
  
//Ex2
const colors = ["black", "white", "purple", "blue", "red"];
const suffixes = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
    let rank;
        rank = i + 1 + suffixes[i] 
        console.log("My", rank, "choice is", colors[i]);
}

//ex3 
let number = Number(prompt("Please enter a number:"));

while (typeof number === 'number' && number < 10) {
  number = Number(prompt("Please enter a new number:"));
}

console.log("The number is now greater than or equal to 10.");

//ex4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building.numberOfFloors)
console.log(building.numberOfAptByFloor.firstFloor,building.numberOfAptByFloor.thirdFloor)

console.log(building.nameOfTenants[1],building.numberOfRoomsAndRent.dan[0])
const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
}

console.log("Updated Dan's rent:", building.numberOfRoomsAndRent.dan[1]);

//ex5 
const family = {
    father: "John",
    mother: "Lisa",
    son: "Tom",
    daughter: "Emily"
  };
for (let key in family) {
    console.log(key);
  }

for (let key in family) {
    console.log(family[key]);
  }

//ex 6

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  };

let sentence = ''

for (let key in details) {
    sentence += key + ' ' + details[key] + ' ';
  }
  
  console.log(sentence.trim());

//ex7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let societyName = "";
const sortedNames = names.sort();
for (let i = 0; i < sortedNames.length; i++) {
  societyName += sortedNames[i][0];
}

console.log("The name of their secret society:", societyName);


const rows = 6;
let field = '';

for (let i = 1; i <= rows; i++) {
  field += '* ';
  console.log(field);
}