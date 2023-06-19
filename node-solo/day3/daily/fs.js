const fs = require('fs');

// Read the 'RightLeft' file
fs.readFile('RightLeft.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const symbols = data.trim(); // Remove any leading/trailing whitespace
  let position = 0;

  // Iterate through each symbol and update the position accordingly
  for (const symbol of symbols) {
    if (symbol === '>') {
      position += 1; // Move 1 step to the right
    } else if (symbol === '<') {
      position -= 1; // Move 1 step to the left
    }
  }

  console.log('Final position:', position);
});
