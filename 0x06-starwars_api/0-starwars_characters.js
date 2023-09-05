#!/usr/bin/node

const request = require('request-promise'); // Use 'request-promise' for Promise-based requests

// Confirm input
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

// Define the Star Wars API URL for fetching movie details
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch and print character names
async function fetchAndPrintCharacterNames () {
  try {
    const movie = await request(apiUrl, { json: true });

    if (movie && movie.characters && movie.characters.length > 0) {
      const characterPromises = movie.characters.map((characterUrl) => {
        return request(characterUrl, { json: true });
      });

      const characters = await Promise.all(characterPromises);

      characters.forEach((character) => {
        console.log(`${character.name}`);
      });
    } else {
      console.log(`No characters found for "${movie.title}".`);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Call the function to fetch and print character names
fetchAndPrintCharacterNames();
