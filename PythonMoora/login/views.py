from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from orm.models import TesOlimpiade,Siswa
import pandas as pd
import requests
from login.forms import AuthenticateForm

from django.conf import settings
from login.forms import AuthenticateForm
from library import authcheck
from orm.models import Siswa,Kelas,Karakter,Plomba,NilaiAkademik,HasilTes


class LoginView(View):
    def get(self, request):
        template = 'login/login.html'
        form = AuthenticateForm(request.POST or None)
        data  = {
            'form': form,
        }
        return render(request, template, data)


class DoLoginView(View):
    def post(self, request):
        template = 'login/login.html'
        form = AuthenticateForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']

            # ngecek user ada apa nggak
            user = authenticate(username=username, password=password) 
            
            if user is not None:
                # checkbox remember 
                print(user.is_staff)
                
                if not remember:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                    request.session.set_expiry(0)
                else:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                if authcheck.AuthCheck.isSuperUser(user):
                    login(request, user)
                    return redirect('data_siswa:view') 
                elif authcheck.AuthCheck.isSoalBio(user):
                    login(request, user)
                    return redirect('soalbiologi:view') 
                elif authcheck.AuthCheck.isSoalFis(user):
                    login(request, user)
                    return redirect('soalfisika:view') 
                elif authcheck.AuthCheck.isSoalKim(user):
                    login(request, user)
                    return redirect('soalkimia:view') 
                elif authcheck.AuthCheck.isSoalMat(user):
                    login(request, user)
                    return redirect('soalmatematika:view') 
                elif authcheck.AuthCheck.isGuru(user):
                    login(request, user)
                    return redirect('guru:view') 

                else:
                     messages.add_message(request, messages.WARNING,
                                 'Akun Belum Terdaftar Sebagai User !!')
            else:
                  messages.add_message(request, messages.WARNING,
                                 'Username dan atau Password tidak ditemukan !!')

        data  = {
            'form': form,
        }
        return redirect('login:view')
        return render(request, template, data)
        


class DoLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login:view')
