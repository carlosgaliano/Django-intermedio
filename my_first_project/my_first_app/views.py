from django.shortcuts import render

# Create your views here.

def my_view(request):

    car_list = [
        {'tittle': 'BMW'},
        {'tittle': 'TOYOTA'},
    ]

    return render(request, 'my_first_app/car_list.html', {'listaDeCarros':car_list})