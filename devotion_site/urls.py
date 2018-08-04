from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manifest', views.manifest, name='manifest'),
    # path('content/bible/<slug:version>/<slug:collection>/<slug:book>/<int:chapter>', views.bible_audio, name='bible'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.auth_login, name='login'),
    path('logout/', auth_views.auth_logout, name='logout'),
]