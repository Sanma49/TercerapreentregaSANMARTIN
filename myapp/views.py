from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Author, Book, Review
from .forms import AuthorForm, BookForm, ReviewForm, SearchForm

def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    reviews = Review.objects.all()

    author_form = AuthorForm()
    book_form = BookForm()
    review_form = ReviewForm()
    search_form = SearchForm()

    if request.method == 'POST':
        if 'author_form' in request.POST:
            author_form = AuthorForm(request.POST)
            if author_form.is_valid():
                author_form.save()

        elif 'book_form' in request.POST:
            book_form = BookForm(request.POST)
            if book_form.is_valid():
                book_form.save()

        elif 'review_form' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review_form.save()

        elif 'search_form' in request.POST:
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                search_query = search_form.cleaned_data['search_query']
                books = Book.objects.filter(title__icontains=search_query)

    context = {
        'authors': authors,
        'books': books,
        'reviews': reviews,
        'author_form': author_form,
        'book_form': book_form,
        'review_form': review_form,
        'search_form': search_form,
    }

    return render(request, 'myapp/index.html', context)
