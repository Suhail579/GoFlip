"""
URL configuration for GoFlip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.utils.translation import template

from users import views
from users.views import CategoryProducts
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("",views.Home.as_view(),name="Home"),
    path("index/",views.Register.as_view(),name="index"),
    path("Otp/",views.Otp.as_view(),name="Otp"),
    path("Login",views.Login.as_view(),name="Login"),
    path("Choose/",views.Choose.as_view(),name="Choose"),
    path("Profile/",views.Profile.as_view(),name="Profile"),
    path("Editprofiles/",views.Editprofiles.as_view(),name="Editprofiles"),
    path("Addproduct/",views.Addproduct.as_view(),name="Addproduct"),
    path("Viewproduct/",views.Viewprodect.as_view(),name="Viewproduct"),
    path("bike/",views.Bike.as_view(),name="Bike"),
    path("Car/",views.Car.as_view(),name="Car"),
    path("Electronics/",views.Electronics.as_view(),name="Electronics"),
    path("Books/",views.Books.as_view(),name="Books"),
    path("Furnitures/", views.Furnitures.as_view(), name="Furnitures"),
    path("Mobiles/",views.Mobile.as_view(),name="Mobiles"),
    path("Gadgetss",views.Gadgetss.as_view(),name="Gadgetss"),
    path("Book_Details/<int:product>",views.Book_Details.as_view(),name="Book_Details"),
    path("Mobile_Details<int:product>/",views.Mobile_Details.as_view(),name="Mobile_Details"),
    path("Bike_Details<int:product>/",views.Bike_Details.as_view(),name="Bike_Details"),
    path("Electronics_Details<int:product>/",views.Electronics_Details.as_view(),name="Electronics_Details"),
    path("Car_Details<int:product>/", views.Car_Details.as_view(), name="Car_Details"),
    path("Furniture_Details<int:product>/", views.Furniture_Details.as_view(), name="Furniture_Details"),
    path("Gadgets_Details<int:product>/", views.Gadgets_Details.as_view(), name="Gadgets_Details"),
    path("category/<str:category>/",CategoryProducts.as_view(),name="CategoryProducts"),
    path("Search/", views.Search.as_view(), name="Search"),
    path("Logout/",views.Logout.as_view(),name="Logout"),
]




from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
