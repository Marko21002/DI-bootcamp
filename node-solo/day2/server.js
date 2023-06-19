 const express = require('express');
 const app = express();
 const port = 3000

// app.get('/users', (req, res) => {
//   const user = {
//     firstname: 'John',
//     lastname: 'Doe'
//   };
  
//   res.json(user);
// });

// app.listen(3000, () => {
//   console.log('Server running at http://localhost:3000/');
// });



app.get('/:id', (req, res) => {
  const id = req.params.id;
  const responseObject = { id: id };

  console.log(responseObject);

  res.json(responseObject);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
