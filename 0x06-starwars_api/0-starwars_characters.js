#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    const name = await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        }
        resolve(JSON.parse(body).name);
      });
    });
    console.log(name);
  }
}
);
