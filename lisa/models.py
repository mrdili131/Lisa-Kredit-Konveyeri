from django.db import models
from users.models import User, Filial
from django.core.validators import MinValueValidator, MaxValueValidator
gender = [
    ('male','Erkak'),
    ('female','Ayol')
]

id = [
    ("id","ID passport"),
    ("old_pass","Eski turdagi passport"),
    ("drivers_license","Haydovchilik guvohnomasi")
]

education = [
    ("1","Oliy"),
    ("2","O‘rta"),
    ("3","O‘rta-maxsus"),
    ("4","Tuganlanmagan oliy"),
    ("5","Boshlang‘ich"),
]

status = [
    ('done','berildi'),
    ('rejected',"rad etildi"),
    ('pending','jarayonda')
]

class Client(models.Model):
    # Client's data
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    middle_name = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(choices=gender,default='male',max_length=50)
    education = models.CharField(choices=education,default="2",max_length=50)
    birth_date = models.DateField(null=True,blank=True)
    client_country = models.CharField(max_length=50,null=True,blank=True)
    client_region = models.CharField(max_length=50,null=True,blank=True)

    # Passport data
    passport_type = models.CharField(choices=id,default="id",max_length=50,null=True,blank=True)
    passport_serial_letter = models.CharField(max_length=5,null=True,blank=True)
    passport_serial_number = models.CharField(max_length=10,null=True,blank=True)
    passport_pinfl = models.CharField(max_length=50,unique=True,null=True,blank=True)
    passport_got_date = models.DateField(null=True,blank=True)
    passport_expiry_date = models.DateField(null=True,blank=True)
    passport_got_region = models.CharField(max_length=100,null=True,blank=True)
    passport_country = models.CharField(max_length=50,null=True,blank=True)

    # Address data from goverment database
    base_country = models.CharField(max_length=50,null=True,blank=True)
    base_region = models.CharField(max_length=50,null=True,blank=True)
    base_city = models.CharField(max_length=50,null=True,blank=True)
    base_address = models.CharField(max_length=150,null=True,blank=True)

    # Current address data
    current_country = models.CharField(max_length=50,null=True,blank=True)
    current_region = models.CharField(max_length=50,null=True,blank=True)
    current_city = models.CharField(max_length=50,null=True,blank=True)
    current_address = models.CharField(max_length=150,null=True,blank=True)

    # Other data
    description = models.TextField(null=True,blank=True)
    filial = models.ForeignKey(Filial,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        if self.first_name:
            return self.first_name
        else:
            return "No name"


class Application(models.Model):
    name = models.CharField(max_length=100)
    limit_amount = models.DecimalField(max_digits=10,decimal_places=0)
    rate = models.IntegerField()
    max_month = models.IntegerField()
    fine = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Credit(models.Model):
    # Linkings
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True,blank=True)
    contract_id = models.CharField(max_length=50,null=True,blank=True)

    # Credit essentials
    application = models.ForeignKey(Application,on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    pay_day = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(31)],null=True,blank=True)

    # Dates
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True,blank=True)

    # Other data
    description =  models.TextField(null=True,blank=True)
    status = models.CharField(choices=status,default="pending",max_length=50)
    filial = models.ForeignKey(Filial,on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.contract_id:
            return self.contract_id
        

class PhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f'{self.name} {self.number}'
