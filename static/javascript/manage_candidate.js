$(document).on('change','#select-job', function(){
    console.log($('#select-job').val())
    $('.candidate-item').hide();
    $('.candidate-item').each(function(index){
        var idPost=$('.id_post').val()
        if(idPost===$('#select-job').val()){
            console.log($('#select-job').val())
            $('.item-'+idPost).show()
        }
    })
})


$(".btn-refuse-cand").click(function(){
    var idApply=this.id
    console.log(idApply)

    $.ajax({
        url: 'refuse-cand/',
        type: 'post', // This is the default though, you don't actually need to always mention it
        data:{
            'idApply':idApply
        },
        success: function(data) {
            alert(data.data)
            },
    }); 
    

})
$(".btn-accept-cand").click(function(){
    var idApply=this.id
    console.log(idApply)
    $.ajax({
        url: 'accept/',
        type: 'post',
        data:{
            'idApply':idApply
        },
        success: function(data) {
            alert(data.data)
            },
    }); 
    
})
