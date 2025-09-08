from django.shortcuts import render, redirect
from django.views import View
from .models import Credit, Application, Client
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from users.models import User
from django.http.response import JsonResponse


class IndexView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'index.html')
    
class toKonveyer(LoginRequiredMixin,View):
    def get(self,request):
        applications = Application.objects.all()
        return render(request,'application.html',{"applications":applications})
    def post(self,request):
        app_id = request.POST.get('app_btn')
        application = Application.objects.get(id=app_id)
        credit = Credit(
            user=request.user,
            filial=request.user.filial,
            application = application
        )
        credit.save()
        credit.contract_id = f'F13-{credit.id}'
        credit.save()
        return redirect('konveyer',id=credit.id)
    
class KonveyerView(LoginRequiredMixin,View):
    def get(self,request,id):
        credit = Credit.objects.get(id=id)
        return render(request,'konveyer.html',{"credit_id":credit.id,"credit":credit})
    
class ArizalarView(LoginRequiredMixin,View):
    def get(self,request):
        credits = Credit.objects.filter(filial=request.user.filial).order_by('-created_at')
        return render(request,'arizalar.html',{"credits":credits})
    

@login_required
def get_user(request):
    if request.method == 'POST':
        pinfl = request.POST.get('pinfl')
        credit_id = request.POST.get('credit_id')
        print(f'\n\n{pinfl}\n\n')
        user = Client.objects.get(passport_pinfl=pinfl)
        credit = Credit.objects.get(id=credit_id)
        data = {
            # Client's data
            "first_name":user.first_name,
            "last_name":user.last_name,
            "middle_name":user.middle_name,
            "gender":user.gender,
            "education":user.education,
            "birth_date":str(user.birth_date),
            "client_country":user.client_country,
            "client_region":user.client_region,

            # Passport data
            "passport_type":user.passport_type,
            "passport_serial_letter":user.passport_serial_letter,
            "passport_serial_number":user.passport_serial_number,
            "passport_pinfl":user.passport_pinfl,
            "passport_got_date":user.passport_got_date,
            "passport_expiry_date":user.passport_expiry_date,
            "passport_got_region":user.passport_got_region,
            "passport_country":user.passport_country,

            # Address data from goverment database
            "base_country":user.base_country,
            "base_region":user.base_region,
            "base_city":user.base_city,
            "base_address":user.base_address,

            # Current address data
            "current_country":user.current_country,
            "current_region":user.current_region,
            "current_city":user.current_city,
            "current_address":user.current_address,

            # Other data
            "description":user.description,
            "filial":user.filial.name,
        }
        credit.client = user
        credit.save()
        return JsonResponse({"user":data})
    


@login_required
def give_credit(request,id):
    credit = Credit.objects.get(id=id)
    credit.status = 'done'
    credit.save()
    return redirect('home')

@login_required
def reject_credit(request,id):
    credit = Credit.objects.get(id=id)
    credit.status = 'rejected'
    credit.save()
    return redirect('home')
