const fs = require('fs');

function countStudents(path) {
  try {
    // Read the file synchronously
    const data = fs.readFileSync(path, 'utf8');
    
    // Split the content by new lines and filter out empty lines
    const lines = data.split('\n').filter(line => line.trim() !== '');

    // Parse the first line (headers)
    const headers = lines[0].split(',');

    // Initialize an object to store the counts and names for each field
    const studentsByField = {};

    // Loop through the lines (starting from line 1, as line 0 is headers)
    for (let i = 1; i < lines.length; i++) {
      const fields = lines[i].split(',');

      // Extract relevant data (assuming 'Field' and 'First Name' are present in headers)
      const field = fields[headers.indexOf('field')];
      const firstName = fields[headers.indexOf('firstname')];

      // Skip empty lines or lines with missing data
      if (!field || !firstName) continue;

      // If this field doesn't exist in the object, initialize it
      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }

      // Add the student's first name to the respective field's array
      studentsByField[field].push(firstName);
    }

    // Log the total number of students
    console.log(`Number of students: ${lines.length - 1}`); // Subtract 1 to exclude the header

    // Log the number of students and their names in each field
    for (const [field, names] of Object.entries(studentsByField)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }

  } catch (error) {
    // Handle the error if the file cannot be read
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;