from django.contrib import admin

from .models import HR_RECORD, APP_RECORD, CSV,SAP_USR02,APP_LIST, POLICIES, CONTROLS, COMPANY, MULTIPLE_COMPANY, USERROLES,PASSWORD,PWCONFIGATTACHMENTS
from .models import PASSWORDPOLICY,TERMINATIONPOLICY,APP_USER_UPLOAD, APP_NEW_USER_APPROVAL, ADMIN_ROLES_FILTER,PASSWORDCONFIG
# Register your models here.
admin.site.register(HR_RECORD)
admin.site.register(APP_RECORD)
admin.site.register(CSV)
admin.site.register(SAP_USR02)
admin.site.register(APP_LIST)
admin.site.register(POLICIES)
admin.site.register(CONTROLS)
admin.site.register(COMPANY)
admin.site.register(MULTIPLE_COMPANY)
admin.site.register(USERROLES)
admin.site.register(PASSWORD)
admin.site.register(PWCONFIGATTACHMENTS)
admin.site.register(PASSWORDPOLICY)
admin.site.register(TERMINATIONPOLICY)
admin.site.register(APP_USER_UPLOAD)
admin.site.register(APP_NEW_USER_APPROVAL)
admin.site.register(ADMIN_ROLES_FILTER)
admin.site.register(PASSWORDCONFIG)