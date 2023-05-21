function playTheGame() {
    var playGame = confirm("Would you like to play the game?");
  
    if (!playGame) {
      alert("No problem, Goodbye.");
    } else {
      var userNumber = prompt("Enter a number between 0 and 10:");
  
      // Checking the validity of the user's number
      if (userNumber === null || userNumber === "") {
        alert("Invalid input. Please enter a number.");
      } else {
        userNumber = parseInt(userNumber); // Convert the user's input to an integer
  
        if (isNaN(userNumber)) {
          alert("Invalid input. Please enter a valid number.");
        } else if (userNumber < 0 || userNumber > 10) {
          alert("Number is not between 0 and 10. Please enter a valid number.");
        } else {
          // Valid number, continue with the game logic
          // Add your game logic here
          var computerNumber = Math.round(Math.random() * 10);

          compareNumbers(userNumber, computerNumber);
        }
      }
    }
  }
  

  function compareNumbers(userNumber, computerNumber) {
    var guesses = 0;
  
    while (guesses < 3) {
      if (userNumber === computerNumber) {
        alert("WINNER");
        return;
      } else if (userNumber > computerNumber) {
        userNumber = prompt("Your number is bigger than the computer's, guess again:");
      } else if (userNumber < computerNumber) {
        userNumber = prompt("Your number is smaller than the computer's, guess again:");
      }
  
      if (userNumber === null || userNumber === "") {
        alert("Invalid input. Please enter a number.");
      } else {
        userNumber = parseInt(userNumber);
  
        if (isNaN(userNumber)) {
          alert("Invalid input. Please enter a valid number.");
        } else if (userNumber < 0 || userNumber > 10) {
          alert("Number is not between 0 and 10. Please enter a valid number.");
        }
  
        guesses++;
      }
    }
  
    alert("Out of chances");
  }
  