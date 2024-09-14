from django.contrib import admin
from django.urls import path
from ots1.views import*

app_name='ots1'
urlpatterns=[
    path('',welcome),
    path('new-candidate',candidateRegistrationForm,name='registration' ),
    path('store-candidate',candidateRegistration,name='savecandidate'),
    path('login',loginView,name='login'),
    path('home',candidateHome,name='home'),
    path('test',starttest,name='test'),
    path('calculate-result',calculateTestResult,name='calculateTest'),
    path('testhistory',testResultHistory,name='testHistory'),
    path('result',showTestResult,name='result'),
    path('logout',logoutViews,name='logout'),
]