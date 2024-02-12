
  $('document').ready(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $('INPUT#btn_translate').click(function () {
      $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
        $('DIV#hello').html(data.hello);
      });
    });
  });

  ///

  $(document).ready(function () {
    $('INPUT#btn_translate').click(function () {
      $('DIV#hello').empty();
      const len = $('INPUT#language_code').val();
      $.ajax({
        type: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=' + len,
        success: function (data) {
          $('DIV#hello').append(data.hello);
        }
      });
    });
  });