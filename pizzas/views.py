from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import Http404
from pizzas.models import Pizza, Topping
from pizzas.forms import PizzaForm, ToppingForm

def menu(request):
  pizzas = Pizza.objects.order_by('date_added')
  context = {'pizzas': pizzas}
  return render(request, 'menu.html', context)

# Single Object Query
def pizza(request, pizza_id):
  pizza = Pizza.objects.get(id=pizza_id)
  toppings = pizza.topping_set.order_by('-date_added')
  context = {'pizza': pizza, 'toppings': toppings}
  return render(request, 'pizza.html', context)


def new_pizza(request):
  """Add a new Pizza."""
  
  if request.method != 'POST':
    # No data submitted; create a blank form.
    form = PizzaForm()
  else:
    form = PizzaForm(request.POST)
    if form.is_valid():
      new_pizza = form.save(commit=False)
      # new_pizza.owner = request.user
      new_pizza.save()
      return redirect('pizzas:menu')

  # Display a blank or invalid form.
  context = {'form': form}
  return render(request, 'new_pizza.html', context)


def new_topping(request, pizza_id):
  """Add a new Topping."""

  pizza = Pizza.objects.get(id=pizza_id)
  # if Pizza.owner != request.user:
  #   raise Http404
  
  if request.method != 'POST':
    # No data submitted; create a blank form.
    form = ToppingForm()
  else:
    form = ToppingForm(request.POST)
    if form.is_valid():
      new_topping = form.save(commit=False)
      new_topping.pizza = pizza
      # new_pizza.owner = request.user
      new_topping.save()
      return HttpResponseRedirect(reverse('pizzas:pizza', args=[pizza_id]))

  # Display a blank or invalid form.
  context = {'pizza': pizza, 'form': form}
  return render(request, 'new_topping.html', context)

# def topping(request, topping_id):
#   toppings = Topping.objects.get(topping_id)
#   context = {'toppings': toppings}
#   return render(request, 'menu.html', context)

# All Objects Queries
# def pizzas(request):
#   pizzas = Pizza.objects.order_by('date_added')
#   context = {'pizzas': pizzas}
#   return render(request, 'menu.html', context)

# def toppings(request):
#   toppings = Topping.objects.order_by('date_added')
#   context = {'toppings': toppings}
#   return render(request, 'menu.html', context)