jQuery(document).ready(function($){
    var content= $('.post-content').text()
    console.log(content)
    $('.post-content').empty()
    $('.post-content').append(content)
})