jQuery(document).ready(function($){
    var content= $('.post-content').text()
    $('.post-content').empty()
    $('.post-content').append(content)
    var x = location.href;

    
    $('.cp-btn').click(function(){
        $('#url-web').select();
        document.execCommand('copy');
        $('.copied').text('Đã sao chép liên kết')
    })
    if($('.table-share').css('display')==='block'){
        $('.table-share').on('clickout', function (e) {
            $('.table-share').hide()
        })
    }
    $('.btn-share').click(function(){
        $('.table-share').toggle()
        $('#url-web').attr('value',x)
    })
    const sendRequestApply=(val)=>{
        $.ajax({
            url: 'apply/',
            type: 'post', // This is the default though, you don't actually need to always mention it
            data:{
                'id-post':val
            },
            success: function(data) {
                if(data.data==='success')
                alert('Bạn đã ứng tuyển thành công!!!');
                else if(data.data==='error'){
                    alert('Bạn đã ứng tuyển công việc này rồi')
                }
                else alert("Đã có lỗi, vui lòng thử lại sau")
            },
        }); 
    }
    $(document).on('click','.btn-apply',function(){
        sendRequestApply($(".id-post").val())
        console.log($(".id-post").val())
        $('.btn-apply').prop('disabled', true);
    })
})