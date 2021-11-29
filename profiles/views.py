from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View
import datetime

from .models import Profile as ProfileModel
from .models import RecruiterProfile as RecruiterProfileModel

from fields_job.models import FieldJob as FieldJobModel

UserModel = get_user_model()

# Clase-based Views Handle Job Seeker's Profile
class Profile(LoginRequiredMixin, View):
      def get(self, request):
            # Get username
            username = request.user
            try:
                  user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                  print('User\'s account does not exist')
            # Check user's account
            if user.is_job_seeker:
                  try:
                        profile = ProfileModel.objects.get(user=username)
                  except ProfileModel.DoesNotExist:
                        print('User\'s profile does not exist')

                  try:
                        list_job_fields = list(FieldJobModel.objects.all())
                  except ValueError:
                        print('Get data from field job model is fail')
                  # Prepare data needed for user
                  context = {
                        'user': user,
                        'profile': profile,
                        'profile_picture_link': profile.profile_picture.url,
                        'list_job_fields': list_job_fields,
                  }
                  return render(request, 'profiles/JobSeeker/profile-page.html', context)
            if user.is_recruiter:
                  return redirect('/profiles/recruiter/')

      def post(self, request, *args, **kwargs):
            if request.method == 'POST' and request.is_ajax():
                  # Get username of user
                  username = request.user
                  # Check user's account which is the correct user type
                  try:
                        user = UserModel.objects.get(username=username)
                  except UserModel.DoesNotExist:
                        print('User\'s account does not exist')
                  if user.is_job_seeker:
                        print(request.POST)
                        name_of_form = request.POST.get('form')

                        try:
                              instance = ProfileModel.objects.get(user=username)
                        except ProfileModel.DoesNotExist:
                              instance = ProfileModel.objects.create(user=username)
                              
                        if request.POST.get('form') == 'basicInformationForm':
                              # Get all field date of POST
                              full_name = request.POST.get('full_name') if request.POST.get('full_name') else None
                              phone_number = request.POST.get('phone_number') if request.POST.get('phone_number') else None
                              address = request.POST.get('address') if request.POST.get('address') else None
                              gender = request.POST.get('gender') if request.POST.get('gender') else None
                              date_of_birth = request.POST.get('date_of_birth') if request.POST.get('date_of_birth') else None
                              # Update fields in Profile model
                              if full_name:
                                    instance.full_name = full_name
                              if phone_number:
                                    instance.phone_number = phone_number
                              if address:
                                    instance.address = address
                              if gender:
                                    instance.gender = gender
                              # Handle with datetime type 
                              date_string = date_of_birth
                              date_format = '%Y-%m-%d'
                              try:
                                    date_obj = datetime.datetime.strptime(date_string, date_format)
                              except ValueError:
                                    print("Incorrect date format, should be YYYY-MM-DD")
                              try: 
                                    instance.date_of_birth = date_obj
                              except ValueError:
                                    print('Cannot save date to model')
                              
                              # Save all things which are just updated
                              instance.save()

                              return JsonResponse({
                                    'full_name': instance.full_name,
                                    'phone_number': instance.phone_number,
                                    'address': instance.address,
                                    'gender': instance.gender,
                                    'date_of_birth': instance.date_of_birth,
                              }, safe=False, content_type='application/json')
                        if request.POST.get('form') == 'changeProfilePicture':
                              img = request.FILES.get('image') if request.FILES.get('image') else None
                              if img:
                                    instance.profile_picture = img
                              instance.save()
                              return JsonResponse({ 'message': 'Uploaded'}, safe=False)
                        if request.POST.get('form') == 'summaryForm':
                              summary = request.POST.get('summary') if request.POST.get('summary') else None
                              if summary:
                                    instance.summary = summary.strip()
                                    instance.is_updated_summary = True
                              else: 
                                    instance.is_updated_summary = False
                              instance.save()
                              return JsonResponse({
                                    'is_updated_summary': instance.is_updated_summary,
                                    'summary': instance.summary,
                              }, safe=False, content_type='application/json')
                        if request.POST.get('form') == 'educationForm':
                              # Get all field data of POST
                              name_of_school = request.POST.get('name_of_school') if request.POST.get('name_of_school') else None
                              academic_degree = request.POST.get('academic_degree') if request.POST.get('academic_degree') else None
                              name_of_major = request.POST.get('name_of_major') if request.POST.get('name_of_major') else None
                              time_admission = request.POST.get('time_admission') if request.POST.get('time_admission') else None
                              time_graduate = request.POST.get('time_graduate') if request.POST.get('time_graduate') else None
                              is_studying = True if request.POST.get('is_studying') == '1' else False
                              additional_education = request.POST.get('additional_education') if request.POST.get('additional_education') else None
                              # Update fields in Profile model
                              if name_of_school:
                                    instance.name_of_school = name_of_school.strip()
                              if academic_degree:
                                    instance.academic_degree = academic_degree.strip()
                              if name_of_major:
                                    instance.name_of_major = name_of_major.strip()
                              # Handle with datetime type 
                              if time_admission:
                                    date_string = time_admission
                                    date_format = '%Y-%m-%d'
                                    try:
                                          date_obj = datetime.datetime.strptime(date_string, date_format)
                                    except ValueError:
                                          print("Incorrect date format, should be YYYY-MM-DD")
                                    try: 
                                          instance.time_admission = date_obj
                                    except ValueError:
                                          print('Cannot save date to model')
                              if time_graduate:
                                    date_string = time_graduate
                                    date_format = '%Y-%m-%d'
                                    try:
                                          date_obj = datetime.datetime.strptime(date_string, date_format)
                                    except ValueError:
                                          print("Incorrect date format, should be YYYY-MM-DD")
                                    try: 
                                          instance.time_graduate = date_obj
                                    except ValueError:
                                          print('Cannot save date to model')
                              if is_studying:
                                    instance.is_studying = is_studying
                              if additional_education:
                                    instance.additional_education = additional_education.strip()
                              if name_of_school or academic_degree or name_of_major or time_admission or time_graduate or is_studying or additional_education:
                                    instance.is_updated_education = True
                              else: 
                                    instance.is_updated_education = False
                              instance.save()
                              return JsonResponse({
                                    'is_updated_education': instance.is_updated_education,
                                    'name_of_school': instance.name_of_school,
                                    'academic_degree': instance.academic_degree,
                                    'name_of_major': instance.name_of_major,
                                    'time_admission': instance.time_admission,
                                    'time_graduate': instance.time_graduate,
                                    'is_studying': instance.is_studying,
                                    'additional_education': instance.additional_education
                              }, safe=False, content_type='application/json')
                        if request.POST.get('form') == 'workExperienceForm':
                              # Get all data fields of POST 
                              name_of_previous_company = request.POST.get('name_of_previous_company') if request.POST.get('name_of_previous_company') else None
                              previous_job_title       = request.POST.get('previous_job_title') if request.POST.get('previous_job_title') else None
                              time_start_previous_job  = request.POST.get('time_start_previous_job') if request.POST.get('time_start_previous_job') else None
                              time_end_previous_job    = request.POST.get('time_end_previous_job') if request.POST.get('time_end_previous_job') else None
                              # Update fields of the model
                              if name_of_previous_company:
                                    instance.name_of_previous_company = name_of_previous_company.strip()
                              if previous_job_title:
                                    instance.previous_job_title = previous_job_title.strip()
                              # Handle datetime type in python
                              if time_start_previous_job:
                                    date_string = time_start_previous_job
                                    date_format = '%Y-%m-%d'
                                    try:
                                          date_obj = datetime.datetime.strptime(date_string, date_format)
                                    except ValueError:
                                          print("Incorrect date format, should be YYYY-MM-DD")
                                    try: 
                                          instance.time_start_previous_job = date_obj
                                    except ValueError:
                                          print('Cannot save date to model')
                              if time_end_previous_job:
                                    date_string = time_end_previous_job
                                    date_format = '%Y-%m-%d'
                                    try:
                                          date_obj = datetime.datetime.strptime(date_string, date_format)
                                    except ValueError:
                                          print("Incorrect date format, should be YYYY-MM-DD")
                                    try: 
                                          instance.time_end_previous_job = date_obj
                                    except ValueError:
                                          print('Cannot save date to model')
                              if name_of_previous_company or previous_job_title or time_start_previous_job or time_end_previous_job:
                                    instance.is_updated_previous_job = True
                              else:
                                    instance.is_updated_previous_job = False
                              # Save all things to database
                              instance.save()
                              return JsonResponse({
                                    'is_updated_previous_job': instance.is_updated_previous_job,
                                    'name_of_previous_company': instance.name_of_previous_company,
                                    'previous_job_title': instance.previous_job_title,
                                    'time_start_previous_job': instance.time_start_previous_job,
                                    'time_end_previous_job': instance.time_end_previous_job,
                              }, safe=False, content_type='application/json')
                        if request.POST.get('form') == 'projectParticipatedForm':
                              # Get all data fields of POST
                              name_of_project_participated     = request.POST.get('name_of_project_participated') if request.POST.get('name_of_project_participated') else None
                              position_in_project_participated = request.POST.get('position_in_project_participated') if request.POST.get('position_in_project_participated') else None
                              link_of_project_participated     = request.POST.get('link_of_project_participated') if request.POST.get('link_of_project_participated') else None
                              description_project_participated = request.POST.get('description_project_participated') if request.POST.get('description_project_participated') else None
                              # Update fields of the model
                              if name_of_project_participated:
                                    instance.name_of_project_participated = name_of_project_participated.strip()
                              if position_in_project_participated:
                                    instance.position_in_project_participated = position_in_project_participated.strip()
                              if link_of_project_participated:
                                    instance.link_of_project_participated = link_of_project_participated.strip()
                              if description_project_participated:
                                    instance.description_project_participated = description_project_participated.strip()
                              if name_of_project_participated or position_in_project_participated or  link_of_project_participated or description_project_participated:
                                    instance.is_updated_project_participated = True
                              else:
                                    instance.is_updated_project_participated = False
                              # Save all things to database
                              instance.save()
                              return JsonResponse({
                                    'is_updated_project_participated': instance.is_updated_project_participated,
                                    'name_of_project_participated': instance.name_of_project_participated,
                                    'position_in_project_participated': instance.position_in_project_participated,
                                    'link_of_project_participated': instance.link_of_project_participated,
                                    'description_project_participated': instance.description_project_participated,
                              }, safe=False, content_type='application/json')
                        if request.POST.get('form') == 'volunteeringActivityForm':
                              # Get all data fields of POST
                              name_of_volunteering_activity    = request.POST.get('name_of_volunteering_activity') if request.POST.get('name_of_volunteering_activity') else None
                              role_in_volunteering_activity    = request.POST.get('role_in_volunteering_activity') if request.POST.get('role_in_volunteering_activity') else None
                              time_start_volunteering_activity = request.POST.get('time_start_volunteering_activity') if request.POST.get('time_start_volunteering_activity') else None
                              time_end_volunteering_activity   = request.POST.get('time_end_volunteering_activity') if request.POST.get('time_end_volunteering_activity') else None
                              # Update fields of the model
                              if name_of_volunteering_activity:
                                    instance.name_of_volunteering_activity = name_of_volunteering_activity.strip()
                              if role_in_volunteering_activity:
                                    instance.role_in_volunteering_activity = role_in_volunteering_activity.strip()
                              # Handle datetime type in python
                              if time_start_volunteering_activity:
                                    date_string = time_start_volunteering_activity
                                    date_format = '%Y-%m-%d'
                                    try:
                                          date_obj = datetime.datetime.strptime(date_string, date_format)
                                    except ValueError:
                                          print("Incorrect date format, should be YYYY-MM-DD")
                                    try: 
                                          instance.time_start_volunteering_activity = date_obj
                                    except ValueError:
                                          print('Cannot save date to model')
                              if time_end_volunteering_activity:
                                    date_string = time_end_volunteering_activity
                                    date_format = '%Y-%m-%d'
                                    try:
                                          date_obj = datetime.datetime.strptime(date_string, date_format)
                                    except ValueError:
                                          print("Incorrect date format, should be YYYY-MM-DD")
                                    try: 
                                          instance.time_end_volunteering_activity = date_obj
                                    except ValueError:
                                          print('Cannot save date to model')
                              if name_of_volunteering_activity or role_in_volunteering_activity or time_start_volunteering_activity or time_start_volunteering_activity:
                                    instance.is_updated_volunteering_activity = True
                              else:
                                    instance.is_updated_volunteering_activity = False
                              # Save all things to database
                              instance.save()
                              return JsonResponse({
                                    'name_of_volunteering_activity': instance.name_of_volunteering_activity,
                                    'role_in_volunteering_activity': instance.role_in_volunteering_activity,
                                    'time_start_volunteering_activity': instance.time_start_volunteering_activity,
                                    'time_end_volunteering_activity': instance.time_end_volunteering_activity,
                                    'is_updated_volunteering_activity': instance.is_updated_volunteering_activity,
                              }, safe=False, content_type='application/json')
                        if name_of_form == 'interested_job_form':
                              # Get all data fields of POST
                              name_of_interested_job   = request.POST.get('name_of_interested_job') if request.POST.get('name_of_interested_job') else None
                              desired_salary           = request.POST.get('desired_salary') if request.POST.get('desired_salary') else None
                              desired_working_location = request.POST.get('desired_working_location') if request.POST.get('desired_working_location') else None
                              list_type_of_job         = request.POST.getlist('list_type_of_job') if request.POST.getlist('list_type_of_job') else None

                              # Update fields of the model
                              if name_of_interested_job:
                                    instance.name_of_interested_job = name_of_interested_job.strip()
                              if desired_salary:
                                    instance.desired_salary = desired_salary.strip()
                              if desired_working_location:
                                    instance.desired_working_location = desired_working_location.strip()
                              if list_type_of_job:
                                    instance.list_type_of_job = list_type_of_job                              
                              if name_of_interested_job or list_type_of_job or desired_salary or desired_working_location:
                                    instance.is_updated_interested_job = True
                              else: 
                                    instance.is_updated_interested_job = False
                              # Save all thing to database
                              instance.save()
                              return JsonResponse({
                                    'name_of_interested_job': instance.name_of_interested_job,
                                    'desired_salary': instance.desired_salary,
                                    'desired_working_location': instance.desired_working_location,
                                    'list_type_of_job': instance.list_type_of_job,
                                    'is_updated_interested_job': instance.is_updated_interested_job,
                              }, safe=False, content_type='application/json')

                  if user.is_recruiter:
                        return redirect('/profiles/recruiter/')
            return JsonResponse({'error': 'Submit error', }, safe=False)

