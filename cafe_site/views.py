from django.contrib import messages
from django.shortcuts import render
from cafe_site.forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'There was an error sending your message.')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')