const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');

  res.write('<h1>1st</h1>');
  res.write('<h1>2nd</h1>');
  res.write('<p>3rd</p>');

  res.end();
});

server.listen(3000, 'localhost', () => {
  console.log('Server running at http://localhost:3000/');
});
