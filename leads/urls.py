from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("", views.LeadListView.as_view(), name="lead-list"),
    path("create", views.LeadCreateView.as_view(), name="lead-create"),
    path("<int:pk>/", views.LeadDetailView.as_view(), name="lead-detail"),
    path("<int:pk>/update", views.LeadUpdateView.as_view(), name="lead-update"),
]
