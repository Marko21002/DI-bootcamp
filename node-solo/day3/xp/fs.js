const fs = require ('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
  
    // Выводим содержимое в терминал
    console.log(data);
  });
 
  // Import the fs module


// Content to write in the text file
const content = 'This is the content that will be written to the file.';

// Create a new text file and write content to it
fs.writeFile('newFile.txt', content, (err) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log('File created and content written successfully!');
});

  
fs.open('newFile.txt', 'a', (err, fd) => {
    if (err) {
      console.error(err);
      return;
    }
  
    // Append the additional text to the file
    fs.appendFile(fd, '\nhello marko', (err) => {
      if (err) {
        console.error(err);
        return;
      }
  
      console.log('Text appended to the file successfully!');
      
      // Close the file
      fs.close(fd, (err) => {
        if (err) {
          console.error(err);
        }
      });
    });
  });
  const fileToDelete = 'newFile.txt';

// Delete the file
fs.unlink(fileToDelete, (err) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log('File deleted successfully!');
});
  
  