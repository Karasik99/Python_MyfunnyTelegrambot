from . import views
from django.urls import path

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    path('about', views.about, name = 'about'),
    path('addpage/', views.AddPage.as_view(), name = 'add_page'),
    path('contact/', views.contact, name = 'contact'),
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name = 'post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name = 'category')


]
