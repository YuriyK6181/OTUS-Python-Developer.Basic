from django.db import models
from .common import calc_orig_price, date_to_str_dmy, calc_diff_dt_in_HM


class Organization(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name="Наименование")
    fullname = models.CharField(max_length=512, blank=True, null=True, verbose_name="Полное наименование")
    phone1 = models.CharField(max_length=20, blank=True, null=True, verbose_name="Контактный телефон")
    phone2 = models.CharField(max_length=20, blank=True, null=True, verbose_name="Доп. телефон")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Адрес")
    org_email = models.CharField(max_length=128, blank=True, null=True, verbose_name="Эл. почта")
    org_site = models.CharField(max_length=255, blank=True, null=True, verbose_name="Официальный сайт")
    org_type = models.CharField(max_length=128, blank=True, null=True, verbose_name="Тип")
    archived = models.BooleanField(default=False, verbose_name="Архив")

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return str(self.name)


class BikeClass(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(null=False, blank=True, verbose_name='Описание')
    archived = models.BooleanField(default=False, verbose_name='Архив')

    class Meta:
        verbose_name = 'Класс велосипедов'
        verbose_name_plural = 'Классы велосипедов'

    def __str__(self):
        return self.name


class BikeType(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(null=False, blank=True, verbose_name='Описание')
    archived = models.BooleanField(default=False, verbose_name='Архив')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип велосипеда'
        verbose_name_plural = 'Типы велосипедов'


class Bike(models.Model):
    manufacturer = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='bike',
                                     verbose_name='Производитель')
    model_name = models.CharField(max_length=64, verbose_name='Модель')
    model_year = models.PositiveSmallIntegerField(verbose_name='Год модели')
    bike_class = models.ForeignKey(BikeClass, on_delete=models.PROTECT, related_name="bike", verbose_name='Класс')
    bike_type = models.ForeignKey(BikeType, on_delete=models.PROTECT, related_name='bike', verbose_name='Тип')
    description = models.TextField(blank=True, null=False, verbose_name='Описание')
    is_new = models.BooleanField(default=True, verbose_name='Новый')
    old_odo = models.PositiveIntegerField(blank=True, null=True, verbose_name='С пробегом, км')
    bought_date = models.DateField(blank=True, null=True, verbose_name='Дата покупки')
    bought_in = models.CharField(max_length=64, blank=True, null=True, verbose_name='Продавец')
    price = models.FloatField(blank=True, null=True, verbose_name='Цена')
    orig_price = models.FloatField(blank=True, null=True, verbose_name='Цена без скидки')
    discount = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Скидка')
    archived = models.BooleanField(default=False, verbose_name='Архив')

    class Meta:
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипеды'

    def __str__(self):
        return str(self.manufacturer) + " " + \
               str(self.model_name) + " '" + \
               str(self.model_year)

    def calc_price_info(self):
        if self.price:
            if not self.discount:
                self.discount = 0
            self.orig_price = calc_orig_price(self.price, self.discount)

    def save(self, *args, **kwargs):
        self.calc_price_info()
        super().save(*args, **kwargs)


class BikeEventType(models.Model):
    name = models.CharField(max_length=64, null=False, verbose_name='Наименование')
    description = models.CharField(max_length=512, null=True, blank=True, verbose_name='Описание')
    archived = models.BooleanField(default=False, verbose_name='Архив')

    class Meta:
        verbose_name = 'Тип велозаезда'
        verbose_name_plural = 'Типы велозаездов'

    def __str__(self):
        return self.name


class BikeRide(models.Model):
    verbose_name = 'Велозаезд'
    name = models.CharField(max_length=256, null=False, verbose_name="Название")
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name="Описание")
    route = models.CharField(max_length=1024, blank=True, null=True, verbose_name="Маршрут")
    ride_date = models.DateField(blank=True, null=True, verbose_name="Дата старта")
    ride_bike = models.ForeignKey(Bike, on_delete=models.PROTECT, related_name="bikeride", verbose_name="Велосипед")
    ride_type = models.ForeignKey(BikeEventType, on_delete=models.PROTECT, related_name="bikeride",
                                  verbose_name="Тип заезда")
    ride_planned = models.BooleanField(default=False, verbose_name="Запланированная поездка")
    ride_was_with_me = models.BooleanField(default=False, verbose_name="Участвовал в заезде")
    ride_start_dt = models.DateTimeField(null=False, blank=False, verbose_name="Старт")
    ride_finish_dt = models.DateTimeField(null=False, blank=False, verbose_name="Финиш")

    ride_time_all_h = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Общее время, ч")
    ride_time_all_m = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Общее время, мин")
    ride_time_all_rtm = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Общее время, в минутах")

    ride_time_h = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Время в движении, ч")
    ride_time_m = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Время в движении, мин")
    ride_time_rtm = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Время в движении, в минутах")

    ride_relax = models.FloatField(null=True, blank=True, verbose_name="Доля времени без движения, %")
    ride_kkal = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Энергозатраты, кКал")

    ride_dst = models.FloatField(null=False, blank=False, verbose_name="Дистанция")
    ride_odo = models.FloatField(null=False, blank=False, verbose_name="Одометр после")

    ride_avg_s = models.FloatField(null=True, blank=True, verbose_name="Скорость средняя")
    ride_max_s = models.FloatField(null=True, blank=True, verbose_name="Скорость макс.")

    ride_avg_c = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Каденс средний")
    ride_max_c = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Каденс макс.")

    ride_total_asc = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Набор высоты")
    ride_total_desc = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Набор спусков")

    ride_avg_pwr = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Мощность средняя")
    ride_max_pwr = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Мощность макс.")

    ride_fun_scale = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Оценка заезда (фан-фактор)")
    ride_hard_scale = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Оценка сложности")

    ride_url = models.CharField(max_length=512, null=True, blank=True, verbose_name="Ссылка на заезд")
    ride_track_url = models.CharField(max_length=512, null=True, blank=True, verbose_name="Ссылка на трек")

    admin_mark = models.CharField(max_length=20, null=True, blank=True, verbose_name="Метка админа")

    class Meta:
        verbose_name = 'Велозаезд'
        verbose_name_plural = 'Велозаезды'

    def __str__(self):
        return date_to_str_dmy(self.ride_date) + ' - "' + str(self.name) + '"'

    def calc_ride_time_info(self):
        if self.ride_start_dt and self.ride_finish_dt:
            hm_dif = calc_diff_dt_in_HM(self.ride_start_dt, self.ride_finish_dt)
            self.ride_time_all_h = hm_dif.h
            self.ride_time_all_m = hm_dif.m
            self.ride_time_rtm = hm_dif.h * 60 + hm_dif.m
            self.ride_date = self.ride_start_dt.date()

        if self.ride_time_all_h and self.ride_time_all_m and self.ride_time_m and self.ride_time_h:
            tm = self.ride_time_all_h * 60 + self.ride_time_all_m
            tr = self.ride_time_h * 60 + self.ride_time_m
            self.ride_time_all_rtm = tr
            self.ride_relax = round((1 - tr / tm) * 100, 2)

    def save(self, *args, **kwargs):
        self.calc_ride_time_info()
        super().save(*args, **kwargs)
