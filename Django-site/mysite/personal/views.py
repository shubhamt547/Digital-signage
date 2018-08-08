from django.shortcuts import render
from .forms import AddAssetForm
from django.views.generic import View
from django.http import HttpResponse
import datetime
from .models import Asset

# Create your views here.

class index(View):
    def get(self, request):
        inactive_assets = Asset.objects.filter(active=False)
        active_assets = Asset.objects.filter(active=True)
        asset_form = AddAssetForm()
        return render(request, 'personal/home.html', context={'asset_form':asset_form,'active_assets':active_assets,'inactive_assets':inactive_assets})

    def post(self, request):
        asset_form = AddAssetForm(request.POST, request.FILES)
        if asset_form.is_valid():
            instance = Asset(source=request.FILES['file'],start_date=datetime.datetime.now(),end_date=datetime.datetime.now()+datetime.timedelta(days=1))
            instance.name = instance.source.name
            instance.type = 'I' if 'image' in request.FILES['file'].content_type else 'V'
            instance.save()
            return HttpResponse('File uploaded successfully')


class changeStatus(View):
    def post(self, request):
        try:
            asset_id = request.POST.get('id')
            status = request.POST.get('status')
            asset_object = Asset.objects.get(id=asset_id)
            if status=='active':
                asset_object.active = True
                asset_object.save()
            else:
                asset_object.active = False
                asset_object.save()
            return JsonResponse({'success': False, 'message': 'Successfully updated the status of {} to {}'.format(asset_object.name, status)})
        except Exception as e:
            print(e.message)
            return JsonResponse({'success': False, 'message': 'Unable to change status'})
