from django.shortcuts import render,redirect,get_object_or_404,reverse,HttpResponseRedirect
from .models import *
from .forms import BookForm,CategoryForm

# Create your views here.

def index(request):
   

    if request.method=='POST':
        data = BookForm(request.POST,request.FILES)
        catdata = CategoryForm(request.POST)
        if data.is_valid():
            data.save()  
            return HttpResponseRedirect("/")
        if catdata.is_valid():
            catdata.save()
            return HttpResponseRedirect("/")   

    # x=Book.objects.all()
    # y=Category.objects.all()
    # f=BookForm()
    # cf=CategoryForm()
    context ={
        'books' :Book.objects.all(),
        'categories':Category.objects.all(),
        'form':BookForm(),
        'formc':CategoryForm(),

    }

    return render(request,'pages/index.html',context=context)


def books(request):
    search = Book.objects.all()
    title=None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)


    
    y=Category.objects.all()
    context ={
        'books' :search,
        'categories':y
    }
    return render(request,'pages/books.html',context=context)


    

    

def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method =='POST':
        data=BookForm(request.POST,request.FILES,instance=book_id)
        if data.is_valid():
              data.save()
              return redirect('/')
    if request.method == 'GET':
        data=BookForm(instance =book_id)             
    context ={
        'form':data     
    }
    return render(request,'pages/update.html',context)

def delete(request,id):
    book_del=get_object_or_404(Book,id=id)    
    if request.method =='POST':
        book_del.delete()
        return redirect('/')
    return render(request,'pages/delete.html')    



