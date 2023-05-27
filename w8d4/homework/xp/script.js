//ex2
function displayStudentInfo(objUser) {
    //destructuring
    const { first, last } = objUser; 
  
    return `Your full name is ${first} ${last}`;
  }
  
  console.log(displayStudentInfo({ first: 'Elie', last: 'Schoppik' }));
  //ex3
  const users = { user1: 18273, user2: 92833, user3: 90315 }
  const usersArray = Object.entries(users);

  const modifiedArray = usersArray.map(([key, value]) => [key, value * 2]);

  console.log(modifiedArray);
  //ex4
  class Animal {
    constructor(name,type,color) {
      this.name = name;
      this.type = type;
      this.color = color;
    }
  };
  class Mamal extends Animal{
    constructor(name,type,color,animalSound){
        super(name,type,color)
        this.animalSound = animalSound
    }
    sound(animalSound) {
        return `The ${this.type} named ${this.name} is ${this.color} and makes the sound "${animalSound}".`;
      }
  }