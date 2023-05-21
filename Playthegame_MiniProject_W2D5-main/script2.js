var number = Number(prompt("How many bottles at start"));
var pass = 1;

while (number > 0) {
  if (number === 1) {
    console.log(`${number} bottle of beer on the wall`);
    console.log(`${number} bottle of beer`);
    console.log(`Take 1 down, pass it around`);
    console.log('End of the song');
    break;
  } else {
    if (pass > number) {
      console.log(`There is only ${number} bottle(s) left, so we take ${number} and that's all`);
      break;
    }
    console.log(`${number} bottles of beer on the wall`);
    console.log(`${number} bottles of beer`);
    console.log(`Take ${pass} down, pass them around`);
    number -= pass;
    pass++;
  }
}
