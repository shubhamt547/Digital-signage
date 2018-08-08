from django.shortcuts import render
from .forms import AddAssetForm
from django.views.generic import View
from django.http import HttpResponse
import datetime
from .models import Asset

# Create your views here.

class index(View):
    def get(self, request, *args, **kwargs):
        inactive_assets = Asset.objects.filter(active=False)
        active_assets = Asset.objects.filter(active=True)
        asset_form = AddAssetForm()
        return render(request,'personal/home.html',context={'asset_form':asset_form,'active_assets':active_assets,'inactive_assets':inactive_assets})

    def post(self, request, *args, **kwargs):
        asset_form = AddAssetForm(request.POST, request.FILES)
        if asset_form.is_valid():
            instance = Asset(source=request.FILES['file'],start_date=datetime.datetime.now(),end_date=datetime.datetime.now()+datetime.timedelta(days=1))
            instance.name = instance.source.name
            instance.type = 'I' if 'image' in request.FILES['file'].content_type else 'V'
            instance.save()
            return HttpResponse('File uploaded successfully')
    def change_Asset_type(self,id):
        data = Asset.objects.all()[id]
        if data.active==True:
            data.active=False
            data.save()
        else:
            data.active=True
            data.save()


