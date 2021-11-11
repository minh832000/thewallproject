$(document).on('click', '#btn-edit', function(){
    $('#frame-1').show();
    $('body').append('<div class="over-edit">');
    $('.over-edit').fadeIn();
});

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
});

// Make the ajax call
$(document).on('click', '#submitBasicInformationForm', (e) => {
    e.preventDefault();

    formData = $('#basicInformationForm').serializeArray();

    jsonData = {
        form: 'basicInformationForm',
    };
    for (let i = 0; i < formData.length; i++) {
        jsonData[formData[i]['name']] = formData[i]['value'];
    } 
    
    // Convert object "jasonData" to JSON 
    content = JSON.stringify(jsonData);
    // Print data in console to check 
    console.log(content);

    // Make a ajax call
    $.ajax({
        url: 'http://127.0.0.1:8000/profiles/',
        type: 'POST',
        data: content,
        success: (dataResponse) => {
            console.log(dataResponse);
            $('#frame-1').hide();
            $('.over-edit').remove();
            // Change text in element to show information change
            $('#displayFullName').text(dataResponse['full_name']);
            $('#displayPhoneNumber').text(dataResponse['phone_number']);
            $('#displayAddress').text(dataResponse['address'])
        },
        error: (error) => {
            console.log('Can not send with error' + error);
        }
    })
})
