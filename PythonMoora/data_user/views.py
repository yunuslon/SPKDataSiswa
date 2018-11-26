from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from library.view import ManagementAccessView
from data_user.forms import UserForm
from django.contrib.auth.models import  User,Group

class ListUserView(ManagementAccessView):
    def get(self, request):
        template = 'data_user/index.html'
        form = UserForm(request.POST or None)
        user = User.objects.all()
        data = {
        'form' : form,
		'user' : user,
        }
        return render(request, template, data)

class SaveDataUserView(ManagementAccessView):
    def post(self, request):
        user_form = UserForm(request.POST or None, request.FILES)

        if user_form.is_valid():
            user = User()
            user.username = UserForm.cleaned_data['username']
            user.password = UserForm.cleaned_data['password']
            superuser = request.POST.get('superuser', None)
            if not superuser == None:
                user.is_superuser = True
                user.save()

                group = Group.objects.get(name='Administrator')
                group.user_set.add(user)

            else:
                 user.save()

            return redirect('data_user:view')
        else:
            return HttpResponse(user_form.errors)