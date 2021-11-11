$(document).on('click', '#showMenu', () => {
      $('.icon-close-menu').addClass('d-block');
      $('#mainMenu').addClass('d-block');
      $('body').append('<div class="overlay"></div>');
      $('.overlay').fadeIn();
})

$(document).on('click', '.overlay, .icon-close-menu', () => {
      $('.overlay, #mainMenu').fadeOut(300, () => {
            $('.overlay').remove();
      });
      $('#mainMenu').addClass('d-none');
      return false;
})