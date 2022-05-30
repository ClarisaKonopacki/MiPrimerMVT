from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    edad = forms.CharField(label="Edad", max_length=50)
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    
class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")