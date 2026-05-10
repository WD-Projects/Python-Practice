from django.shortcuts import render
from django import forms
from .models import Book
def home(request):
    book_list = Book.objects.all()
    context = {
        "books": book_list
    }
    return render(request=request, template_name='get_books.html', context = context)

# class BookCreateForm(forms.Form):
#     title = forms.CharField(
#         min_length=3,
#         max_length=30,
#         # help_text='This is title'
#     )
#     author = forms.CharField(
#         min_length=3,
#         max_length=30,
#         # help_text='This is title'
#     )
#     rating = forms.IntegerField()
#     description = forms.CharField(
#         # help_text='This is title'
#     )

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        # these fields name must be match to the model table and then django will automatically consider these fields name as backend name like name = 'title'
        fields = ["title", "author", "rating", "description"]

def create_books(request):
    # print(request.method)
    if request.method == "POST":
        data = request.POST
        form = BookCreateForm(data) 
        if form.is_valid():
            # when we use Modelform, we only use form.save()
            form.save()
            # Book.objects.create(
            #     # title = request.POST["title"],
            #     # author = request.POST["author"],
            #     # rating = request.POST["rating"],
            #     # description = request.POST["description"]
                
            #     title = form.cleaned_data["title"],
            #     author = form.cleaned_data["author"],
            #     rating = form.cleaned_data["rating"],
            #     description = form.cleaned_data["description"]
            # )
    else:
        form = BookCreateForm()
    context = {
        'form': form
    }
    return render(request=request, template_name='create_books.html', context=context)