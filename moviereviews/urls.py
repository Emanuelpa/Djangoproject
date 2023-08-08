from django.contrib import admin
from django.urls import path
from movie import views as movieViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',movieViews.home),
    path('about',movieViews.about),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)