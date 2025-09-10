from django.shortcuts import render, redirect
from django.views import View
from .models import Credit, Application, Client, PhoneNumber
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
            application = application,
            rate = application.rate
        )
        credit.save()
        credit.contract_id = f'F13-{credit.id}'
        credit.save()
        return redirect('konveyer',id=credit.id)
    
class KonveyerView(LoginRequiredMixin,View):
    def get(self,request,id):
        credit = Credit.objects.get(id=id)
        try:
            numbers = PhoneNumber.objects.filter(client_id=credit.client.id).order_by("id")
            return render(request,'konveyer.html',{"credit_id":credit.id,"credit":credit,"numbers":numbers})
        except AttributeError:
            return render(request,'konveyer.html',{"credit_id":credit.id,"credit":credit})
    
class ArizalarView(LoginRequiredMixin,View):
    def get(self,request):
        credits = Credit.objects.filter(filial=request.user.filial).order_by('-created_at')
        return render(request,'arizalar.html',{"credits":credits})
    

@login_required
def get_user(request):
    if request.method == 'POST':
        credit_id = request.POST.get('credit_id')
        credit = Credit.objects.get(id=credit_id)
        try:
            pinfl = request.POST.get('pinfl')
            client = Client.objects.get(passport_pinfl=pinfl)
            credit.client = client
            credit.save()
            return JsonResponse({"status":True})
        except Client.DoesNotExist:
            credit.client = None
            credit.save()
            return JsonResponse({"status":False})
    

@login_required
def save_number(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        client = request.POST.get('client')
        name = request.POST.get('name')
        client_obj = Client.objects.get(id=client)
        if (number and client):
            num = PhoneNumber(
                number = number,
                name = name,
                client = client_obj
            )
            num.save()
            numbers = PhoneNumber.objects.filter(client_id=client_obj.id).order_by("id")
            nums = {}
            for i in numbers:
                nums[i.name] = i.number
            return JsonResponse({"status":True,"numbers":nums})
        return JsonResponse({"status":False})


@login_required
def give_credit(request,id):
    credit = Credit.objects.get(id=id)
    if credit.status != 'rejected' and credit.status != 'paid':
        credit.status = 'done'
        credit.save()
        return redirect('home')
    else:
        return redirect('arizalar')

@login_required
def reject_credit(request,id):
    credit = Credit.objects.get(id=id)
    if credit.status != 'done' and credit.status != 'paid':
        credit.status = 'rejected'
        credit.save()
        return redirect('home')
    else:
        return redirect('arizalar')
