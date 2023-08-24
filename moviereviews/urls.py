from django.contrib import admin
from django.urls import path
from movie import views as movieViews
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',movieViews.home, name='home'),
    path('about',movieViews.about),
    path('news/',include('news.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)