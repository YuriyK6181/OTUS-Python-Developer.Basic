
from django.urls import path
from .views import (
    BikesListView,
    BikeDetailView,
    BikeUpdateView,
    BikeCreateView,
    BikeDeleteView,

    BikeRidesListView,
    BikeRideDetailView,
    BikeRideCreateView,
    BikeRideUpdateView,
    BikeRideDeleteView,
)

app_name = "veloride"

urlpatterns = [
    path("", BikesListView.as_view(), name="index"),
    path("<int:pk>/", BikeDetailView.as_view(), name="details"),
    path("create/", BikeCreateView.as_view(), name="create"),
    path("<int:pk>/update/", BikeUpdateView.as_view(), name="update"),
    path("<int:pk>/confirm-delete/", BikeDeleteView.as_view(), name="delete"),

    path("bikerides/", BikeRidesListView.as_view(), name="bikerides"),
    path("bikerides/<int:pk>", BikeRideDetailView.as_view(), name="bikeride"),
    path("bikerides/create/", BikeRideCreateView.as_view(), name="create-bikeride"),
    path("bikerides/<int:pk>/update/", BikeRideUpdateView.as_view(), name="update-bikeride"),
    path("bikerides/<int:pk>/confirm-delete/", BikeRideDeleteView.as_view(), name="delete-bikeride"),
]