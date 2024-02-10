// 9-script.js

$(document).ready(function () {
    // Fetch data from the URL using $.ajax
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
      method: 'GET',
      success: function (data) {
        // Display the translation in the DIV#hello
        $('#hello').text(data.hello);
      },
      error: function (error) {
        console.error('Error fetching data:', error);
      }
    });
  });