
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import thesis.views
import achievements.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name =  'home'),
    path('COVID_Dashboard/', jobs.views.COVID_Dashboard, name='COVID_Dashboard'),
    path('AirBnB_Listing/', jobs.views.AirBnB_Listing, name='AirBnB_Listing'),
    path('tableau_cv/', jobs.views.tableau_cv, name='tableau_cv'),
    path('HDIP_Project/', thesis.views.thesis, name =  'thesis'),
    path('achievements/', achievements.views.achievements, name = 'achievements'),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


handler404 = 'thesis.views.error_404_view'
