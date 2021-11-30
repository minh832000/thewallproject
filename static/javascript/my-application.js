jQuery(document).ready(function($){
    $(document).on('click','#btn-submitted', function() {
        $('.application-submitted').show();
        $('.application-accepted').hide();
    })
    $(document).on('click','#btn-accepted', function() {
        $('.application-submitted').hide();
        $('.application-accepted').show();
    })
})