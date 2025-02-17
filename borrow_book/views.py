from django.shortcuts import render,redirect
from . import forms,models

def add_book(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, request.FILES)  # Add request.FILES
        if post_form.is_valid():
            post_form.save()
            return redirect('available_book')
    else:
        post_form = forms.PostForm()
    return render(request, 'add_books.html', {'form': post_form})


def available_book(request):
    books = models.Book_Model.objects.all()
    return render(request, 'available_books.html', {'books': books})
