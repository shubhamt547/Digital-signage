from django.shortcuts import render,get_object_or_404,get_list_or_404
from .forms import AddAssetForm
from django.views.generic import View
from django.http import  JsonResponse ,HttpResponseRedirect,HttpResponse
from django.db.models import Q
from mimetypes import MimeTypes
from .models import Asset
import datetime
from django.utils import timezone
import os
import mimetypes
# Create your views here.
mime = MimeTypes()


class Index(View):
    def get(self, request):
        changed_time=Asset.changed_time
        query = Q(active=True,end_date__gte=datetime.datetime.now(),start_date__lte=datetime.datetime.now())
        inactive_assets = Asset.objects.exclude(query).order_by('id')
        active_assets = Asset.objects.filter(query).order_by('changed_time')
        asset_form = AddAssetForm()
        #        #edit_asset_form = EditAssetForm()
        return render(request, 'personal/home.html', context={'asset_form':asset_form,'active_assets':active_assets,'inactive_assets':inactive_assets})

    def post(self, request):
        asset_form = AddAssetForm(request.POST, request.FILES)
        if asset_form.is_valid():
            instance = Asset(source=request.FILES['file'],start_date=timezone.now(),end_date=datetime.datetime.now()+datetime.timedelta(days=1))
            instance.name = instance.source.name
            mime_type = mime.guess_type(instance.source.url,strict=True)
#             mime_type=mimetypes.guess_type(instance.name)
            if 'image' in mime_type[0]:
                instance.type='I'
            else:
                instance.type='V'
            instance.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # return HttpResponse('File uploaded successfully')

class EditAsset(View):
    def post(self, request):
        #edit_asset_form =EditAssetForm(request.POST, request.FILES)
        #if edit_asset_form.is_valid():
        try:
            asset_id = request.POST.get('assetId')
            asset_object = Asset.objects.get(id=asset_id)
            active=asset_object.active
            duration = request.POST.get('duration')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            asset_object.name=request.POST.get('name')
            asset_object.start_date=datetime.datetime.strptime(start_date,'%m/%d/%Y %I:%M %p')
            asset_object.end_date=datetime.datetime.strptime(end_date,'%m/%d/%Y %I:%M %p')
            asset_object.duration=duration
            asset_object.active=active
            asset_object.save()
            return JsonResponse({'success': True, 'message': 'Successfully updated the status' })
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': 'Unable to edit the asset'})
            # instance = Asset(source=request.FILES['file'],start_date=request.FILES['start_date'],end_date=datetime.datetime.now()+datetime.timedelta(days=1))
            # instance.name = instance.source
            # mime_type = mime.guess_type(instance.source.path)
            # instance.type = 'I' if 'image' in mime_type else 'V'
            # instance.save()
            #return HttpResponse('File edited successfully')

class changeStatus(View):
    def post(self, request):
        try:
            asset_id = request.POST.get('assetId')
            status= request.POST.get('status')
            asset_object = Asset.objects.get(id=asset_id)
            if status=='active':
                asset_object.active = True
                asset_object.changed_time=timezone.now()
                asset_object.save()
            else:
                asset_object.active = False
                asset_object.save()
            return JsonResponse({'success': True, 'message': 'Successfully updated the status of {} to {}'.format(asset_object.name, status)})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': 'Unable to change status'})

class  deleteAsset(View):
    def post(self,request):
        try:
            asset_id=request.POST.get('assetId')
            delete_item=Asset.objects.get(id=asset_id)
            name=delete_item.name
            delete_item.delete()
            # os.chdir('C:/Users/stiwari/PycharmProjects/Web-app/Django-site/mysite/uploads')
            # os.remove(name)
            return JsonResponse({'success': True,'message': '{} Successfully deleted'.format(name)})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message':'Unable to delete'})

#
# class fetchingAsset(View):
#     def get(self,request):
#         try:
#             query = Q(active=True,end_date__gte=datetime.datetime.now(),start_date__lte=datetime.datetime.now())
#             active_assets = Asset.objects.filter(query).order_by('changed_time')
#             lst=[]
#             for i in active_assets:
#                 lst.append({'duration':i.duration,'url':i.source.url,'id':i.id})
#             return JsonResponse({'success': True,'asset':lst})
#         except Exception as e:
#             print(e)
#             return JsonResponse({'success': False})


from filetransfers.api import serve_file,public_download_url
from time import sleep
class fetchingAsset(View):
    def get(self,request,id):
        try:
            id=int(id)
            query = Q(active=True,end_date__gte=datetime.datetime.now(),start_date__lte=datetime.datetime.now())
            active_assets = Asset.objects.filter(query).order_by('changed_time')
            lst=[]
            for i in active_assets:
                lst.append(i.id)
            if id in lst:
                upload=get_object_or_404(Asset,pk=id)
                return (serve_file(request,upload.source,save_as=True))
        except Exception as p:
            print(p)
            return JsonResponse({'success': False})


class FileDownload(View):
    def get(self,request):
        try:
            query = Q(active=True,end_date__gte=datetime.datetime.now(),start_date__lte=datetime.datetime.now())
            active_assets = Asset.objects.filter(query).order_by('changed_time')
            lst=[]
            for i in active_assets:
                lst.append({'duration':i.duration,'url':i.source.url,'id':i.id})
            return JsonResponse({'success': True,'asset':lst})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False})