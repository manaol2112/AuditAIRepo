from django.db import models
from django.contrib.auth.models import User, Group

# SAP S/4HANA AND ECC MODELS ARE STORED IN THIS GROUP

class SAP_USR02(models.Model):
    BNAME = models.CharField(max_length=50,blank=True,null=True) #USERID
    MANDT = models.CharField(max_length=50,blank=True,null=True) #CLIENTCODE
    USTYP = models.CharField(max_length=2,blank=True,null=True) #USER TYPE AS TO DIALOG, SYSTEM, OR COMM
    GLTGB = models.DateTimeField() #RECORD CREATION DATE AND TIME
    GLTGV = models.DateField() #LAST LOGON OF USER
    TRDAT = models.DateTimeField() #LAST SUCCESSFUL LOGIN
    LTIME = models.DateTimeField() #LAST UNSUCCESSFUL ATTEMPT
    UFLAG = models.CharField(max_length=10,blank=True,null=False) #USER STATUS (ACTIVE OR LOCKED)
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.BNAME
    
    class Meta:
        managed = True
        db_table = 'SAP_USR02'

class SAP_AGR_USERS(models.Model):
    UNAME = models.CharField(max_length=50,blank=True,null=True) #USERID
    MANDT = models.CharField(max_length=50,blank=True,null=True) #CLIENTCODE
    AGR_NAME = models.CharField(max_length=50,blank=True,null=True) #AUTHORIZATIONS ASSIGNED
    FROM_DAT = models.DateTimeField() #VALIDITY START DATE
    TO_DAT = models.DateTimeField() #VALIDITY END DATE
    
    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.MANDT
    
    class Meta:
        managed = True
        db_table = 'SAP_AGR_USERS'


class PASSWORDCONFIG(models.Model):
    MIN_LENGTH = models.CharField(max_length=100,blank=True,null=True)
    HISTORY = models.CharField(max_length=100,blank=True,null=True)
    AGE = models.CharField(max_length=100,blank=True,null=True)
    LOCKOUT = models.CharField(max_length=100,blank=True,null=True)
    LOCKOUT_DURATION = models.CharField(max_length=100,blank=True,null=True)
    COMPLEXITY_ENABLED =  models.BooleanField(blank=True,null=True)
    HAS_SPECIALCHAR =  models.BooleanField(blank=True,null=True)
    HAS_NUMERIC =  models.BooleanField(blank=True,null=True)
    HAS_UPPER =  models.BooleanField(blank=True,null=True)
    HAS_LOWER =  models.BooleanField(blank=True,null=True)
    MFA_ENABLED =  models.BooleanField(blank=True,null=True)
    SESSION_LENGTH = models.CharField(max_length=100,blank=True,null=True)

    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True, null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)


    class Meta:
        managed = True
        db_table = 'SYS_PWCONFIG'

#[PLACEHOLDER]ORACLE AND ORACLE FUSION ARE STORED IN THIS GROUP

#COMPANY
class COMPANY(models.Model):
    COMPANY_ID = models.CharField(max_length=100,blank=True,null=True)
    COMPANY_NAME = models.CharField(max_length=1000,blank=True,null=True)
    SELECTED = models.BooleanField(blank=True,null=True)

    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True, null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.COMPANY_NAME
    
    class Meta:
        managed = True
        db_table = 'COMPANY'

class MULTIPLE_COMPANY(models.Model):
    MULTIPLE = models.BooleanField(blank=True,null=True)

    def bool(self):
        return self.MULTIPLE
    
    class Meta:
        managed = True
        db_table = 'MULTIPLE_COMPANY'

