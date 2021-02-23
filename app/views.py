from django.shortcuts import render, redirect
from app.model.contact import Contact
from app.forms.contact_form import ContactForm

# Create your views here.
def home(request):
    return render(request, 'index.html')


def contact_add(request):
    if request.method == 'POST':
        data = request.POST
        contact = Contact()
        contact_form = ContactForm(request.POST)
        if form.is_valid():
            contact.name = data.get('name')
            contact.email = data.get('email')
            contact.description = data.get('description')

            contact.save()
            return redirect('/')
    return render(request, 'index.html', {'contact' : contact})