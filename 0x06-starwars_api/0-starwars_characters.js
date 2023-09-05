#!/usr/bin/node

const request = require('request');

// confirm input
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

// Define the Star Wars API URL for fetching movie details
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch and print character names
function fetchAndPrintCharacterNames() {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode === 200) {
        const movie = JSON.parse(body);
        const characters = movie.characters;

        if (characters && characters.length > 0) {
          characters.forEach((characterUrl) => {
            // Fetch character details
            request(characterUrl, (charError, charResponse, charBody) => {
              if (!charError && charResponse.statusCode === 200) {
                const character = JSON.parse(charBody);
                console.log(`${character.name}`);
              } else {
                console.error('Error fetching character details:', charError);
              }
            });
          });
        } else {
          console.log(`No characters found for "${movie.title}".`);
        }
      } else {
        console.error('Request failed with status code:', response.statusCode);
      }
    }
  });
}

// Call the function to fetch and print character names
fetchAndPrintCharacterNames();

