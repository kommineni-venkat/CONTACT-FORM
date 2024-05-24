from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm  

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            
            email_subject = 'New Contact Form Submission'
            email_body = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content,
            })

            email_message = EmailMessage(
                email_subject,
                email_body,
                'your_email@example.com',  
                ['recipient@example.com'],  
            )
            email_message.content_subtype = 'html'
            email_message.send()

            return redirect('success_page')  
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {'form': form})
