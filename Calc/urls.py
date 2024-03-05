from django.contrib import admin
from django.urls import path,include, re_path
from Calc import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('login/',views.user_login,name="user_login"),
    path('signup/',views.signup,name="Signup"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
