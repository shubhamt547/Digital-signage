# import cv2
# import datetime
# from django.db.models import Q
# from  Web-app.Django-site.mysite.personal.models import Asset
#
# query = Q(active=True, end_date__gte=datetime.datetime.now(), start_date__lte=datetime.datetime.now())
# active_assets = Asset.objects.filter(query).order_by('changed_time')
# # from personal.models import Asset
#
# import sqlite3
# obj=sqlite3.connect('db.sqlite3')
# #print(obj)
# cur = obj.cursor()
# save=cur.execute('select * FROM personal_Asset')
# lst=list(save.fetchall())
# #print(save)
#
# print(lst)
# obj.close()
#
# image1=cv2.imread('4.png')
# img2=cv2.imread('6.png')
# height, width = image1.shape[:2]
# print(height,width)
# thumbnail = cv2.resize(image1, (width/2, height/2), interpolation = cv2.INTER_AREA)
# cv2.imshow('image1',thumbnail)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()
# height, width = img2.shape[:2]
# thumbnail1 = cv2.resize(img2, (width/2, height/2), interpolation = cv2.INTER_AREA)
# cv2.imshow('img2',thumbnail1)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()