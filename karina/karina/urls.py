
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import thesis.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name =  'home'),
    path('thesis/', thesis.views.thesis, name =  'thesis'),
#    path('crypto_choice/', thesis.views.crypto_choice, name =  'crypto_choice'),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
