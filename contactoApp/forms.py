from django import forms

class formcontacto(forms.Form):
    nombre =forms.CharField(label='Nombre', max_length=100)
    cel =forms.CharField(label='Celular', max_length=30)
    email = forms.EmailField(label='Email')
    mensaje = forms.CharField(label='Mensaje',widget=forms.Textarea)

    

