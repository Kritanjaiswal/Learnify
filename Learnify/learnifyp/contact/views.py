from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Add any additional logic (e.g., sending emails) here
            return redirect('contact_success')  # Create a success page in your templates
    else:
        form = ContactForm()

    return render(request, 'contact_app/contact_form.html', {'form': form})
