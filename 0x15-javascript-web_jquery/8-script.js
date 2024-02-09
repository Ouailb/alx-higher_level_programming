// JavaScript code that fetches and lists the title for all movies

$(() => {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, status) => {
      if (status === 'success') {
        const movies = data.results;
        movies.forEach(movie => {
          $('#list_movies').append('<li>' + movie.title + '</li>');
        });
      }
    });
  });



  ///

  $(document).ready(function () {
    $.ajax({
      type: 'GET',
      url: 'https://swapi.co/api/films/?format=json',
      success: function (data) {
        $.each(data.results, function (i, film) {
          $('UL#list_movies').append('<li>' + film.title + '</li>');
        });
      }
    });
  });