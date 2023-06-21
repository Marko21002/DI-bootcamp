const express = require("express");
const app = express();

const bodyParser = require("body-parser");
const db = require("./db");

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.get("/", async (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  try {
    // Query the database for the provided username and password
    const user = await db('register')
      .where({ username, password })
      .first();

    if (user) {
      // Login successful
      res.status(200).json({ message: 'Login successful' });
    } else {
      // Login failed
      res.status(401).json({ message: 'Invalid username or password' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

app.post("/register", async (req, res) => {
  console.log(req.body);
  console.log(req.body.email);
  console.log(req.body.username);
  console.log(req.body.password);

  db("register")
    .insert({
      email: req.body.email,
      username: req.body.username,
      password: req.body.password,
    })
    .then((data) => {
      console.log(data);
     
    });

  return res.json({
    message: "success",
  });
});

app.listen(3000, () => {
  console.log("Example app listening on port 3000!");
});
