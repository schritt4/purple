
from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('curation/<int:curation_id>/', c_detail, name='c_detail')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
