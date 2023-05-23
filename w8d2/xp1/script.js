//ex2
const winBattle = () => true;

const experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints)

//ex3
const isString = (value) => typeof value === 'string' ? true : false;
//ex4
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
for (let i = 0; i < colors.length; i++) {
  console.log(`${i + 1}# choice is ${colors[i]}.`);
}
if (colors.includes("Violet")) {
    console.log("Yeah");
    } else {
    console.log("No...");
    }
//ex5
const ordinal = ["th","st","nd","rd"];

for (let i = 0; i < colors.length; i++) {
    let rank;
        rank = i + 1 + suffixes[i] 
        console.log("My", rank, "choice is", colors[i]);
}
//ex6

let bankAmount = 10000;
const vat = 17;
const details = ["-200", "-100", "-146", "+167", "+2900"];

function checkPositiveNegative(array) {
  array.forEach((expense) => {
    const value = parseInt(expense);
    if (value > 0) {
        bankAmount += expense * 0.83;
    } else {
        bankAmount += expense * 1.17;
    } 
  });

}

checkPositiveNegative(details);
console.log(bankAmount)
