from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tictactoe.views import SaveResult


urlpatterns = [
    path('saveresult/', SaveResult.as_view(), name='save-result')
]
urlpatterns = format_suffix_patterns(urlpatterns)
