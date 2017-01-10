"""tryTen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from profiles import views as profileViews
from contact import views as contactViews

urlpatterns = [
    # admin url
    url(r'^admin/', admin.site.urls),

    # for profile app
    url(r'^$', profileViews.home, name='home'),
    url(r'^about/$', profileViews.about, name='about'),

    # for contact app
    url(r'^contact/$', contactViews.contact, name='contact'),
]

# if settings.DEBUG:
#     urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)