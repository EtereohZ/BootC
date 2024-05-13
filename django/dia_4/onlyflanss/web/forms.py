from django import forms

class ContactDataForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'cols':50}))
    customer_email.widget.attrs.update(size='50')
    customer_name.widget.attrs.update(size='50')