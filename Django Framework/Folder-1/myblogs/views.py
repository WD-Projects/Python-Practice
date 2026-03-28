from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Blog
def home(request):
    blog_list = Blog.objects.all() # SELECT * FROM myblogs_blog
    context = {
        'name': 'Mahir',
        'roll': 193,
        'blogs': blog_list
    }
    final_text = render_to_string(template_name="abc.html", context=context)
    return HttpResponse(final_text)