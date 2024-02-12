$(document).ready(function () {
    $('DIV#add_item').click(function () {
      $('UL.my_list').append('<li>Item</li>');
    });
    $('DIV#remove_item').click(function () {
      $('UL.my_list li:last-child').remove();
    });
    $('DIV#clear_list').click(function () {
      $('UL.my_list').empty('ul');
    });
  });

  //

  $('document').ready(function () {
    $('DIV#add_item').click(function () {
      $('UL.my_list').append('<li>oy</li>');
    });
    $('DIV#remove_item').click(function () {
      $('UL.my_list li:first').remove();
    });
    $('DIV#clear_list').click(function () {
      $('UL.my_list').empty();
    });
  });

  ///

  document.addEventListener('DOMContentLoaded', function () {
    // Function to add a new element to the list
    function addItem() {
      $('.my_list').append('<li>Item</li>');
    }

    // Function to remove the last element from the list
    function removeItem() {
      $('.my_list li:last-child').remove();
    }

    // Function to clear all elements from the list
    function clearList() {
      $('.my_list').empty();
    }

    // Event listener for adding an item
    $('#add_item').click(addItem);

    // Event listener for removing the last item
    $('#remove_item').click(removeItem);

    // Event listener for clearing the entire list
    $('#clear_list').click(clearList);
  });
