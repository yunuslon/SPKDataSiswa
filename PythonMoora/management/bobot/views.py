from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Bobot
from management.bobot.forms import BobotForm
from library.view import ManagementAccessView
# Create your views here.


class ListBobotView(ManagementAccessView):
	def get(self, request):

		template = 'bobot/index.html'

		form = BobotForm(request.POST or None)
		bobot = Bobot.objects.all()
		data = {
        'form_mode' : 'add',
        'form' : form,
		'bobot' : bobot,
		}
		return render(request, template, data)

class EditBobotView(ManagementAccessView):
    template = 'bobot/index.html'

    def get(self, request, id):
        bobot = Bobot.objects.filter(id=id)
        if not bobot.exists():
            return redirect('bobot:view')
        bobot = bobot.first()
        initial = {

            'id': bobot.id,
            'nilai_akademik' : bobot.nilai_akademik,
            'kelas' : bobot.kelas,
            'karakter' : bobot.karakter,
            'plomba'	: bobot.plomba,
            'hasil_tes' : bobot.hasil_tes,
        }

        form = BobotForm(initial=initial)
        bobot = Bobot.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'bobot' : bobot,
        }
        return render(request, self.template, data)



class UpdateBobotView(ManagementAccessView):

    def post(self, request):
        
        template = "bobot/index.html"
        form = BobotForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            bobot = Bobot.objects.get(pk=id)
            bobot.nilai_akademik = form.cleaned_data['nilai_akademik']
            bobot.kelas = form.cleaned_data['kelas']
            bobot.karakter = form.cleaned_data['karakter']
            bobot.plomba = form.cleaned_data['plomba']
            bobot.hasil_tes = form.cleaned_data['hasil_tes']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            bobot.save(force_update=True)
            return redirect('bobot:view')
        else:
            bobot = bobot.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'bobot': bobot,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            return render(request, template, data)

