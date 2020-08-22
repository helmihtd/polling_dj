from django.contrib import admin
# tambahkan include
from django.urls import include, path


# ketika pergi ke /polls maka akan mencari file di polls/urls.py
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
