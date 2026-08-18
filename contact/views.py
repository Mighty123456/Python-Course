from django.shortcuts import render
from forms import ContactForm

def contact_view(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you can process the data — e.g., save to DB or send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"New message from {name} ({email}): {message}")
            submitted = True
            form = ContactForm()  # clear the form
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'submitted': submitted})
