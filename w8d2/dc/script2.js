let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

const displayFruits = () => {
    groceries.fruits.forEach((fruit) => {
      console.log(fruit);
    });
  };
  
  displayFruits();

const cloneGroceries = () =>{
    let user = client;
    client = "Betty"
    let shopping = { ...groceries };
    shopping.totalPrice = "35$";
    shopping.other.payed = false;

console.log(user);
console.log(shopping);

}
cloneGroceries();
console.log(groceries)