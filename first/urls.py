from django.urls import path
from . import views

urlpatterns = [ 
  path('',views.home,name='home'),
  path('index',views.index,name='index'),
  path('display',views.display,name='display'),
  path('dataset/<int:id>',views.dataset,name='dataset'),
  path('delete_data',views.delete_data,name='delete_data'),
  path('search_data',views.search_data,name='search_data'),
  path('edit_data',views.edit_data,name='edit_data'),
  path('edit_data1',views.edit_data1,name='edit_data1'),
]
