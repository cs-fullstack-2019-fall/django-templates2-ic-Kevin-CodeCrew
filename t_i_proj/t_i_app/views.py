from django.shortcuts import render

cars = ['Honda', 'Toyota', 'GM', 'Nissan']


# Create your views here.
def base(request):
    print('Ace of the base')
    return render(request, 't_i_app/base.html', {'car_list': cars})


def car_list(request):
    print('cars list')
    return render(request, 't_i_app/child.html', {'car_list': cars})
