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
        success: res => {
            console.log(res['summary'])
            $('#frame-2').hide();
            $('.over-edit').remove();
            if(res['is_updated_summary']) {
                $('#entry_section_Summary').addClass('d-none');
                $('#display_section_Summary').removeClass('d-none');

                $('#displaySummaryInformation').text(res['summary']);
            }
            else {
                $('#entry_section_Summary').addClass('d-none');
                $('#display_section_Summary').removeClass('d-none');
            }
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
            if(res['is_updated_education']) {
                $('#entry_section_Education').addClass('d-none');
                $('#display_section_Education').removeClass('d-none');
            }
            else {
                $('#entry_section_Education').removeClass('d-none');
                $('#display_section_Education').addClass('d-none');
            }
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
            // Update the fields which are just changed
            if(res['is_updated_previous_job']) {
                $('#entry_section_workExperience').addClass('d-none');
                $('#display_section_workExperience').removeClass('d-none');
            }
            else {
                $('#entry_section_workExperience').removeClass('d-none');
                $('#display_section_workExperience').addClass('d-none');
            }
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
            // Update the fields which are just changed
            if(res['is_updated_project_participated']) {
                $('#entry_section_projectParticipated').addClass('d-none');
                $('#display_section_projectParticipated').removeClass('d-none');
            }
            else {
                $('#entry_section_projectParticipated').removeClass('d-none');
                $('#display_section_projectParticipated').addClass('d-none');
            }
            $('#display_name_ProjectParticipated').text(res['name_of_project_participated']);
            $('#display_position_ProjectParticipated').text(res['position_in_project_participated']);
            $('#display_link_ProjectParticipated').text(res['link_of_project_participated']);
            $('#display_description_ProjectParticipated').text(res['description_project_participated']);
            $('#btn-edit-6').removeClass('d-none');
        },
        error: err => {
            console.log(err);
        }
    })
})

$(document).on('click', '#btn_submit_volunteeringActivityForm', e => {
    e.preventDefault();
    // selecting elements which are related to the volunteering start time
    var m_s = $('#month_start_volunteeringActivityForm').val();
    var y_s = $('#year_start_volunteeringActivityForm').val();
    var t_s = `${y_s}-${m_s}-01`;
    // selecting elements which are related to the volunteering end time
    var m_e = $('#month_end_volunteeringActivityForm').val();
    var y_e = $('#year_end_volunteeringActivityForm').val();
    var t_e = `${y_e}-${m_e}-01`;
    // selecting form element which is related to the volunteering
    var f = document.getElementById('volunteeringActivityForm');
    var fd = new FormData(f);
    fd.append('form', 'volunteeringActivityForm');
    fd.append('time_start_volunteering_activity', t_s);
    fd.append('time_end_volunteering_activity', t_e);
    //make a ajax call
    $.ajax({
        url: 'http://127.0.0.1:8000/profiles/',
        type: 'POST',
        data: fd,
        enctype: 'multipart/form-data',
        contentType: false,
        processData: false,
        success: res => {
            console.log(res);
            $('#frame-7').hide();
            $('.over-edit').remove();
            $('#btn-edit-7').removeClass('d-none');
            // update the fields which are just changed
            console.log(typeof(res['is_updated_volunteering_activity']));
            console.log(res['is_updated_volunteering_activity']);
            if (res['is_updated_volunteering_activity']) {
                $('#display_section_volunteeringActivity').removeClass('d-none');
                $('#entry_section_volunteeringActivity').addClass('d-none');
                console.log('true');
            } else {
                $('#display_section_volunteeringActivity').addClass('d-none');
                $('#entry_section_volunteeringActivity').removeClass('d-none');
                console.log('false');
            }
            $('#display_name_volunteeringActivity').text(res['name_of_volunteering_activity']);
            $('#display_role_volunteeringActivity').text(res['role_in_volunteering_activity']);
            // convert datetime type in javascript
            var t_start = new Date(res['time_start_volunteering_activity']);
            var m_start = t_start.getMonth() + 1;

            var t_end = new Date(res['time_end_volunteering_activity']);
            var m_end = t_end.getMonth() + 1;

            var t_str = `${m_start}/${t_start.getFullYear()} - ${m_end}/${t_end.getFullYear()}`;
            $('#display_time_volunteeringActivity').text(t_str);
        },
        error: err => {
            console.log(err);
        }        
    })
})

