$(document).on('change','#select-job', function(){
    console.log($('#select-job').val())
    $('.candidate-item').hide();
    $('.candidate-item').each(function(index){
        var idPost=$('.id_post').val()
        if(idPost===$('#select-job').val()){
            console.log($('#item-'+idPost))
            $('.item-'+idPost).show()
        }
    })
})