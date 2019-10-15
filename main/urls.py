from django.urls import path
from main import views
app_name = 'main'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('thermoglobe/resources/',views.ResourcesView.as_view(),name='resources'),
    path('thermoglobe/site/<pk>/', views.SiteView.as_view(), name='site'),
    path('upload/',views.UploadView.as_view(),name='upload'),
    path('upload/confirm/',views.ConfirmUploadView.as_view(),name='confirm_upload'),
]