# Create your models here.
class USERROLES(models.Model):
    COMPANY_ID = models.ManyToManyField(COMPANY,blank=True,null=True)
    USERNAME = models.ForeignKey(User,on_delete=models.CASCADE)

    #LOG
    CREATED_BY =  models.CharField(max_length=150,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True, null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY =  models.CharField(max_length=150,blank=True,null=True)

    def __str__(self):
      return str(self.USERNAME.username) if self.USERNAME else ''
    
    class Meta:
        managed = True
        db_table = 'USERROLES'
    
#HR SYSTEM MODELS ARE IN THIS GROUP

class HR_RECORD(models.Model):
    COMPANY_ID = models.CharField(max_length=1000,blank=True,null=True)
    USER_ID = models.CharField(max_length=50,blank=True,null=True)
    EMAIL_ADDRESS = models.CharField(max_length=50,blank=True,null=True)
    FIRST_NAME = models.CharField(max_length=50,blank=True,null=True)
    LAST_NAME = models.CharField(max_length=50,blank=True,null=True)
    JOB_TITLE = models.CharField(max_length=50,blank=True,null=True)
    DEPARTMENT = models.CharField(max_length=50,blank=True,null=True)
    MANAGER = models.CharField(max_length=50,blank=True,null=True)
    HIRE_DATE = models.DateField(null=True)
    EMP_TYPE =  models.CharField(max_length=10,blank=True,null=True)
    REHIRE_DATE = models.DateField(null=True)
    STATUS = models.CharField(max_length=50,blank=True,null=True)
    TERMINATION_DATE = models.DateField(null=True)
    
    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True, null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return f"{self.FIRST_NAME} {self.LAST_NAME}"
    
    class Meta:
        managed = True
        db_table = 'HR_RECORD'

class APP_USERS(models.Model):
    USER_ID = models.CharField(max_length=100,blank=True,null=True)
    FIRST_NAME = models.CharField(max_length=100,blank=True,null=True)
    LAST_NAME = models.CharField(max_length=100,blank=True,null=True)
    EMAIL_ADDRESS = models.CharField(max_length=100,blank=True,null=True)
    STATUS = models.CharField(max_length=100,blank=True,null=True)
    LOCKED = models.CharField(max_length=100,blank=True,null=True)


class APP_LIST(models.Model):
    #APPLICATION LIST
    COMPANY_ID = models.ForeignKey(COMPANY,on_delete=models.CASCADE,max_length=100,blank=True,null=True)
    APP_NAME = models.CharField(max_length=100,blank=True,null=True)
    APP_TYPE = models.CharField(max_length=100,blank=True,null=True)
    HOSTED = models.CharField(max_length=50,blank=True,null=True)
    RISKRATING = models.CharField(max_length=50,blank=True,null=True)
    RELEVANT_PROCESS = models.CharField(max_length=100,blank=True,null=True)
    DATE_IMPLEMENTED = models.CharField(max_length=100,blank=True,null=True)
    DATE_TERMINATED = models.DateField(null=True,blank=True)
    APPLICATION_OWNER = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True)
    AUTHENTICATION_TYPE = models.CharField(max_length=50,blank=True,null=True)

     #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.APP_NAME
    
    def get_owner_name(self):
        if self.APPLICATION_OWNER:
            return f"{self.APPLICATION_OWNER.first_name} {self.APPLICATION_OWNER.last_name}"
        else:
            return "No Owner"
    
    class Meta:
        managed = True
        db_table = 'APP_LIST'

