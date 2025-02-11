from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    cars = Car.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, {'cars': cars})  # передайте необходимый контекст


def car_details_view(request, car_id):
    car = Car.objects.get(id=car_id)
    template_name = 'main/details.html'
    return render(request, template_name, {'car': car})  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car).select_related('client')
        template_name = 'main/sales.html'
        return render(request, template_name, {'car': car, 'sales': sales})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
