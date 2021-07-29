from django.shortcuts import render, redirect
from rango.models import Category, Page
from rango.forms import CategoryForm


# Create your views here.

def index(request):
    # Show list of categories
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    # Show pages
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context = {'boldmessage': 'David Salazar'}

    return render(request, 'rango/about.html', context=context)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context=context_dict)


def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect('/rango/')

        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})

