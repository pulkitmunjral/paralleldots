from . import views
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('fetch/<str:data_requested>', views.fetch, name='fetch'),
    path('', RedirectView.as_view(url='fetch/anything')),
]
