const slugify = require('slugify');

const text = 'Hello World! This is a sample text.';
const slug = slugify(text, {
  replacement: '-',  // Replace spaces with -
  lower: true        // Convert to lowercase
});

console.log(slug);  // Output: hello-world-this-is-a-sample-text
