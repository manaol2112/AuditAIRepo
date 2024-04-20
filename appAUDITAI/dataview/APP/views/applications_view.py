from appAUDITAI.dataview.MISC.imports import *

# THIS CLASS HANDLES ALL THE ACTIONS TAKEN BY THE SYSTEM ADMINISTRATOR (USER ADDITION, TERMINATION, UPLOAD)

class AppListByCompany(ProcessOwnerPermissionMixin,View):
    template_name = 'pages/APP/processowner-company.html'

    def get(self, request):
        active_user = request.user
        user_roles = USERROLES.objects.filter(USERNAME=active_user)
        for user_role in user_roles:
            company_ids = user_role.COMPANY_ID.all()
            for company_id in company_ids:
                context = {
                    'company_ids':company_ids
                }
        return render(request, self.template_name, context)


class ApplistByProcessOwner(ProcessOwnerPermissionMixin, View):
    template_name = 'pages/APP/processowner-applist.html'

    def get(self, request,comp_id):
        context = self.common_data(request,comp_id)
        return render(request, self.template_name, context)

    def common_data(self, request, comp_id):
        user = request.user
        app = APP_LIST.objects.filter(APPLICATION_OWNER=user, COMPANY_ID=comp_id)
        process_owner_group_name = "Process Owner"
        app_owners = User.objects.filter(
            is_active=True, groups__name=process_owner_group_name)
        company_name = COMPANY.objects.get(id=comp_id)
        context = {
            'app_owners': app_owners,
            'app': app,
            'comp_id':comp_id,
            'company_name':company_name
        }
        return context

    def post(self, request, comp_id):

        app_name = request.POST.get('app_name')
        app_type = request.POST.get('app_type')
        hosting = request.POST.get('hosting')
        risk_rating = request.POST.get('risk_rating')
        relevant_process = request.POST.get('relevant_process')
        date_implemented = request.POST.get('date_implemented')
        app_list_app_owner1 = request.POST.get('app_list_app_owner1')
        auth_type = request.POST.get('auth_type')
        company = COMPANY.objects.filter(id = comp_id)
        app_owner = User.objects.get(id = app_list_app_owner1)

        new_app, created = APP_LIST.objects.get_or_create(APP_NAME=app_name, COMPANY_ID = company.first())
        new_app.COMPANY_ID = company.first()
        new_app.APP_NAME = app_name
        new_app.APP_TYPE = app_type
        new_app.HOSTED = hosting
        new_app.RISKRATING = risk_rating
        new_app.RELEVANT_PROCESS = relevant_process
        new_app.APPLICATION_OWNER = app_owner
        new_app.AUTHENTICATION_TYPE = auth_type
        new_app.DATE_IMPLEMENTED = date_implemented
        new_app.save()

        context = self.common_data(request, comp_id)
        return render(request, self.template_name, context)


class SetupNewAppView(ProcessOwnerPermissionMixin,View):
    template_name = 'pages/APP/processowner-setupnewapp.html'

    def get(self, request,comp_id,app_id):
        company_name = COMPANY.objects.get(id=comp_id)
        selected_app = APP_LIST.objects.get(id=app_id)

        # # hostname = '10.0.0.18'
        # # port = 22
        # # username = 'robertjohn'
        # # password = 'Robertjohn89'
        # # remote_dir = '/Users/robertjohn/Desktop/auditai-sftp'

        # # try:
        # #     # Establish SSH transport
        # #     transport = paramiko.Transport((hostname, port))
        # #     transport.connect(username=username, password=password)
            
        # #     # Establish SFTP session
        # #     sftp = paramiko.SFTPClient.from_transport(transport)
            
        # #     # List files in remote directory
        # #     file_list = sftp.listdir(remote_dir)
            
        # #     # Close the SFTP session and transport
        # #     sftp.close()
        # #     transport.close()
        # #     return JsonResponse({'files': file_list})
        
        # # except Exception as e:
        # #     return JsonResponse({'error': str(e)}, status=500)

        context = {
            'comp_id':comp_id,
            'app_id':app_id,
            'company_name':company_name,
            'selected_app':selected_app
        }
        return render(request, self.template_name, context)  # Pass request instead of self

