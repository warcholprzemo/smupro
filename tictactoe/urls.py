from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tictactoe.views import SaveResult, ListResult


urlpatterns = [
    path('saveresult/', SaveResult.as_view(), name='save-result'),
    path('allgames/', ListResult.as_view(), name='all-games'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
