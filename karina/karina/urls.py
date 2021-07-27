
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import thesis.views
import covid.views
import achievements.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name =  'home'),
    path('thesis/', thesis.views.thesis, name =  'thesis'),
    path('COVID-Dashboard/', covid.views.COVID_Dashboard, name = 'COVID_Dashboard'),
    path('achievements/', achievements.views.achievements, name = 'achievements'),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
