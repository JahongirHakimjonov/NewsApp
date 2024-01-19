from django.shortcuts import render, redirect

from news.forms import ContactForm
from news.models import New


def home_page(request):
    news = New.objects.all()
    context = {
        "news": news,
    }
    return render(request, 'news/index.html', context=context)


def contact_page(request):
    news = New.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = ContactForm()
    context = {
        "news": news,
        "form": form,
    }
    return render(request, 'news/contact.html', context=context)


def single_page(request):
    news = New.objects.all()
    context = {
        "news": news,
    }
    return render(request, 'news/single_page.html', context=context)


def page_notfound(request):
    return render(request, 'news/404.html')