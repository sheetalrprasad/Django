from . import views
from django.urls import path

#For template taggin in HTML
app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name = 'list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name = 'create'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete'),
]
