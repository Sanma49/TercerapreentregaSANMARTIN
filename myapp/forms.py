from django import forms
from .models import Author, Book, Review

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('book', 'content', 'rating',)

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)
