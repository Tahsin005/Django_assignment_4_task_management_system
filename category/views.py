from django.shortcuts import render, redirect
from category.forms import CategoryForm
from category.models import CategoryModel
# Create your views here.
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            print (form.cleaned_data)
            return redirect('task_list')
    categories = CategoryModel.objects.all()
    
    return render(request, 'add_category.html', {'form': form, 'categories': categories})