class AppdetailsByProcessOwner(ProcessOwnerPermissionMixin, View):
    
    template_name = 'pages/APP/processowner-appdetails.html'

    def setup_new_app(self,request,comp_id,app_id):
       pass

    def common_data(self, request, comp_id, app_id):
        user = request.user
        app = APP_LIST.objects.filter(APPLICATION_OWNER=user)
        selected_app = APP_LIST.objects.get(id=app_id)
        password_exist = PASSWORD.objects.filter(APP_NAME=selected_app.id)
        attachment = PWCONFIGATTACHMENTS.objects.filter(
            APP_NAME=selected_app.id, activated=True).first()
        file_path_relative = attachment.file_name.url if attachment and attachment.file_name and attachment.file_name.url else '/media/pwconfigs/default.png'
        form = PWCONFIG_MODELFORM()
        user_upload_form = APP_USER_UPLOAD_FORM()
        app_users = APP_RECORD.objects.filter(APP_NAME=selected_app).values(
            'USER_ID', 'EMAIL_ADDRESS', 'STATUS').distinct().order_by('STATUS', 'EMAIL_ADDRESS')
        company_name = COMPANY.objects.get(id=comp_id)
        context = {
            'app': app,
            'app_users': app_users,
            'selected_app': selected_app,
            'form': form,
            'password_exist': password_exist,
            'file_path': file_path_relative,
            'user_upload_form': user_upload_form,
            'comp_id':comp_id,
            'company_name':company_name
        }
        return context

    def get(self, request, comp_id, app_id):
        selected_app = APP_LIST.objects.get(id=app_id)
        try:
            app_users = APP_RECORD.objects.filter(APP_NAME=selected_app).values(
                'USER_ID', 'EMAIL_ADDRESS', 'STATUS').distinct().order_by('STATUS', 'EMAIL_ADDRESS')
            if app_users.exists():  # Check if any app_users are found
                context = self.common_data(request, comp_id, app_id)
            else:
                context = self.common_data(request, comp_id, app_id)
                return redirect('appAUDITAI:setup-new-app',comp_id,app_id)
        except AttributeError as e:  # Handle the case when the selected_app doesn't exist
            print('Attribute Error',e)
        except ValueError as e:
            print('Value Error:',e)
 
        # If the code reaches here, render the template with no context
        return render(request, self.template_name, context)

        
    def post(self, request, comp_id, app_id):
        # Check if it's an AJAX request
        is_ajax_request = request.POST.get('is_ajax_request', None)
        if is_ajax_request == 'true':
            return self.pw_to_image(request, comp_id, app_id)
        else:
            form_id = request.POST.get('form_id')
            if form_id == 'pw_attachment_upload_form':
                return self.save_pwconfig(request, comp_id, app_id)
            elif form_id == 'app_user_upload_form':
                return self.upload_app_user(request, comp_id, app_id)

    def upload_app_user(self, request, comp_id, app_id):
        user = request.user
        form = APP_USER_UPLOAD_FORM(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['file_name'].name != 'AUDITAI_USER_UPLOAD_CSV.csv':
                return JsonResponse({'error': 'The attached file is invalid. Make sure to use the template provided to avoid receiving this error.'})
            else:
                form.save()
                form = APP_USER_UPLOAD_FORM()
                obj = APP_USER_UPLOAD.objects.get(activated=False)
                date_formats = ["%Y-%m-%d", "%d/%m/%Y",
                                "%m/%d/%Y", "%Y%m%d", "%m/%d/%y"]
                with open(obj.file_name.path, 'r') as f:
                    reader = csv.reader(f)
                    header = next(reader)
                    header = [field.strip('\ufeff') for field in header]
                    expected_fields = ['USER_ID', 'EMAIL_ADDRESS', 'FIRST_NAME', 'LAST_NAME',
                                       'ROLE_NAME', 'STATUS', 'DATE_GRANTED', 'DATE_REVOKED', 'LAST_LOGIN']
                    missing_fields = [
                        field for field in expected_fields if field not in header]
                    if missing_fields:
                        obj.delete()
                        return JsonResponse({'error': 'Missing field(s) in the attached template: {}'.format(', '.join(missing_fields))})
                    else:
                        for i, row in enumerate(reader):
                            DATE_GRANTED = row[6]
                            DATE_REVOKED = row[7]
                            LAST_LOGIN = row[8]
                            if not DATE_GRANTED:
                                # Assign a default date, e.g., January 1, 1990
                                DATE_GRANTED = datetime(1900, 1, 1)
                            else:
                                DATE_GRANTED = self.parse_date(
                                    str(DATE_GRANTED), date_formats)
                            if not DATE_REVOKED:
                                DATE_REVOKED = datetime(1900, 1, 1)
                            else:
                                DATE_REVOKED = self.parse_date(
                                    str(DATE_REVOKED), date_formats)
                            if not LAST_LOGIN:
                                LAST_LOGIN = datetime(1900, 1, 1)
                            else:
                                LAST_LOGIN = self.parse_date(
                                    str(LAST_LOGIN), date_formats)

                            app_name = request.POST['selected_app']
                            app_list_instance = APP_LIST.objects.get(
                                id=app_name)

                            user_record_data = {
                                'APP_NAME': app_list_instance,
                                'USER_ID': row[0],
                                'EMAIL_ADDRESS': row[1],
                                'FIRST_NAME': row[2],
                                'LAST_NAME': row[3],
                                'ROLE_NAME': row[4],
                                'STATUS': row[5],
                                'DATE_GRANTED': DATE_GRANTED,
                                'DATE_REVOKED': DATE_REVOKED,
                                'LAST_LOGIN': LAST_LOGIN,
                                'CREATED_BY': user.username,
                                'CREATED_ON': timezone.now()
                            }
                            user_record, created = APP_RECORD.objects.get_or_create(
                                APP_NAME=app_list_instance,
                                USER_ID=row[0],
                                EMAIL_ADDRESS=row[1],
                                ROLE_NAME=row[4],
                                defaults=user_record_data  # Data to update or create
                            )

                            # If the record already existed, update its fields
                            if not created:
                                for field, value in user_record_data.items():
                                    setattr(user_record, field, value)
                                user_record.MODIFIED_BY = user.username
                                user_record.LAST_MODIFIED = timezone.now()
                                user_record.save()
                        obj.activated = True
                        obj.save()

                        if obj.activated:
                            return HttpResponseRedirect(request.path_info)
                        else:
                            obj.delete()
        else:
            return JsonResponse({'error': 'Invalid form data'})

        context = self.common_data(request,  comp_id, app_id)
        return render(request, self.template_name, context)

    def parse_date(self, date_str, date_formats):
        for date_format in date_formats:
            try:
                return datetime.strptime(date_str, date_format)
            except ValueError:
                pass
        # If none of the formats match, return a default date
        return datetime(1900, 1, 1)

    def pw_to_image(self, request, comp_id, app_id):
        template_name = 'pages/APP/processowner-appdetails.html'
        form = PWCONFIG_MODELFORM(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file_name']
            try:
                img = Image.open(uploaded_file)
            except (OSError, ValueError):
                return HttpResponse("Invalid image file")
            try:
                text = pytesseract.image_to_string(img, lang='eng')

                # Define a regular expression for extracting numbers between "age" and "days"
                max_history = re.compile(
                    r'p(?:a{0,3})s(?:s{0,3})w(?:o{0,3})r(?:d{0,3})\sh(?:i{0,3})s(?:t{0,3})o(?:r{0,3})y\s*(\d+)', re.IGNORECASE)
                max_pw_age = re.compile(
                    r'.*?M(?:a{0,3})x(?:i{0,3})m(?:u{0,3})m(?:\s*|\s*)p(?:a{0,3})s(?:s{0,3})w(?:o{0,3})r(?:d{0,3})\s*a(?:g{0,3})e(?:\s*|\s*)(\d+)\s*d(?:a{0,3})y(?:s{0,3}).*?', re.IGNORECASE)
                min_pw_age = re.compile(
                    r'.*?M(?:i{0,3})n(?:i{0,3})m(?:u{0,3})m(?:\s*|\s*)p(?:a{0,3})s(?:s{0,3})w(?:o{0,3})r(?:d{0,3})\s*a(?:g{0,3})e(?:\s*|\s*)(\d+)\s*d(?:a{0,3})y(?:s{0,3}).*?', re.IGNORECASE)
                pw_length = re.compile(
                    r'.*?M(?:i{0,3})n(?:i{0,3})m(?:u{0,3})m(?:\s*|\s*)p(?:a{0,3})s(?:s{0,3})w(?:o{0,3})r(?:d{0,3})\s*l(?:e{0,3})n(?:g{0,3})t(?:h{0,3})\s*(\d+)\s*c(?:h{0,3})a{0,3}r(?:a{0,3})c(?:t{0,3})e{0,3}r{0,3}s{0,3}.*?', re.IGNORECASE)

                # Search for matches using the regular expression
                max_history_pw_match = max_history.search(text)
                max_age_match = max_pw_age.search(text)
                min_age_match = min_pw_age.search(text)
                min_pw_length_match = pw_length.search(text)

                # Assign the extracted number and matched text to variables
                max_history_pw = max_history_pw_match.group(
                    1) if max_history_pw_match else ''
                extract_max_pw_age = max_age_match.group(
                    1) if max_age_match else ''
                extract_min_pw_age = min_age_match.group(
                    1) if min_age_match else ''
                extract_pw_length = min_pw_length_match.group(
                    1) if min_pw_length_match else ''

                response_content = (
                    f"Password History: {max_history_pw}\n"
                    f"Maximum Password Age: {extract_max_pw_age}\n"
                    f"Minimum Password Age: {extract_min_pw_age}\n"
                    f"Minimum Password Length: {extract_pw_length}"
                )
                response = HttpResponse(
                    content=response_content, content_type='text/plain')
                return HttpResponse(response)
            except pytesseract.TesseractError as e:
                return HttpResponse(f"Tesseract Error: {e}")
        context = self.common_data(request, comp_id, app_id)
        return render(request, self.template_name, context)

    def save_pwconfig(self, request, comp_id, app_id):
        form = PWCONFIG_MODELFORM(request.POST, request.FILES)
        if form.is_valid():
            APP_NAME = APP_LIST.objects.get(id=app_id)
            selected_app, created = PASSWORD.objects.get_or_create(
                APP_NAME=APP_NAME)
            # ASSIGN THE VALUE TO THE PASSWORD CONFIGURATION FIELD
            selected_app.APP_NAME = APP_NAME    
            selected_app.COMPLEXITY_ENABLED = bool(
                request.POST.get('pass_complexity', False))
            selected_app.LENGTH = int(request.POST.get('pass_length', 0))
            selected_app.UPPER = 'upper_case' in request.POST
            selected_app.LOWER = 'lower_case' in request.POST
            selected_app.NUMBER = 'number' in request.POST
            selected_app.SPECIAL_CHAR = 'special_character' in request.POST
            selected_app.AGE = int(request.POST.get('pass_age', 0))
            selected_app.HISTORY = int(request.POST.get('pass_history', 0))
            selected_app.LOCKOUT_ATTEMPT = int(
                request.POST.get('pass_lockout', 0))
            selected_app.LOCKOUT_DURATION = request.POST.get(
                'pass_lockout_duration', '')
            selected_app.MFA_ENABLED = bool(
                request.POST.get('multifactor_enabled', False))
            selected_app.save()  # Save the changes to the existing record
            existing_attachment = PWCONFIGATTACHMENTS.objects.filter(
                APP_NAME=APP_NAME).first()
            file_name = form.cleaned_data['file_name']
            # UPDATE OR UPLOAD THE ATTACHMENT
            if existing_attachment:
                # Update the existing attachment
                if file_name:
                    existing_attachment.file_name.delete()
                    existing_attachment.file_name = file_name
                    existing_attachment.attachment_file = form.cleaned_data['file_name']
                    existing_attachment.activated = True
                    existing_attachment.save()
            else:
                # Create a new attachment
                new_attachment = PWCONFIGATTACHMENTS(
                    APP_NAME=APP_NAME, file_name=file_name)
                new_attachment.save()
                new_attachment.activated = True
                new_attachment.save()

        context = self.common_data(request, comp_id, app_id,)
        return render(request, self.template_name, context)


class AppUserRecordView(ProcessOwnerPermissionMixin,View):
    template_name = "pages/APP/processowner-userrecord.html"

    def get(self, request, comp_id, app_id, username):
        selected_user = APP_RECORD.objects.filter(
            APP_NAME=app_id, USER_ID=username).first()
        mapped_user = HR_RECORD.objects.filter(
            Q(EMAIL_ADDRESS=selected_user.EMAIL_ADDRESS) |
            Q(USER_ID=selected_user.USER_ID) |
            (Q(FIRST_NAME=selected_user.FIRST_NAME)
             & Q(LAST_NAME=selected_user.LAST_NAME))
        )
        context = {
            'comp_id':comp_id, 
            'selected_user': selected_user,
            'app_id': app_id,
            'mapped_user': mapped_user
        }
        return render(request, self.template_name, context)


class AppNewUserListView(ProcessOwnerPermissionMixin,View):
    template_name = "pages/APP/processowner-appnewuserlist.html"

    def get(self, request, comp_id, app_id):
        current_date = timezone.now()
        current_year = current_date.year
        new_users = APP_RECORD.objects.filter(DATE_GRANTED__year=current_year, APP_NAME=app_id).order_by(
            'STATUS', 'DATE_GRANTED', 'EMAIL_ADDRESS')
        unique_statuses = set(user.STATUS for user in new_users)
        new_user_approval_form = NEW_USER_APPROVAL_FORM()
        selected_app = APP_LIST.objects.get(id = app_id)
        company_name = COMPANY.objects.get(id=comp_id)
        context = {
            'selected_app':selected_app,
            'new_users': new_users,
            'new_user_approval_form': new_user_approval_form,
            'app_id': app_id,
            'unique_statuses': unique_statuses,
            'comp_id':comp_id,
            'company_name':company_name
        }
        return render(request, self.template_name, context)


class AppNewUserApprovalView(ProcessOwnerPermissionMixin,View):
    template_name = 'pages/APP/processowner-appnewuserapproval.html'

    def common_data(self, request, comp_id, app_id, user_id):
        new_user_approval_form = NEW_USER_APPROVAL_FORM()
        selected_user = APP_RECORD.objects.get(id=user_id)
        existing_attachment_orig = APP_NEW_USER_APPROVAL.objects.filter(
            USER_ID=user_id).first()
        existing_attachment = basename(
            existing_attachment_orig.file_name.name) if existing_attachment_orig else None
        active_hr_users = HR_RECORD.objects.filter(STATUS__iexact='ACTIVE')
        if existing_attachment_orig:
            context = {
                'new_user_approval_form': new_user_approval_form,
                'active_hr_users': active_hr_users,
                'app_id': app_id,
                'selected_user': selected_user,
                'comp_id':comp_id,
                'existing_attachment': existing_attachment}
        else:
            context = {
                'new_user_approval_form': new_user_approval_form,
                'active_hr_users': active_hr_users,
                'app_id': app_id,
                'comp_id':comp_id,
                'selected_user': selected_user,
            }
        return context

    def get(self, request, comp_id, app_id, user_id):
        context = self.common_data(request, comp_id, app_id, user_id)
        return render(request, self.template_name, context)

    def new_user_add_attachment(self, request, comp_id, app_id, user_id):
        form = NEW_USER_APPROVAL_FORM(request.POST, request.FILES)
        if form.is_valid():
            approver1 = get_object_or_404(
                HR_RECORD, id=request.POST.get('approver1_id'))
            approver2 = get_object_or_404(
                HR_RECORD, id=request.POST.get('approver2_id'))

            date_formats = ["%Y-%m-%d", "%d/%m/%Y",
                            "%m/%d/%Y", "%Y%m%d", "%m/%d/%y"]
            date_approved = request.POST.get('date_approved')
            date_approved = timezone.make_aware(
                self.parse_date(str(date_approved), date_formats))

            selected_user, created = APP_RECORD.objects.get_or_create(
                id=user_id)
            selected_user.DATE_APPROVED = date_approved
            selected_user.ACCESS_APPROVER_NAME1 = approver1
            selected_user.ACCESS_APPROVER_NAME2 = approver2
            selected_user.APPROVAL_TYPE = request.POST.get('approval_type')
            selected_user.APPROVAL_REFERENCE = request.POST.get('approval_ref')
            selected_user.save()

            user_to_be_uploaded = APP_RECORD.objects.get(id=user_id)
            file_name = form.cleaned_data['file_name']
            if file_name:
                attach_to_user, created = APP_NEW_USER_APPROVAL.objects.get_or_create(
                    USER_ID=user_to_be_uploaded)  # Save the changes to the existing record
                attach_to_user.file_name.delete()
                attach_to_user.file_name = file_name
                attach_to_user.save()

        # RELOAD THE PAGE
        context = self.common_data(request, comp_id, app_id, user_id)
        return render(request, self.template_name, context)

    def delete_new_user_approval(self, request, comp_id, app_id, user_id):
        attachment = APP_NEW_USER_APPROVAL.objects.get(USER_ID=user_id)
        attachment.file_name.delete()
        attachment.save()
        context = self.common_data(request, comp_id, app_id, user_id)
        return render(request, self.template_name, context)

    def post(self, request, comp_id, app_id, user_id):
        form_id = request.POST.get('form_id')
        if form_id == 'new_user_add_approval':
            return self.new_user_add_attachment(request,comp_id,app_id, user_id)
        elif form_id == 'delete_new_user_attachment':
            return self.delete_new_user_approval(request, comp_id,app_id, user_id)

    def parse_date(self, date_str, date_formats):
        for date_format in date_formats:
            try:
                return datetime.strptime(date_str, date_format)
            except ValueError:
                pass
        # If none of the formats match, return a default date
        return datetime(1900, 1, 1)


class AppNewUserGetJobApprovalView(ProcessOwnerPermissionMixin,View):
    def get(self, request, id):
        user = get_object_or_404(HR_RECORD, id=id)
        job_title = user.JOB_TITLE
        context = {
            'job_title': job_title
        }
        return JsonResponse(context)

class AppTerminationListView(ProcessOwnerPermissionMixin,View):
    template_name = "pages/APP/processowner-appterminationlist.html"

    def get(self, request,comp_id,app_id):
        current_date = timezone.now()
        current_year = current_date.year
        termed_users = APP_RECORD.objects.filter(
            DATE_REVOKED__year=current_year, APP_NAME=app_id).order_by('DATE_REVOKED')
        selected_app = APP_LIST.objects.get(id = app_id)
        company_name = COMPANY.objects.get(id=comp_id)
        context = {
            'selected_app':selected_app,
            'comp_id':comp_id,
            'termed_users': termed_users,
            'app_id': app_id,
            'company_name':company_name
        }
        return render(request, self.template_name, context)
    
class AdminAccountListView(ProcessOwnerPermissionMixin,View):
    template_name = "pages/APP/processowner-adminaccounts.html"

    def common_data(self, request,comp_id,app_id):
        admin_roles = ADMIN_ROLES_FILTER.objects.filter(ROLE_NAME__isnull = False)
        active_roles = APP_RECORD.objects.filter(APP_NAME = app_id, ROLE_NAME__isnull = False).values('ROLE_NAME').distinct()
        admin_accounts = APP_RECORD.objects.filter(APP_NAME=app_id, roles_filter__in=admin_roles, STATUS__iexact = 'Active').order_by('USER_ID')
        unique_admin_accounts = ADMIN_ROLES_FILTER.objects.filter(APP_NAME=app_id).values('ROLE_NAME').distinct()
        selected_app = APP_LIST.objects.get(id = app_id)
        company_name = COMPANY.objects.get(id=comp_id)
        context = {
            'active_roles':active_roles,
            'unique_admin_accounts':unique_admin_accounts,
            'selected_app':selected_app,
            'comp_id':comp_id,
            'admin_accounts': admin_accounts,
            'app_id': app_id,
            'company_name':company_name
        }
        return context

    def get(self, request,comp_id,app_id):
        context = self.common_data(request, comp_id, app_id)
        return render(request, self.template_name, context)
 
    def post(self,request,comp_id,app_id):
        selected_roles = request.POST.getlist('role_list')
        app_names = APP_RECORD.objects.filter(APP_NAME=app_id).first()
        app_instance = APP_LIST.objects.filter(APP_NAME = app_names.APP_NAME).first()
        roles = APP_RECORD.objects.filter(APP_NAME = app_id, ROLE_NAME__in=selected_roles, ROLE_NAME__isnull = False)

        admin_roles, created = ADMIN_ROLES_FILTER.objects.get_or_create(
                APP_NAME=app_instance)
        admin_roles.APP_NAME = app_instance
        admin_roles.ROLE_NAME.set(roles)
        admin_roles.save()

        context = self.common_data(request, comp_id, app_id)
        return render(request, self.template_name, context)
    
class GenericAccountListView(ProcessOwnerPermissionMixin,View):
    template_name = "pages/APP/processowner-appgenericaccounts.html"

    def common_data(self, request,comp_id,app_id):
        app_name = APP_LIST.objects.filter(id = app_id).first()
        generic_accounts = generic_account = APP_RECORD.objects.filter(
        Q(TYPE='system_account') | Q(TYPE='integration_account'),
        Q(STATUS__iexact='ACTIVE'),APP_NAME = app_name).order_by('EMAIL_ADDRESS', 'TYPE')
        print(generic_account)
        company_name = COMPANY.objects.get(id=comp_id)
        selected_app = APP_LIST.objects.get(id = app_id)
        context = {
            'generic_accounts':generic_accounts,
            'comp_id':comp_id,
            'app_id': app_id,
            'company_name':company_name,
            'selected_app':selected_app,
        }
        return context

    def get(self, request,comp_id,app_id):
        context = self.common_data(request, comp_id, app_id)
        return render(request, self.template_name, context)
        
class AppHRMappingListView(View):
    template_name = "pages/APP/processowner-apphrmapping.html"

    def get(self, request, comp_id, app_id):
        app_users = APP_RECORD.objects.filter(APP_NAME=app_id)
        selected_app = APP_LIST.objects.get(id = app_id)
        company_name = COMPANY.objects.get(id=comp_id)
        mapped_users = HR_RECORD.objects.filter(
            Q(EMAIL_ADDRESS__in=app_users.values_list('EMAIL_ADDRESS', flat=True)) |
            Q(USER_ID__in=app_users.values_list('USER_ID', flat=True)) |
            (Q(FIRST_NAME__in=app_users.values_list('FIRST_NAME', flat=True)) &
             Q(LAST_NAME__in=app_users.values_list('LAST_NAME', flat=True)))
        )
        unmapped_users = app_users.exclude(
            Q(EMAIL_ADDRESS__in=mapped_users.values_list('EMAIL_ADDRESS', flat=True)) |
            Q(USER_ID__in=mapped_users.values_list('USER_ID', flat=True)) |
            Q(TYPE__isnull = False)
        )
        context = {
            'selected_app':selected_app,
            'mapped_users': mapped_users,
            'unmapped_users': unmapped_users,
            'comp_id':comp_id,
            'app_id': app_id,
            'company_name':company_name
        }
        return render(request, self.template_name, context)


# THIS IS THE CLASS FOR PASSWORD SECTION
class DeletePWAttachment(View):
    template_name: template_name = 'pages/APP/processowner-appdetails.html'

    def get_attachment(self, id):
        selected_app = get_object_or_404(APP_RECORD, id=id)
        attachment = PWCONFIGATTACHMENTS.objects.filter(
            APP_NAME=selected_app.id, activated=True).first()
        return selected_app, attachment

    def post(self, request, id):
        selected_app, attachment = self.get_attachment(id)
        if attachment:
            attachment.delete()
            attachment.file_name.delete()
            response_data = {'message': 'Attachment deleted successfully'}
            return JsonResponse(response_data)
        else:
            # Assuming you want to send an error message if the attachment is not found
            response_data = {'error': 'Attachment not found'}
            return JsonResponse(response_data, status=404)


class ApplicationList(View):

    template_name = 'pages/APP/app-list.html'

    def get(self, request, user_id=0, *args, **kwargs):
        # Load all employees
        app = APP_LIST.objects.filter(APP_NAME__isnull=False)
        active_users = User.objects.filter(is_active=True)
        context = {'app': app,
                   'active_users': active_users}
        return render(request, self.template_name, context)

    def post(self, request, app_id=0):
        if app_id == 0:
            form = NewAPP(request.POST)
            app_ower = User.objects.get(username=request.POST['app_owner'])
            if form.is_valid():
                app = form.save(commit=False)
                app.APP_NAME = request.POST['app_name']
                app.APP_TYPE = request.POST['app_type']
                app.HOSTED = request.POST['hosting']
                app.RISKRATING = request.POST['risk_rating']
                app.RELEVANT_PROCESS = request.POST['relevant_process']
                app.DATE_IMPLEMENTED = request.POST['date_implemented']
                app.APPLICATION_OWNER = app_ower
                # Logging
                app.CREATED_BY = 'manaol2112'
                app.CREATED_ON = timezone.now()
                app.save()

                app = APP_LIST.objects.filter(APP_NAME__isnull=False)
                context = {'app': app}
                return render(request, self.template_name, context)


class FetchMappedUser(View):
    model = HR_RECORD
    template_name = 'pages/APP/app-details.html'
    form_class = MappedUser

    def get(self, request, id, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            try:
                mapped_user = HR_RECORD.objects.get(EMAIL_ADDRESS=id)
                hr_mapping = self.form_class(instance=mapped_user)
                context = {
                    'hr_mapping': model_to_dict(hr_mapping.instance),
                    'form_html': hr_mapping.as_table(),
                }
                return JsonResponse(context)
            except ObjectDoesNotExist:
                error_message = "Employee not found"
                return JsonResponse({"error": error_message}, status=404)


class FetchAPPDetails(View):
    model = APP_LIST
    template_name = 'pages/APP/app-details.html'

    def get(self, request, app_name, *args, **kwargs):
        # POPULATE THE CV FORM
        form = CSVModelForm()
        # OBTAIN THE LIST OF APPS BASED ON SELECTED VALUE
        selected_app = APP_LIST.objects.get(APP_NAME=app_name)
        # OBTAIN THE LIST OF USERS BASED ON APP
        app_users = APP_RECORD.objects.filter(APP_NAME=selected_app)
        # MATCHING USERS FROM HR RECORD
        matching_users = HR_RECORD.objects.filter(
            # Match based on USER_ID, EMAIL_ADDRESS, or a combination of FIRST_NAME and LAST_NAME
            Q(USER_ID__in=app_users.values_list('USER_ID', flat=True)) |
            Q(EMAIL_ADDRESS__in=app_users.values_list('EMAIL_ADDRESS', flat=True)) |
            (Q(FIRST_NAME__in=app_users.values_list('FIRST_NAME', flat=True)) &
             Q(LAST_NAME__in=app_users.values_list('LAST_NAME', flat=True)))
        )
        # USERS FROM APP_RECORD THAT MATCH HR_RECORD
        matched_app_users = app_users.filter(
            Q(USER_ID__in=matching_users.values_list('USER_ID', flat=True)) |
            Q(EMAIL_ADDRESS__in=matching_users.values_list(
                'EMAIL_ADDRESS', flat=True))
            # |(Q(FIRST_NAME__in=matching_users.values_list('FIRST_NAME', flat=True)) &
            # Q(LAST_NAME__in=matching_users.values_list('LAST_NAME', flat=True)))
        )

        # USERS FROM APP_RECORD THAT DO NOT MATCH HR_RECORD
        unmatched_app_users = app_users.exclude(
            Q(USER_ID__in=matching_users.values_list('USER_ID', flat=True)) |
            Q(EMAIL_ADDRESS__in=matching_users.values_list('EMAIL_ADDRESS', flat=True)) |
            Q(TYPE__isnull=False)  # Filtering for null TYPE
            # |(Q(FIRST_NAME__in=matching_users.values_list('FIRST_NAME', flat=True)) &
            # Q(LAST_NAME__in=matching_users.values_list('LAST_NAME', flat=True)))
        )

        context = {'selected_app': selected_app,
                   'form': form,
                   'app_users': app_users,
                   'matched_app_users': matched_app_users,
                   'unmatched_app_users': unmatched_app_users}
        return render(request, self.template_name, context)


class TagUserType(View):

    def get(self, request, id):
        model = APP_RECORD
        template_name = 'pages/APP/app-details.html'
        unmapped_user = model.objects.get(id=id)
        context = {
            'unmapped_user': model_to_dict(unmapped_user.instance),
            'form_html': unmapped_user.as_table(),
        }
        return JsonResponse(context)

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            try:
                data = json.loads(request.body.decode('utf-8'))
                ids = data.get('checkedRecords', [])
                selected_type = data.get('selected_type')
                for id in ids:
                    unmapped_user = APP_RECORD.objects.get(id=id)
                    unmapped_user.TYPE = selected_type
                    unmapped_user.save()
                return JsonResponse({'message': 'User types updated successfully.'})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
