from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.showroom_login),
    path('logging/',views.logging),
    path('logout/',views.showroom_logout),
    path('dashboard/',views.cars_dashboard),
    path('add_new_car/',views.add_new_car),
    path('create_new_car/',views.create_car),
    path('edit_car/<id>/',views.edit_car),
    path('update_car/<id>/',views.update_car),
    path('show_car/<id>/',views.show_car),
    path('upload_doc/<id>/',views.upload_doc),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)