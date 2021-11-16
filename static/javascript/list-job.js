jQuery(document).ready(function($){
    //xử lý đóng mở menu
        $(document).on('click', ".overr", function() {
            $('.overr').fadeOut(300 , function() {
                $('.overr').remove();
            });
            $('.filter').hide(300);
        return false;
        });    
    //xử lý nút lưu post
        $(document).on('click','.icon-save', function(){
            var idIcon ='#'+ this.id;
            if($(idIcon).hasClass("far")){ //nên thay lại bằng điều kiện từ csdl
                $(idIcon).attr('class', "fas fa-bookmark icon-save");
                $(idIcon).css("color", "#FFE600")
            }
            else {
                $(idIcon).attr('class', "far fa-bookmark icon-save");
                $(idIcon).css("color", "#000")
            }
        })
        

    
})
const filterTypeJob=(val)=>{
    console.log(val)
    $.ajax({
        type: 'POST',
        url:"filter/",
        data:{
            'value':val
        },
        success: (res) => {
            console.log(res)
        }
    })
}

$("input[name='type-job']").click(function(){
    var checkTypeJob=$("input[name='type-job']");
    var result=[];
    
    $(checkTypeJob).each(function (index, check) {
        if ($(check).prop('checked') === true){
            result[index] = $(check).val();
        }
    });
    filterTypeJob(result)
})