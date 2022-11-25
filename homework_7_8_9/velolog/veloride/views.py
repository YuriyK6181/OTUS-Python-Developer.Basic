
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Bike, BikeRide
from .forms import (BikeCreateForm, BikeUpdateForm,
                    BikeRideCreateForm, BikeRideUpdateForm,
                    )

from django.http import HttpResponseRedirect


class BikesListView(ListView):
    template_name = "veloride/index.html"
    context_object_name = "veloride"
    queryset = (
        Bike
        .objects
        .select_related("bike_class")
        .select_related("bike_type")
        .filter(archived=False)
        .order_by("pk")
        .all()
    )


class BikeDetailView(DetailView):
    template_name = "veloride/details.html"
    context_object_name = "bike"
    queryset = (
        Bike
        .objects
        .select_related("bike_class")
        .select_related("bike_type")
        .filter(archived=False)
        .order_by("pk")
        .all()
    )


class BikeCreateView(CreateView):
    model = Bike
    form_class = BikeCreateForm

    def get_success_url(self):
        return reverse("veloride:index")


class BikeUpdateView(UpdateView):
    model = Bike
    form_class = BikeUpdateForm
    template_name = 'veloride/bike_update_form.html'
    success_url = reverse_lazy("veloride:index")


class BikeDeleteView(DeleteView):
    model = Bike
    success_url = reverse_lazy("veloride:index")
    context_object_name = "bike"

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class BikeRidesListView(ListView):
    template_name = "veloride/bikerides_list.html"
    context_object_name = "bikerides"

    queryset = (
        BikeRide
        .objects
        .select_related("ride_bike")
        .select_related("ride_type")
        .order_by("ride_date")
        .all()
    )


class BikeRideDetailView(DetailView):
    template_name = "veloride/bikeride_details.html"
    context_object_name = "bikeride"
    #ride_id = str(BikeRide.pk)
    queryset = (
        BikeRide
        .objects
        .select_related("ride_bike")
        .select_related("ride_type")
    )


class BikeRideCreateView(CreateView):
    model = BikeRide
    form_class = BikeRideCreateForm

    def get_success_url(self):
        return reverse("veloride:bikerides")


class BikeRideUpdateView(UpdateView):
    model = BikeRide
    form_class = BikeRideUpdateForm

    def get_success_url(self):
        return reverse("veloride:bikerides")


class BikeRideDeleteView(DeleteView):
    model = BikeRide
    success_url = reverse_lazy("veloride:bikerides")
    context_object_name = "bikeride"

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)



