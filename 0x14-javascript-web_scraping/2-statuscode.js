#!/usr/bin/env node

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});

/// another module like request = axios

const axios = require('axios');
const URL = process.argv[2];

axios.get(URL)
  .then(response => {
    console.log('code: ' + response.status);
  })
  .catch(error => {
    console.error(error.message);
  });
  
///
  const axios = require('axios');

  axios.get(process.argv[2])
    .then(({ status }) => console.log(`code: ${status}`))
    .catch(error => console.error(error.message));
