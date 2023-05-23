//ex1
const sum = (num1, num2) => num1 + num2;

//ex2
function convert(kilos){
    return kilos * 1000;
}
console.log(convert(10))

const convert2 = function(kilos) {
    return kilos * 1000;
    };
console.log(convert2(5))

// Function declaration is hoisted, function expression is not.

//ex3
(function(numchild, name, location, job) {
    const sentence = `You will be a ${jobTitle} in ${location}, and married to ${name} with ${numchild} kids.`;;
  })(2, "John", "New York", "Software Engineer");

//ex4
function makeJuice(size) {
    const ingredients = [];
  
    function addIngredients(ingredient1, ingredient2, ingredient3) {
      ingredients.push(ingredient1, ingredient2, ingredient3);
    }
  
    function displayJuice() {
      const sentence = `The client wants a ${size} juice, containing ${ingredients.join(", ")}.`;
      console.log(sentence);
    }
  
    addIngredients("apple", "orange", "banana");
    addIngredients("strawberry", "mango", "pineapple");
    displayJuice();
  }
  
  makeJuice("large");
  