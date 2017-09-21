from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.response import SimpleTemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from todo.models import Todo


class TodoList(ListView):
    model = Todo
    template_name = "todo_list.html"


class CreateTodoView(CreateView):
    model = Todo
    fields = ['name']
    success_url = '/'


@csrf_exempt
def check_todo(request):
    if request.method == 'POST':
        todo_id = request.POST.get('id')
        todo = get_object_or_404(Todo, id=todo_id)
        todo.checked = not todo.checked
        todo.save()
    return JsonResponse({'success': 'true'})


import random


def pass_gen(pass_len, symb_len, num_len):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    symbols = "~!@#$%^&*()_+{}|:?></.,';][\=-`"

    num_letters = pass_len - symb_len - num_len

    pw_list = []

    if num_letters < 0:
        print("Incercati din nou...")
        exit()

    # litere mici
    i = 0

    while i < num_letters:
        pw_list.append(str(''.join(random.sample(letters, 1))))
        i += 1

    # simboluri
    k = 0
    symbol_inc = num_letters - 1

    while k < symb_len:
        pw_list.insert(random.randint(0, symbol_inc), str(''.join(random.sample(symbols, 1))))
        k += 1
        symbol_inc += 1

    # cifre
    l = 0
    num_inc = num_letters + symb_len - 1

    while l < num_len:
        pw_list.insert(random.randint(0, num_inc), str(random.randint(0, 9)))
        l += 1
        symbol_inc += 1

    # print parola

    return str(''.join(pw_list))


def homepage(reuqest):
    return SimpleTemplateResponse(template='TemaProiect.html')

@csrf_exempt
def genpass(request):
    parola = pass_gen(int(request.POST.get("nume1")), int(request.POST.get("nume2")), int(request.POST.get("nume3")))
    return SimpleTemplateResponse(template='TemaPRoiectPg2.html', context={'password': parola})
