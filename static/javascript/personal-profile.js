$(document).on('click', '#btn-edit', function(){
    $('#frame-1').show();
    $('body').append('<div class="over-edit">');
    $('.over-edit').fadeIn();
})
$(document).on('click', ".i-close, .over-edit, btn-cancel", function() {
    $('.over-edit, #frame-1').fadeOut(300 , function() {
        $('.over-edit').remove();
    });
    $('#frame-1').hide();
return false;
});
$(document).on('click', '.add-edit', function(){
    var idBtn = '#'+this.id;
    var numberBtn = idBtn.slice(-1);
    var idFrame= '#frame-'+ numberBtn;
        $(idFrame).show();
        $('body').append('<div class="over-edit">');
        $('.over-edit').fadeIn();
    $(document).on('click', ".i-close, .over-edit, .btn-cancel", function() {
        $('.over-edit',idFrame).fadeOut(300 , function() {
            $('.over-edit').remove();
        });
        $(idFrame).hide();
    return false;
    });
})