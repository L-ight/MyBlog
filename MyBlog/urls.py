"""MyBlog URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from DjangoUeditor import urls as DjangoUeditor_urls

from views import home as home_view
from Classification import urls as Classification_urls
from Tag import urls as Tag_urls
from Article import urls as Article_urls

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^$',home_view),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^Classifications/',include(Classification_urls)),
    url(r'^Tag/', include(Tag_urls)),
     url(r'Article/',include(Article_urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
