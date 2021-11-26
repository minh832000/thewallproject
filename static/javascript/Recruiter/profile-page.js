$(document).on('click', '.control_change_profile_picture', function() {
      $('#id_changeProfilePicture').trigger('click');
})

$(document).on('click', '#btn_submit_basicInformationCompany', e => {
      e.preventDefault();
      // selecting form element
      var f = document.getElementById('form_basicInformationCompany');
      // creating new FormData object
      var fd = new FormData(f);
      fd.append('form', 'form_basic_information_company');

      $.ajax({
            url: 'http://127.0.0.1:8000/profiles/recruiter/',
            type: 'POST',
            data: fd,
            enctype: 'multipart/form-data',
            contentType: false,
            processData: false,
            success: res => {
                  $('#modal_basicInformationCompany').modal('hide');
                  // updating content of elements when data is updated
                  $('#id_display_name_of_company').text(res['name_of_company']);
                  $('#id_display_email_of_company').text(res['email_of_company']);
                  $('#id_display_hotline_of_company').text(res['hotline_of_company']);
                  $('#id_display_website_of_company').text(res['website_of_company']);
                  $('#id_display_location_of_company').text(res['location_of_company']);
                  $('#id_display_business_field_of_company').text(res['business_field_of_company']);
            },
            error: err => {
                  console.log(err)
            }
      })
})

$(document).on('change', '#id_changeProfilePicture', function(){
      var f = this;
      var url = $(this).val();
      var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
      if (f.files && f.files[0] && (ext == "gif" || ext == "png" || ext == "jpeg" || ext == "jpg")) {
            var reader = new FileReader();
            reader.onload = function(e){
                  $('#id_profilePictureCompany').attr('src', e.target.result);
                  $('#id_profile_picture_company_header').attr('src', e.target.result);
            }
            reader.readAsDataURL(f.files[0]);

            var fd = new  FormData();
            fd.append('form', 'form_change_profile_picture');
            fd.append('profile_picture', f.files[0]);

            $.ajax({
                  url: 'http://127.0.0.1:8000/profiles/recruiter/',
                  type: 'POST',
                  data: fd,
                  enctype: 'multipart/form-data',
                  contentType: false,
                  processData: false,
                  success: res => {
                        console.log(res);
                  },
                  error: err => {
                        console.log(err);
                  }
            })
      } else {
            alert('Hình ảnh không hợp lệ');
      }
})

$(document).on('click', '#btn_submit_SummaryCompany', e => {
      e.preventDefault();
      var f = document.getElementById('id_form_SummaryCompany');
      var fd = new FormData(f);
      fd.append('form', 'form_summary_company');
      
      // Make a ajax call
      $.ajax({
            url: 'http://127.0.0.1:8000/profiles/recruiter/',
            type: 'POST',
            data: fd,
            enctype: 'multipart/form-data',
            contentType: false,
            processData: false,
            success: res => {
                  $('#id_modal_SummaryCompany').modal('hide');
                  // Change elements show
                  $('#id_entry_summary_company').addClass('d-none');
                  $('#id_display_summary_company').removeClass('d-none');
                  // Update data
                  $('#id_display_summary_company').text(res['summary_company']);             
            },
            error: err => {
                  console.log(err)
            }
      })

})