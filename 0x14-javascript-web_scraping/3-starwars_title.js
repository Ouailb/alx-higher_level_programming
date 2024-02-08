#!/usr/bin/env node


const request = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + episodeNum, function (err, response, body) {
  if (err)
  {
    console.log(err);
  }
  else if (response.statusCode === 200)
  {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  }
  else
  {
    console.log('Error code: ' + response.statusCode);
  }
});
///
const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Unable to fetch movie details. Status code: ${response.statusCode}`);
    process.exit(1);
  }

  const movieDetails = JSON.parse(body);
  console.log(movieDetails.title);
});
