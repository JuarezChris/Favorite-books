from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    if 'user_first' not in request.session:
        return redirect("/")
    context = {
        "all_books": Book.objects.all()
        
    }
    # print (Message.objects.all().values())
    
    return render(request, 'book_app/books.html', context)

def log_out(request):
    request.session.flush()
    return redirect("/")

def add_fav_book(request):
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
    if len(errors): # checking for errors
        for key, value in errors.items():
            messages.error(request, value)
            return redirect ("/fav_book")
    else:
        this_user = User.objects.get(id=request.session['user_id'])
        id_book = Book.objects.create(title=request.POST['title'], description=request.POST['description'], user = this_user).id
        just_created=Book.objects.get(id=id_book)
        just_created.like.add(this_user)

    return redirect('/fav_book')


def update(request, num):
    if request.method == "POST":
        errors = User.objects.edit_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect ("/book_info/"+str(x.id))
    else:
        x = Book.objects.get(id=num)
        x.description = request.POST['description']
        x.save()
    return redirect("/book_info/"+str(x.id))

def unfav(request, num):
        this_user = User.objects.get(id=request.session['user_id'])
        this_book=Book.objects.get(id=num)
        this_book.like.remove(this_user)
        # this_book.save()
        return redirect("/book_info/"+str(this_book.id))

def book_info(request, num):
    book = Book.objects.get(id=num)
    liked_books=User.objects.filter(liked_books=book)
    print(len(liked_books))
    context = {
        "book_info": book,
        "liked_books": liked_books
    }
    return render(request,'book_app/book_info.html', context)


def destroy(request, num):
    unfav_to_delete = User.objects.get(id=num)	
    unfav_to_delete.delete()
    
    return redirect("//book_info/"+str(x.id))