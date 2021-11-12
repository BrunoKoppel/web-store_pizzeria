from django.shortcuts import render
from pizzas.models import Pizza, Topping

def menu(request):
  pizzas = Pizza.objects.order_by('date_added')
  context = {'pizzas': pizzas}
  return render(request, 'menu.html', context)

# All Objects Queries
# def pizzas(request):
#   pizzas = Pizza.objects.order_by('date_added')
#   context = {'pizzas': pizzas}
#   return render(request, 'menu.html', context)

# def toppings(request):
#   toppings = Topping.objects.order_by('date_added')
#   context = {'toppings': toppings}
#   return render(request, 'menu.html', context)

# Single Object Query
def pizza(request, pizza_id):
  pizza = Pizza.objects.get(id=pizza_id)
  toppings = pizza.topping_set.order_by('-date_added')
  context = {'pizza': pizza, 'toppings': toppings}
  return render(request, 'pizza.html', context)

# def topping(request, topping_id):
#   toppings = Topping.objects.get(topping_id)
#   context = {'toppings': toppings}
#   return render(request, 'menu.html', context)