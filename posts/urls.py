from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]
