from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from library.view import ManagementAccessView
from data_user.forms import UserForm
from orm.models import Guru
from django.contrib.auth.models import  User,Group,Permission

class ListUserView(ManagementAccessView):
    def get(self, request):
        template = 'data_user/index.html'
        form = UserForm(request.POST or None)
        # user = User.objects.filter(permisson='Administrator')

        group = Group.objects.get(name='Administrator')
        users = group.user_set.all()
        data = {
        'form' : form,
		'user' : users,
        }
        return render(request, template, data)

class SaveDataUserView(ManagementAccessView):
    def post(self, request):
        user_form = UserForm(request.POST or None, request.FILES)

        if user_form.is_valid():
            user = User()
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.last_name = request.POST['last_name']
            superuser = request.POST.get('superuser', None)
            if not superuser == None:
                user.is_superuser = True
                user.is_staff = True
                user.save()

                group = Group.objects.get(name='Administrator')
                group.user_set.add(user)

            else:
                 user.save()

            return redirect('data_user:view')
        else:
            return HttpResponse(user_form.errors)

class HapusDataUserView(ManagementAccessView):
    
    def get(self, request, id):
        user = User.objects.filter(id=id)
        if user.exists():
            user.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('data_user:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 

class EditDataUserView(ManagementAccessView):
    template = 'data_user/edit.html'

    def get(self, request, id):
        user = User.objects.filter(id=id)
        if not user.exists():
            return redirect('data_user:view')
        user = user.first()
        initial = {

            'id': user.id,
            'username': user.username,
            'last_name': user.last_name,
            'password': user.password,
        }

        form = UserForm(initial=initial)
        user = User.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'user' : user,
        }
        return render(request, self.template, data)


class UpdateDataUserView(ManagementAccessView):

    def post(self, request):
        
        template = "data_user/index.html"
        form = UserForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            user = User.objects.get(pk=id)
            user.username = form.cleaned_data['username']
            user.last_name = form.cleaned_data['last_name']
            user.password = form.cleaned_data['password']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            user.save(force_update=True)
            return redirect('data_user:view')
        else:
            user = User.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'user': user,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            return render(request, template, data)
            # return HttpResponse(form.errors)

# #####################################################################################################################
# ###################################################### Guru #########################################################
# #####################################################################################################################



class ListUserGuruView(ManagementAccessView):
    def get(self, request):
        template = 'data_user/guru.html'
        form = UserForm(request.POST or None)
        # user = User.objects.filter(permisson='Administrator')

        group = Group.objects.get(name='Guru')
        users = group.user_set.all()
        data = {
        'form' : form,
		'user' : users,
        }
        return render(request, template, data)

class SaveDataUserGuruView(ManagementAccessView):
    def post(self, request):
        user_form = UserForm(request.POST or None, request.FILES)

        if user_form.is_valid():
            user = User()
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.last_name = request.POST['last_name']
            staff = request.POST.get('staff', None)
            if not staff == None:
                user.is_staff = True
                user.save()

                group = Group.objects.get(name='Guru')
                group.user_set.add(user)

                guru = Guru()
                guru.user = user
                guru.nama = user.last_name
                guru.save()

            else:
                 user.save()

            return redirect('data_user:guru')
        else:
            return HttpResponse(user_form.errors)

class HapusDataUserGuruView(ManagementAccessView):
    
    def get(self, request, id):
        user = User.objects.filter(id=id)
        if user.exists():
            user.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('data_user:guru')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 

class EditDataUserGuruView(ManagementAccessView):
    template = 'data_user/editguru.html'

    def get(self, request, id):
        user = User.objects.filter(id=id)
        if not user.exists():
            return redirect('data_user:guru')
        user = user.first()
        initial = {

            'id': user.id,
            'username': user.username,
            'last_name': user.last_name,
            'password': user.password,
        }

        form = UserForm(initial=initial)
        user = User.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'user' : user,
        }
        return render(request, self.template, data)


class UpdateDataUserGuruView(ManagementAccessView):

    def post(self, request):
        
        template = "data_user/guru.html"
        form = UserForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            user = User.objects.get(pk=id)
            user.username = form.cleaned_data['username']
            user.last_name = form.cleaned_data['last_name']
            user.password = form.cleaned_data['password']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            user.save(force_update=True)
            return redirect('data_user:guru')
        else:
            user = User.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'user': user,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            return render(request, template, data)
            # return HttpResponse(form.errors)