$(document).on('click', '#btn_submit_Interested-Job', e => {
    e.preventDefault();
    
    // selecting form element
    var f = document.getElementById('id_form_Interested-Job');
    // create new formdata object
    var fd = new FormData(f);
    fd.append('form', 'interested_job_form');
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
            // close modal
            $('#frame-8').hide();
            $('.over-edit').remove();
            $('#btn-edit-8').removeClass('d-none');
            // update the fields which are just changed
            if(res['is_updated_interested_job']){
                // change elements
                $('#id_entry_section_Interested_Job').addClass('d-none')
                $('#id_display_section_Interested_Job').removeClass('d-none')
                $('#btn-edit-8').removeClass('d-none');
                // change text of elements
                $('#id_display_name_of_interested_job').text(res['name_of_interested_job']);
                $('#id_display_desired_salary').text(res['desired_salary']);
                $('#id_display_desired_working_location').text(res['desired_working_location']);
                // check the array "list type of job"
                if(res['list_type_of_job']) {
                    for(var i of res['list_type_of_job']) {
                        $('id_display_list_type_job').append(`<li>${i}</li>`);
                    };
                };
            }
            else {
                // change elements
                $('#id_entry_section_Interested_Job').removeClass('d-none')
                $('#id_display_section_Interested_Job').addClass('d-none')
                $('#btn-edit-8').addClass('d-none');
            }
        },
        error: err => {
            console.log(err);
        }
    })
})

// Handle searching skill tag
const array_skill_tag = [];
$(document).on('keyup', '#id_search_skill_tag', function(e){
    e.preventDefault();
    var k = $(this).val();
    if(k){
        $.ajax({
            url: 'http://127.0.0.1:8000/tags/skill/',
            type: 'POST',
            data: {
                'key_word': k,
            },
            success: res => {
                $('#id_display_list_skill_tag').empty();
                if(res['is_found']) {
                    if(res['list_tag_skill']) {
                        console.log(res['list_tag_skill'].length)
                        if(res['list_tag_skill'].length > 1) {
                            for(var t of res['list_tag_skill']) {
                                if (array_skill_tag.length === 0){
                                    array_skill_tag.push(t.name)
                                }
                                else {
                                    if(!array_skill_tag.includes(t.name)) {
                                        array_skill_tag.push(t.name);
                                    }
                                }
                            }
                        }
                        else {
                            while(array_skill_tag.length > 0) {
                                array_skill_tag.pop();
                            }
                            for(var t of res['list_tag_skill']) {
                                if(!array_skill_tag.includes(t.name)) {
                                    array_skill_tag.push(t.name)
                                }
                            }
                        }
                       
                        for(var i of array_skill_tag) {
                            $('#id_display_list_skill_tag').append(
                                `<div class="form-check" style="width: 40%">
                                    <input
                                        name="suggested_tag_skill" 
                                        id="id_tag_skill"
                                        class="form-check-input"
                                        type="checkbox" 
                                        value="${i}"
                                    >
                                    <label 
                                        class="form-check-label"
                                        for="id_tag_skill"
                                    >
                                        ${i}
                                    </label>
                                </div>`
                            );
                        }
                    }
                }
                else {
                    $('#id_display_list_skill_tag').append('<p class="font-WorkSans-Light">Không tìm thấy kết quả</p>')    
                }
            },
            error: err => {
                console.log(err)
            }
        })
    }
    else {
        $('#id_display_list_skill_tag').empty();
    }
})

$(document).on('click', '#id_tag_skill', function(e){
    var v = $(this).val();
    var is_checked = $(this).attr('checked');
    console.log(is_checked)
    $('#id_display_selected_skill_tag').append(
        `<div 
            id="id_selected_skill_tag"
            class="bg-light px-3 py-2"
        >
            <input
                type="text"
                class="font-WorkSans-Medium bg-transparent border-0"
                value="${v}"
                name="list_skill_tag"
                readonly>   
            <i class="icon_remove_skill_tag icofont-close-line"></i>             
        </div>`
    )    
})

$(document).on('click', '.icon_remove_skill_tag', function(){
    var id_parent = $(this).parent().attr('id');
    
    if($(`#${id_parent}`).children().length === 0 ){
        $('#id_display_selected_skill_tag').append('<p class="color-gray-light px-5">Bạn chưa chọn kỹ năng nào</p>');
    }
    else {
        $(`#${id_parent}`).remove();
    }
})

$(document).on('click', '#id_btn_submit_Skill_Tag', e => {
    e.preventDefault();
    var f = document.getElementById('id_form_Skill_Tag');
    var fd = new FormData(f);
    fd.append('form', 'form_skill_tag');
    $.ajax({
        url: 'http://127.0.0.1:8000/profiles/',
        type: 'POST',
        data: fd,
        enctype: 'multipart/form-data',
        contentType: false,
        processData: false,
        success: res => {
             // close modal
             $('#frame-5').hide();
             $('.over-edit').remove();
             $('#btn-edit-8').removeClass('d-none');
            if(res['list_skill_tag']){
                $('#display_section_ProfessionalSkill').removeClass('d-none');
                $('#display_section_ProfessionalSkill').addClass('d-flex align-items-center justify-content-around')
                $('#entry_section_ProfessionalSkill').addClass('d-none');

                // Update
                for(var t of res['list_skill_tag']) {
                    $('#display_section_ProfessionalSkill').append(
                        `<span class="font-WorkSans-Regular px-3 py-1 bg-light">${t}</span>`
                    )

                }
            }
        },
        error: err => {
            console.log(err);
        }
    })
})