const http = require('http');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('Hello Holberton School!');
});

app.listen(1242, () => {
  console.log('...');
});

module.exports = app;
