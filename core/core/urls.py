from django.contrib import admin
from django.urls import include, path
from accounts.views import *

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls', namespace='quiz')),
    path('accounts/', include('accounts.urls')),
]