class APP_RECORD(models.Model):
    #GENERAL USER INFORMATION
    APP_NAME = models.ForeignKey(APP_LIST,on_delete=models.CASCADE,max_length=100,blank=True,null=True)
    APP_TYPE = models.CharField(max_length=50,blank=True,null=True)
    USER_ID =  models.CharField(max_length=50,blank=True,null=True)
    EMAIL_ADDRESS = models.CharField(max_length=50,blank=True,null=True)
    FIRST_NAME = models.CharField(max_length=50,blank=True,null=True)
    LAST_NAME = models.CharField(max_length=50,blank=True,null=True)
    ROLE_NAME = models.CharField(max_length=100,blank=True,null=True)
    STATUS = models.CharField(max_length=50,blank=True,null=True)
    TYPE = models.CharField(max_length=50,blank=True,null=True) #USER_ACCOUNT, SYSTEM_ACCOUNT, OTHER
    OWNER_IF_SYSTEM = models.CharField(max_length=50,blank=True,null=True) 
    OWNER_IF_REGULAR = models.CharField(max_length=50,blank=True,null=True) 
    IS_ADMIN = models.CharField(max_length=50,blank=True,null=True)

    #PROVISIONING
    DATE_GRANTED = models.DateTimeField(null=True)
    DATE_APPROVED = models.DateTimeField(null=True)
    ACCESS_APPROVER_NAME1 = models.ForeignKey(HR_RECORD,on_delete=models.DO_NOTHING,max_length=100,blank=True,null=True, related_name='access_approver_name1')
    ACCESS_APPROVER_TITLE1 = models.ForeignKey(HR_RECORD,on_delete=models.DO_NOTHING,max_length=100,blank=True,null=True, related_name='access_approver_title1')
    ACCESS_APPROVER_NAME2 = models.ForeignKey(HR_RECORD,on_delete=models.DO_NOTHING,max_length=100,blank=True,null=True, related_name='access_approver_name2')
    ACCESS_APPROVER_TITLE2 = models.ForeignKey(HR_RECORD,on_delete=models.DO_NOTHING,max_length=100,blank=True,null=True,related_name='access_approver_title2')
    APPROVAL_TYPE = models.CharField(max_length=100,blank=True,null=True) #TICKET, EMAIL, OR OTHER
    APPROVAL_REFERENCE = models.CharField(max_length=100,blank=True,null=True)
    APPROVAL_SUPPORT = models.CharField(max_length=1000,blank=True,null=True)

    #TERMINATION
    DATE_REVOKED = models.DateTimeField(null=True)
    LAST_LOGIN = models.DateTimeField(null=True)
    HR_NOTIFICATION_DATE = models.DateTimeField(null=True)
    NOTIFICATION_TYPE = models.CharField(max_length=100,blank=True,null=True) #TICKET, EMAIL, OR OTHER
    NOTIFICATION_SUPPORT = models.CharField(max_length=100,blank=True,null=True) #LINK

    #USER ACCESS REVIEW
    DATE_LAST_CERTIFIED = models.DateTimeField(null=True)
    CERTIFIED_BY = models.CharField(max_length=50,blank=True,null=True)
    TAGGED_INAPPROPRITE = models.CharField(max_length=50,blank=True,null=True)
    DATE_TAGGED_INAPPROPRIATE = models.DateTimeField(null=True)

    #MAPPING TO HR
    MAPPED_TO_HR = models.CharField(max_length=50,blank=True,null=True)
    MAPPED_HR_FNAME = models.CharField(max_length=50,blank=True,null=True)
    MAPPED_HR_LNAME = models.CharField(max_length=50,blank=True,null=True)
    MAPPED_HR_EMAIL = models.CharField(max_length=50,blank=True,null=True)
    MAPPED_USING = models.CharField(max_length=100,blank=True,null=True)

    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return f"{self.APP_NAME} - {self.USER_ID}" 
    
    def approval_duration(self):
        if self.DATE_APPROVED and self.DATE_GRANTED:
            duration = self.DATE_APPROVED - self.DATE_GRANTED
            return duration.days
        return None
    
    class Meta:
        managed = True
        db_table = 'APP_RECORD'

class ADMIN_ROLES_FILTER(models.Model):
    APP_NAME = models.ForeignKey(APP_LIST,on_delete=models.CASCADE,max_length=100,blank=True,null=True)
    ROLE_NAME = models.ManyToManyField(APP_RECORD, related_name = 'roles_filter')

    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)


class SYSTEM_ACCOUNTS(models.Model):
    APP_NAME = models.ForeignKey(APP_LIST,on_delete=models.CASCADE,max_length=100,blank=True,null=True)
    USER_ID = models.ForeignKey(APP_RECORD,on_delete=models.CASCADE,max_length=100, blank=True,null=True)
    IS_SYSTEM_ACCOUNT = models.BooleanField(blank=True, null=True)

    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

class INTEGRATION_ACCOUNTS(models.Model):
    APP_NAME = models.ForeignKey(APP_LIST,on_delete=models.CASCADE,max_length=100,blank=True,null=True)
    USER_ID = models.ForeignKey(APP_RECORD,on_delete=models.CASCADE,max_length=100, blank=True,null=True)
    IS_INTEGRATION_ACCOUNT = models.BooleanField(blank=True, null=True)

    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

class APP_USER_UPLOAD(models.Model):
    file_name = models.FileField(upload_to='app_users/')
    APP_NAME = models.ForeignKey(APP_RECORD,on_delete=models.CASCADE,max_length=100,blank=True,null=True)
    activated = models.BooleanField(default=False)
    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return f"{self.file_name}"  
    
    class Meta:
        managed = True
        db_table = 'USER_UPLOAD_ATTACHMENTS'

class APP_NEW_USER_APPROVAL(models.Model):
    file_name = models.FileField(upload_to='new_users_approval/')
    USER_ID = models.ForeignKey(APP_RECORD,on_delete=models.CASCADE,max_length=100,blank=True,null=True)
    activated = models.BooleanField(default=False)
    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return f"{self.file_name}"  
    
    class Meta:
        managed = True
        db_table = 'NEW_USER_APPROVAL'
        
class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    upload_date = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"
    
