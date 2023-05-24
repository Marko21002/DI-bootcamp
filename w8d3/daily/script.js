function getCarHonda(carInventory){
    for (let i = 0; i < carInventory.length; i++){
        if (carInventory[i].car_make === "Honda"){
            const car = carInventory[i];
            return `This is a ${car.car_make} ${car.car_model} from ${car.car_year}.`;
        }
      }
        }
    


const inventory = [
    { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
    { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
    { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
    { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
    { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
  ];
  getCarHonda(inventory);


function sortCarInventoryByYear(carInventory){
    carInventory.sort((a,b) => a.car_year - b.car_year);
  
  // Return the sorted car inventory
  return carInventory;
}

const sorted = sortCarInventoryByYear(inventory)
console.log(sorted)

