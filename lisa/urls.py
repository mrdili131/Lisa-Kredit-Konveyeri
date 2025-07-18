from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('to-konveyer/',views.toKonveyer.as_view(),name='to_konveyer'),
    path('konveyer/<int:id>/',views.KonveyerView.as_view(),name='konveyer'),
    path('arizalar/',views.ArizalarView.as_view(),name='arizalar'),
    path('get_user/',views.get_user,name='get_user'),
    path('give_credit/<int:id>/',views.give_credit,name='give_credit'),
    path('reject_credit/<int:id>/',views.reject_credit,name='reject_credit')

]