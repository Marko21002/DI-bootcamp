const http = require('http');

const user = {
  firstname: 'John',
  lastname: 'Doe'
};

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify(user));
});

server.listen(8080, 'localhost', () => {
  console.log('Server running at http://localhost:8080/');
});
