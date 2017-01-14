from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


def contact(request):
    title = 'Contact us'
    form = ContactForm(request.POST or None)
    confirm_messege = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = "Message from django project"
        message = '%s %s' % (name, comment)
        emailForm = form.cleaned_data['email']
        emailTo = settings.EMAIL_HOST_USER
        send_mail(subject, message, emailForm, emailTo, fail_silently=True)
        title = "Thanks"
        confirm_messege = "Thanks for the messege. We will right back to you."
        form = None

    context = {'title': title, 'form': form, 'confirm_messege': confirm_messege}
    template = 'contact.html'
    return render(request, template, context)
