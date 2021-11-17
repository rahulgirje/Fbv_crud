from . import views
from django.urls import path

urlpatterns = [
    path('allprod/', views.productview, name = 'allprods'),
    path('addprod/', views.addview, name = 'addprod'),
    path('delprod/<int:i>/', views.deleteview, name = 'del'),
    path('updtprod/<int:oid>/', views.updateview, name = 'updt')
]