//ex1
function compareToTen(num){
    return new Promise((resolve,reject)=> {
        if (num < 10){
            resolve(`${num} is less than 10.`)
        }else{
            reject(`${num} is greater than or equal to 10.`)
        }
    })
}
//In the example, the promise should reject
compareToTen(15)
  .then(result => console.log(result))
  .catch(error => console.log(error))

//In the example, the promise should resolve
compareToTen(8)
  .then(result => console.log(result))
  .catch(error => console.log(error))

//2
const delay = () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve("success");
      }, 4000);
    });
  };

delay()
  .then((result) => {
    console.log(result); // Output: "success"
  })
  .catch((error) => {
    console.log("Oops, something went wrong:", error);
  });

//3
const resolvedPromise = Promise.resolve(3);
const rejectedPromise = Promise.reject("Boo!");

resolvedPromise
  .then((value) => {
    console.log("Resolved:", value); // Output: Resolved: 3
  })
rejectedPromise
.catch((error) => {
    console.log("Rejected:", error); // Output: Rejected: Boo!
  });