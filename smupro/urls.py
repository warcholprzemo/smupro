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
from django.contrib import admin
from django.urls import include, path
from multiplex.views import HallList
from pocket.views import SomeDataList, SomeDataPost


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
    path('admin/', admin.site.urls),
    path('multiplex/', include('multiplex.urls')),
    #path('', include(router.urls)),
    path('', HallList.as_view(), name='main-page'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('processform/', SomeDataPost.as_view(), name='some_data_post'),
    path('some-data-list/', SomeDataList.as_view(), name='some_data_list'),
]
