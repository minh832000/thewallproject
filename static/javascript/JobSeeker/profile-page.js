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

$(document).on('click', '.add-edit', function() {
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
            var m = d.getMonth() + 1;
            var d_str = `${d.getDate()}/${m}/${d.getFullYear()}`
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
            $('#displaySummaryInformation').text(res['summary']);
        },
        error: (error) => {
            console.log(error);
        }
    })
})

$(document).on('click', '#btn_submit_EducationForm', (e) => {
    e.preventDefault();
    // selecting elements which are related to admission time field
    var m_s = $('#month_start_EducationForm').val();
    var y_s = $('#year_start_EducationForm').val();
    var t_s = `${y_s}-${m_s}-01`;
    // selecting elements which are related to graduation time field
    var m_e = $('#month_end_EducationForm').val();
    var y_e = $('#year_end_EducationForm').val();
    var t_e = `${y_e}-${m_e}-01`;
    // selecting element form 
    var f = document.getElementById('educationForm');
    var fd = new FormData(f);
    fd.append('form', 'educationForm');
    fd.append('time_admission', t_s);
    fd.append('time_graduate', t_e);
    
    $.ajax({
        url: 'http://127.0.0.1:8000/profiles/',
        type: 'POST',
        data: fd,
        enctype: 'multipart/form-data',
        contentType: false,
        processData: false,
        success: (res) => {
            console.log(res);
            $('#frame-4').hide();
            $('.over-edit').remove();
            // Update the fields which are just changed
            $('#display_NameOfSchool').text(res['name_of_school'])
            $('#display_AcademicDegree').text(res['academic_degree'])
            $('#display_NameOfMajor').text(res['name_of_major'])
            $('#display_AdditionalEducation').text(res['additional_education'])

            var t_start = new Date(res['time_admission']);
            var m_start = t_start.getMonth() + 1;
            var t_end = new Date(res['time_graduate']);
            var m_end = t_end.getMonth() + 1;
            var t_str = `${m_start}/${t_start.getFullYear()} - ${m_end}/${t_end.getFullYear()}`;
            $('#display_TimeEducation').text(t_str);
        },
        error: (error) => {
            console.log(error);
        }
    })
})

$(document).on('click', '#btn_submit_WorkExperienceForm', e => {
    e.preventDefault();
    // selecting elements which are related to time start previous job
    let m_s = $('#month_start_WorkExperienceForm').val();
    let y_s = $('#year_start_WorkExperienceForm').val();
    let t_s = `${y_s}-${m_s}-01`;
    // selecting elements which are related to time end previous job
    let m_e = $('#month_end_WorkExperienceForm').val();
    let y_e = $('#year_end_WorkExperienceForm').val();
    let t_e = `${y_e}-${m_e}-01`;
    // selecting element form
    var f = document.getElementById('workExperienceForm');
    var fd = new FormData(f);
    fd.append('form', 'workExperienceForm');
    fd.append('time_start_previous_job', t_s);
    fd.append('time_end_previous_job', t_e);

    // Make a call ajax
    $.ajax({
        url: 'http://127.0.0.1:8000/profiles/',
        type: 'POST',
        data: fd,
        enctype: 'multipart/form-data',
        contentType: false,
        processData: false,
        success: (res) => {
            console.log(res);
            $('#frame-3').hide();
            $('.over-edit').remove();
            $('#display_name_PreviousCompany').text(res['name_of_previous_company']);
            $('#display_title_PreviousJob').text(res['previous_job_title']);
            // Convert datetime type of element in object json to datetime in javascript
            var t_start = new Date(res['time_start_previous_job']);
            var m_start = t_start.getMonth() + 1;

            var t_end = new Date(res['time_end_previous_job']);
            var m_end = t_end.getMonth() + 1;
            // => Result time previous job 
            var t_str = `${m_start}/${t_start.getFullYear()} - ${m_end}/${t_end.getFullYear()}`;
            $('#display_time_PreviousJob').text(t_str);
        },
        error: error => {
            console.log(error);
        }
    })
})

$(document).on('click', '#btn_submit_projectParticipatedForm', e => {
    e.preventDefault();
    // selecting form
    var f = document.getElementById('projectParticipatedForm');
    var fd = new FormData(f);
    fd.append('form', 'projectParticipatedForm');
    // make a ajax call
    $.ajax({
        url: 'http://127.0.0.1:8000/profiles/',
        type: 'POST',
        data: fd,
        enctype: 'multipart/form-data',
        contentType: false,
        processData: false,
        success: res => {
            console.log(res);
            $('#frame-6').hide();
            $('.over-edit').remove();
            $('#display_name_ProjectParticipated').text(res['name_of_project_participated']);
            $('#display_position_ProjectParticipated').text(res['position_in_project_participated']);
            $('#display_link_ProjectParticipated').text(res['link_of_project_participated']);
            $('#display_description_ProjectParticipated').text(res['description_project_participated']);
            $('btn-edit-6').removeClass('d-none');
        },
        error: err => {
            console.log(err);
        }
    })
})