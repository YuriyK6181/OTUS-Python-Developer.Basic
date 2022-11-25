from django.contrib.auth.forms import AuthenticationForm as AuthenticationFormGeneric
from django.forms import ModelForm, CharField, IntegerField, TextInput, DateInput, BooleanField, FloatField
from django.forms.widgets import Widget
from django.forms import Widget
from .models import Bike, BikeRide
from django.db import models

WIDGET_CLASS_FOR_TYPE = {"BooleanField": "checkbox", "TextField": "textarea", "DateField": "textarea",
                         "DateTimeField": "text", "CharField": "text"}
WIDGET_FORMAT_FOR_TYPE = {"DateField": "d.m.Y", "DateTimeField": "d.m.Y H:i:s", "TimeField": "H:i:s"}


class AuthenticationForm(AuthenticationFormGeneric):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"


class BikeCreateForm(ModelForm):
    class Meta:
        model = Bike
        fields = ("manufacturer", "model_name", "model_year",
                  "bike_class", "bike_type",
                  "description", "is_new", "old_odo", "bought_date",
                  "bought_in", "price", "discount", "archived")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        model_fields = dict((f.name, str(f.__class__)) for f in self._meta.model._meta.fields)
        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            # change widget class by fieldnames
            cur_field = model_fields[name]

            if cur_field.find("BooleanField") > 0:
                widget.attrs["class"] = "checkbox"
            else:
                widget.attrs["class"] = "form-control"


class BikeUpdateForm(ModelForm):
    class Meta:
        model = Bike
        fields = ("manufacturer", "model_name", "model_year",
                  "bike_class", "bike_type",
                  "description", "is_new", "old_odo", "bought_date",
                  "bought_in", "price", "discount", "archived")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        model_fields = dict((f.name, str(f.__class__)) for f in self._meta.model._meta.fields)
        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            # change widget class by fieldnames
            cur_field = model_fields[name]

            if cur_field.find("BooleanField") > 0:
                widget.attrs["class"] = "checkbox"
            else:
                widget.attrs["class"] = "form-control"


class BikeRideCreateForm(ModelForm):
    class Meta:
        model = BikeRide
        fields = ("name", "description", "route", "ride_bike", "ride_type",
                  "ride_planned", "ride_was_with_me",
                  "ride_start_dt", "ride_finish_dt", "ride_time_all_h", "ride_time_all_m", "ride_time_h", "ride_time_m",
                  "ride_relax", "ride_kkal",
                  "ride_dst", "ride_odo", "ride_avg_s", "ride_max_s", "ride_avg_c", "ride_max_c", "ride_total_asc",
                  "ride_total_desc",
                  "ride_avg_pwr", "ride_max_pwr", "ride_fun_scale", "ride_hard_scale", "ride_url", "ride_track_url")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        model_fields = dict((f.name, str(f.__class__)) for f in self._meta.model._meta.fields)
        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            # change widget class by fieldnames
            cur_field = model_fields[name]

            if cur_field.find("BooleanField") > 0:
                widget.attrs["class"] = "checkbox"
            else:
                widget.attrs["class"] = "form-control"


class BikeRideUpdateForm(ModelForm):
    class Meta:
        model = BikeRide
        fields = ("name", "description", "route", "ride_bike", "ride_type",
                  "ride_planned", "ride_was_with_me",
                  "ride_start_dt", "ride_finish_dt", "ride_time_all_h", "ride_time_all_m", "ride_time_h", "ride_time_m",
                  "ride_relax", "ride_kkal",
                  "ride_dst", "ride_odo", "ride_avg_s", "ride_max_s", "ride_avg_c", "ride_max_c", "ride_total_asc",
                  "ride_total_desc",
                  "ride_avg_pwr", "ride_max_pwr", "ride_fun_scale", "ride_hard_scale", "ride_url", "ride_track_url")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        model_fields = dict((f.name, str(f.__class__)) for f in self._meta.model._meta.fields)
        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            # change widget class by fieldnames
            cur_field = model_fields[name]

            if cur_field.find("BooleanField") > 0:
                widget.attrs["class"] = "checkbox"
            else:
                widget.attrs["class"] = "form-control"

