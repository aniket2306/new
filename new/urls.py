from django.contrib import admin
from django.urls import path
from django.confs.urls import url,include
from. import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.urls.static import static
from django.confs import settings

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^&',views.homepage),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