class PWCONFIGATTACHMENTS(models.Model):
    APP_NAME = models.ForeignKey(APP_LIST,on_delete=models.CASCADE,null=True)
    file_name = models.FileField(upload_to='pwconfigs/',null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"
    

class CONTROLS(models.Model):
    COMPANY_ID = models.ForeignKey(COMPANY,on_delete=models.CASCADE)
    CONTROL_ID = models.CharField(max_length=50,blank=True,null=True)
    CONTROL_NAME = models.CharField(max_length=50,blank=True,null=True)
    CONTROL_DESCRIPTION = models.CharField(max_length=50,blank=True,null=True)
    APP_NAME = models.ManyToManyField(APP_RECORD)

    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
            return self.CONTROL_NAME
    
    class Meta:
        managed = True
        db_table = 'CONTROLS'
    
class POLICIES(models.Model):
    POLICY_NAME = models.CharField(max_length=50,blank=True,null=True)
    POLICY_DESCRIPTION = models.CharField(max_length=1000,blank=True,null=True)
    CONTROL_ID = models.ManyToManyField(CONTROLS)
    LAST_UPDATED = models.DateField(null=True)
  
    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
            return self.POLICY_NAME
    
    class Meta:
        managed = True
        db_table = 'POLICIES'


#MODELS FOR THE POLICIES ARE SAVED IN HERE

class PASSWORDPOLICY(models.Model):
    COMPANY_ID = models.ManyToManyField(COMPANY,blank=True,null=True)
    COMPLEXITY_ENABLED = models.BooleanField(default=False) 
    LENGTH = models.IntegerField(blank=True, null=True)
    UPPER = models.BooleanField(default=False) 
    LOWER = models.BooleanField(default=False) 
    NUMBER = models.BooleanField(default=False) 
    SPECIAL_CHAR = models.BooleanField(default=False)  
    AGE = models.IntegerField(blank=True, null=True)
    HISTORY = models.IntegerField(blank=True, null=True)
    LOCKOUT_ATTEMPT = models.IntegerField(blank=True, null=True)
    LOCKOUT_DURATION = models.CharField(max_length=50, blank=True, null=True)
    MFA_ENABLED = models.BooleanField(default=False) 
    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True) 

def __str__(self):
    return str(self.id)

class Meta:
        managed = True
        db_table = 'PASSWORDPOLICY'

class TERMINATIONPOLICY(models.Model):

    COMPANY_ID = models.ManyToManyField(COMPANY,blank=True,null=True)
    DAYS_TO_TERMINATE = models.IntegerField(blank=True, null= True)
     #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True) 

class Meta:
        managed = True
        db_table = 'TERMINATIONPOLICY'

    
class PASSWORD(models.Model):
    APP_NAME = models.ForeignKey(APP_LIST, on_delete=models.CASCADE, blank=True, null=True)
    CONTROL_ID = models.ForeignKey(CONTROLS, on_delete=models.CASCADE, blank=True, null=True)
    COMPLEXITY_ENABLED = models.BooleanField(default=False) 
    LENGTH = models.IntegerField(blank=True, null=True)
    UPPER = models.BooleanField(default=False) 
    LOWER = models.BooleanField(default=False) 
    NUMBER = models.BooleanField(default=False) 
    SPECIAL_CHAR = models.BooleanField(default=False)  
    AGE = models.IntegerField(blank=True, null=True)
    HISTORY = models.IntegerField(blank=True, null=True)
    LOCKOUT_ATTEMPT = models.IntegerField(blank=True, null=True)
    LOCKOUT_DURATION = models.CharField(max_length=50, blank=True, null=True)
    MFA_ENABLED = models.BooleanField(default=False)  
    #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

def __str__(self):
    return str(self.CONTROL_ID)

class Meta:
        managed = True
        db_table = 'PASSWORD'

class TERMINATION(models.Model):
    CONTROL_ID = models.ForeignKey(CONTROLS,on_delete=models.DO_NOTHING)
    REQUIRED_DAYS = models.IntegerField(null=True)

     #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
            return self.REQUIRED_DAYS
    
    class Meta:
        managed = True
        db_table = 'TERMINATION'
    
class PROVISIONING(models.Model):
    CONTROL_ID = models.ForeignKey(CONTROLS,on_delete=models.DO_NOTHING)
    REQUIRED_APPROVERS = models.CharField(max_length=50,blank=True,null=True)

     #LOG
    CREATED_BY = models.CharField(max_length=50,blank=True,null=True)
    CREATED_ON = models.DateField(auto_now_add=True,null=True,blank=True)
    LAST_MODIFIED = models.DateTimeField(null=True)
    MODIFIED_BY = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
            return self.REQUIRED_APPROVERS
    
    class Meta:
        managed = True
        db_table = 'PROVISIONING'


    
