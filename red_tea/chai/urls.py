from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.chai,name='chai'),
    path('chai/<int:chai_id>/', views.chai_description, name='chai_description'),
    path('find_store/', views.find_chai_store, name='find_store'),

]
