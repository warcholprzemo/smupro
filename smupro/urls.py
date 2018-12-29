"""smupro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.static import serve

from multiplex.views import HallList
from pocket.views import BlogList, SomeDataList, SomeDataPost, BlogDetail, MyImageCreate, MyImageList



# # I don't need this now... TODO: move somwehere else
# # Serializers define the API representation
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
#
#
# # ViewSets define the view behavior
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# # Routers provide an easy way to automatically determining the URL conf
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
#
# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browsable API


urlpatterns = [
    path('api/multiplex/', include('multiplex.urls')),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/processform/', SomeDataPost.as_view(), name='some_data_post'),
    path('api/some-data-list/', SomeDataList.as_view(), name='some_data_list'),
    path('api/tictactoe/', include('tictactoe.urls')),
    path('api/blog/', BlogList.as_view(), name='blog_list'),
    path('api/blog/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('api/myimage/create/', MyImageCreate.as_view(), name='myimage_create'),
    path('api/myimage/list/', MyImageList.as_view(), name='myimage_list'),
]

if settings.DEBUG is False:
    #extensions = staticfiles_urlpatterns()
    extensions = []
    extensions += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]
    #extensions += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    extensions += [re_path('.*', TemplateView.as_view(template_name='index.html')),]
else:
    extensions = [
        path('admin/', admin.site.urls),
        # path('', include(router.urls)),
        path('', HallList.as_view(), name='main-page'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns.extend(extensions)
