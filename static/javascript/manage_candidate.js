$(document).on('change','#select-job', function(){
    var val=$('#select-job').val()
    $.ajax({
        url: 'show/',
        type: 'post', // This is the default though, you don't actually need to always mention it
        data:{
            'id-post':val
        },
        success: function(data) {
            if(data.data==='success')
            alert('Bạn đã ứng tuyển thành công!!!');
            else alert("Đã có lỗi, vui lòng thử lại sau")
        },
    }); 
})