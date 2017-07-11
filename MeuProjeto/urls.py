# Arquivo: MeuProjeto/urls.py
from django.conf.urls import include, url
from django.contrib import admin

import apps.users.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('apps.users.urls', namespace="users")),
]


