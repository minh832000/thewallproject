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

$(".btn-accept-cand").click(function(){
    var idCandidate=this.id
    console.log(idCandidate)
    $.ajax({
        url: 'accept/',
        type: 'post', // This is the default though, you don't actually need to always mention it
        data:{
            'id-candidate':idCandidate
        },
        success: function(data) {
            alert(data.data)
        },
    }); 
})

$(".btn-refuse").click(function(){
    var idCandidate=this.id
    console.log(idCandidate)
    $.ajax({
        url: 'refuse/',
        type: 'post', // This is the default though, you don't actually need to always mention it
        data:{
            'id-candidate':idCandidate
        },
        success: function(data) {
            alert(data.data)
        },
    }); 
})