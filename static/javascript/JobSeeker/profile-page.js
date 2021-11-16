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
        $('.over-edit', idFrame).fadeOut(300 , function() {
            $('.over-edit').remove();
        });
        $(idFrame).hide();
    return false;
    });
});

// Make the ajax call
$(document).on('click', '#submitBasicInformationForm', (e) => {
    e.preventDefault();
    // selecting id of the form
    var f = document.getElementById('basicInformationForm');
    // selecting gender radio button
    var inputGender = $("input[type='radio'][name='gender']:checked").val();
    var gender = inputGender?inputGender:"";
    // selecting date of birth
    var d = $('#dayBirth').val();
    var m = $('#monthBirth').val();
    var y = $('#yearBirth').val();
    var birth = `${y}-${m}-${d}`; // string of datetime type
    // creating a new FormData object
    var fd = new FormData(f);
    fd.append('form', 'basicInformationForm');
    fd.append('gender', gender)
    fd.append('date_of_birth', birth)

    // Make a ajax call
    $.ajax({
        url: 'http://127.0.0.1:8000/profiles/',
        type: 'POST',
        data: fd,
        enctype: 'multipart/form-data',
        contentType: false,
        processData: false,
        success: (res) => {
            console.log(res);
            $('#frame-1').hide();
            $('.over-edit').remove();
            // Change text in element to show information change
            $('#displayFullName').text(res['full_name']);
            $('#displayPhoneNumber').text(res['phone_number']);
            $('#displayAddress').text(res['address']);
    
            if (res['gender'] == "2") {
                $('#displayGender').text('Nữ');
            };
            if (res['gender'] == "1") {
                $('#displayGender').text("Nam");
            };

            var d = new Date(res['date_of_birth']);
            var d_str = `${d.getDate()}/${d.getMonth()}/${d.getFullYear()}`
            $('#displayDateOfBirth').text(d_str)
        },
        error: (error) => {
            console.log('Can not send with error' + error);
        }
    })
})

$(document).on('change', '#changeProfilePicture', function() {
    var f = this;
    var url = $(this).val();
    var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
    if (f.files && f.files[0] && (ext == "gif" || ext == "png" || ext == "jpeg" || ext == "jpg")) {
        var reader = new FileReader();
        reader.onload = function (e) {
           $('#profilePicture').attr('src', e.target.result);
        }
       reader.readAsDataURL(f.files[0]);

       var fd = new FormData();
       fd.append('form', 'changeProfilePicture');
       fd.append('image', f.files[0]);
       $.ajax({
           url: 'http://127.0.0.1:8000/profiles/',
           type: 'POST',
           data: fd,
           enctype: 'multipart/form-data',
           contentType: false,
           processData: false,
           success: (res) => {

           },
           success: (res) => {
               console.log('Upload Profile Image Success ');
           },
           error: (error) => {
               console.log(error)
           }
       })
    }
    else {
        alert('Hình ảnh không hợp lệ.')
    }
})

$(document).on('click', '#submitSummaryForm', (e) => {
    e.preventDefault();
    var f = document.getElementById('summaryForm');
    var fd = new FormData(f);
    fd.append('form', 'summaryForm');
    console.log(fd);
    $.ajax({
        url: 'http://127.0.0.1:8000/profiles/',
        type: 'POST',
        data: fd,
        enctype: 'multipart/form-data',
        contentType: false,
        processData: false,
        success: (res) => {
            $('#updateSummaryInformation').addClass('d-none');
            var e_str = `<p class="font-WorkSans-Regular">${res['summary']}</p>`;
            $('#displaySummaryInformation').html(e_str);
        },
        error: (error) => {
            console.log(error);
        }
        
    })
})