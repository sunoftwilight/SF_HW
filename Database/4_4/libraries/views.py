from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm


def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'libraries/index.html', context)


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    reviews = book.review_set.all()
    if request.method == 'POST':
        
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            form.save()
            return redirect('libraries:detail', pk)
    else:
        form = ReviewForm()
    context = {
        'book': book,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'libraries/detail.html', context)


def delete(request, book_pk, review_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('libraries:detail', book_pk)