# Class-based Views Handle Recruiter's Profile      
class RecruiterProfile(LoginRequiredMixin, View):
      def get(self, request):
            # Get username of user's account
            username = request.user
            # Check user'account
            try:
                  user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                  print('User\'s account does not exist.')
            if user.is_recruiter:
                  try:
                        recruiter_profile = RecruiterProfileModel.objects.get(user=username)
                  except RecruiterProfileModel.DoesNotExist:
                        recruiter_profile = RecruiterProfileModel.objects.create(user=username)
                  
                  # Send data needed to user
                  context = {
                        'account': user,
                        'recruiter_profile': recruiter_profile,
                        'profile_picture_company_link': recruiter_profile.profile_picture_company.url,
                  }
                  return render(request, 'profiles/Recruiter/profile-page.html', context)
            if user.is_job_seeker:
                  return redirect('/profiles/')
            return JsonResponse({'message': 'Tài khoản đăng nhập không phù hợp.'})

      def post(self, request):
            if request.method == 'POST' and request.is_ajax():
                  # Get username
                  username = request.user
                  print(request.POST)
                  # Check user account
                  try:
                        user = UserModel.objects.get(username=username)
                  except UserModel.DoesNotExist:
                        print('User account does not exist')
                  if user.is_recruiter:
                        print(request.POST)
                        try:
                              instance = RecruiterProfileModel.objects.get(user=username)
                        except RecruiterProfileModel.DoesNotExist:
                              instance = RecruiterProfileModel.objects.create(user=username)
                        # Get name of the form
                        form_name = request.POST.get('form')
                        # Check form_name to choose the function
                        if form_name == 'form_basic_information_company':
                              name_of_company           = request.POST.get('name_of_company') if request.POST.get('name_of_company') else None
                              email_of_company          = request.POST.get('email_of_company') if request.POST.get('email_of_company') else None
                              hotline_of_company        = request.POST.get('hotline_of_company') if request.POST.get('hotline_of_company') else None
                              website_of_company        = request.POST.get('website_of_company') if request.POST.get('website_of_company') else None
                              location_of_company       = request.POST.get('location_of_company') if request.POST.get('location_of_company') else None
                              business_field_of_company = request.POST.get('business_field_of_company') if request.POST.get('business_field_of_company') else None
                             
                              if name_of_company:
                                    instance.name_of_company = name_of_company
                              if email_of_company:
                                    instance.email_of_company = email_of_company
                              if hotline_of_company:
                                    instance.hotline_of_company = hotline_of_company
                              if website_of_company:
                                    instance.website_of_company = website_of_company
                              if location_of_company:
                                    instance.location_of_company = location_of_company
                              if business_field_of_company:
                                    instance.business_field_of_company = business_field_of_company
                              if name_of_company or email_of_company or hotline_of_company or website_of_company or location_of_company or business_field_of_company:
                                    instance.is_updated_basic_information_company = True
                              else:
                                    instance.is_updated_basic_information_company = False

                              instance.save()

                              return JsonResponse({
                                    'name_of_company': instance.name_of_company,
                                    'email_of_company': instance.email_of_company,
                                    'hotline_of_company': instance.hotline_of_company,
                                    'website_of_company': instance.website_of_company,
                                    'location_of_company': instance.location_of_company,
                                    'business_field_of_company': instance.business_field_of_company,
                              }, safe=False, content_type='application/json')
                        if form_name == 'form_change_profile_picture':
                              print(request.FILES)
                              img = request.FILES.get('profile_picture') if request.FILES.get('profile_picture') else None
                              if img:
                                    instance.profile_picture_company = img
                              instance.save()
                              return JsonResponse({ 'message': 'Uploaded'}, safe=False)
                        if form_name == 'form_summary_company':
                              summary_company = request.POST.get('summary_company') if request.POST.get('summary_company') else None
                              if summary_company:
                                    instance.summary_company = summary_company
                              instance.save()
                              return JsonResponse({
                                    'summary_company': instance.summary_company,
                              }, safe=False, content_type='application/json')

                  return JsonResponse({'message': 'Tài khoản người dụng không phù hợp.'})
            return JsonResponse({'message': 'Có lỗi phát sinh.'})

# Class-based Views Handle Company Listing
class CompanyListing(LoginRequiredMixin, View):
      def get(self, request):
            # Get username
            username = request.user
            # Check user's account
            try:
                  user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                  print('User\'s account does not exist')

            if user.is_job_seeker:
                  # Get the information of the user sending request
                  try:
                        sender_profile = ProfileModel.objects.get(user=username)
                  except ProfileModel.DoesNotExist:
                        print('User\'s profile does not exist')
                  # Get data of all recruiter profile
                  try:
                        list_recruiter_profile = list(RecruiterProfileModel.objects.all())
                  except ValueError:
                        print('Error')
                  
                  # Prepare data needed fo user
                  context = {
                        'list_of_companies': list_recruiter_profile,
                        'profile_picture_link': sender_profile.profile_picture.url,
                  }
                  return render(request, 'profiles/JobSeeker/company-listing-page.html', context)
