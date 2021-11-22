jQuery(document).ready(function($){
    //xử lý đóng mở menu
        $(document).on('click', ".icon-close, .over", function() {
            $('.over, .nav, .header-nav').fadeOut(300 , function() {
                $('.over').remove();
            });
            $('.nav').hide();
            $('.list-menu').hide()
            $('.header-nav').hide();
            $('.icon-menu').show(100)
        return false;
        });
        $('.icon-menu').click(function(){
            $('.nav').show();
            $('.header-nav').show();
            $('.list-menu').css('display','block')
            $('body').append('<div class="over">');
            $('.over').fadeIn();
        })
})