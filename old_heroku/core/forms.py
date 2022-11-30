from django.conf import settings
from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Telefone', max_length=13, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=300 )

    def send_mail(self):
        #recipient = [settings.EMAIL_HOST_USER]
        #sender = self.cleaned_data['email']
        #subject = "CONTATO - " + self.cleaned_data['name']
        #message = " TELEFONE: " + self.cleaned_data['phone'] + "\n MENSAGEM:" + self.cleaned_data['message'] + "\n EMAIL: " + self.cleaned_data['email']
        #print("Contact: email sent to: " + sender)
        #send_mail(subject, message, sender, recipient)
        pass