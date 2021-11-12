from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('createProduct/', views.createProduct,name='createProduct'),
    path('deleteProduct/<id_product>', views.deleteProduct,name='deleteProduct'),
    path('editProduct/<id_product>/', views.editProduct, name='editProduct'),
    path('listTypeProduct/', views.listTypeProduct, name='listTypeProduct'),
    path('createProductType/',views.createProductType, name='createProductType'),
    path('editProductType/<id_product_type>/', views.editProductType, name='editProductType'),
    path('deleteProductType/<id_product_type>', views.deleteProductType, name='deleteProductType'),
    path('listProvider/', views.listProvider, name='listProvider'),
    path('providerData/<id_provider>', views.providerData, name='providerData'),
    path('list2Provider/', views.list2Provider, name='list2Provider'),
    path('createProvider/', views.createProvider, name='createProvider'),
    path('deleteProvider/<id_provider>', views.deleteProvider, name='deleteProvider'),

]