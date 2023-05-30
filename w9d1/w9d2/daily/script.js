function makeAllCaps(array) {
    return new Promise((resolve, reject) => {
      if (Array.isArray(array)) {
        const capitalized = array.map((word) => {
          if (typeof word === 'string') {
            return word.toUpperCase();
          } else {
            reject(new Error('non string'));
          }
        });
        resolve(capitalized);
      } else {
        reject(new Error('Input is not an array.'));
      }
    });
  }
  function sortWords(words) {
    return new Promise((resolve, reject) => {
      if (Array.isArray(words)) {
        if (words.length > 4) {
          const sortedWords = words.sort();
          resolve(sortedWords);
        } else {
          reject(new Error('Array length is not bigger than 4.'));
        }
      } else {
        reject(new Error('Input is not an array.'));
      }
    });
  }
  




  makeAllCaps([1, "pear", "banana"])
  .then((arr) => sortWords(arr))
  .then((result) => console.log(result))
  .catch(error => console.log(error,Number(array.length)))  

  //2nd
  const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`

  function ToJs(jsonString){
    const jsonObject = JSON.parse(jsonString);
    console.log(jsonObject)
  }