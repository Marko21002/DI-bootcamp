const express = require('express');
const app = express();
const path = require('path');

const publicPath = path.join(__dirname, 'public');

app.use(express.static(publicPath));
app.use(express.urlencoded({ extended: true }));

app.get('/aboutMe/:hobby', (req, res) => {
  const hobby = req.params.hobby;

  if (typeof hobby !== 'string') {
    res.status(404).send('Invalid hobby');
  } else {
    res.send(`My hobby is ${hobby}`);
  }
});

app.get('/pic', (req, res) => {
  res.sendFile(path.join(publicPath, 'picture.html'));
});

app.get('/form', (req, res) => {
  res.sendFile(path.join(publicPath, 'form.html'));
});

app.post('/formData', (req, res) => {
  const { email, message } = req.body;
  res.send(`${email} sent you a message: "${message}"`);
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
