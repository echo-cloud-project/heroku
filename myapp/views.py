from django.shortcuts import render
import os

# index 페이지 뷰 함수
def index(request):
    return render(request, 'index.html')

# kcn 페이지 뷰 함수
def ksn(request):
    return render(request, 'ksn.html')

# kdy 페이지 뷰 함수
def kdy(request):
    return render(request, 'kdy.html')

# ksh 페이지 뷰 함수
def ksh(request):
    return render(request, 'ksh.html')

# pde 페이지 뷰 함수
def pde(request):
    return render(request, 'pde.html')
