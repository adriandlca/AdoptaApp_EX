from django import forms
from .models import TipoMascota, Mascota, Persona,PostMascota

class TipoMascotaForm(forms.ModelForm):
    class Meta:
        model = TipoMascota
        fields = ['nombre', 'descripcion']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Perro'
            }),
            'descripcion': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Ej. Mascotas caninas de todas las razas',
                'rows':3
            }) 
        }

        labels = {
            'nombre':'Nombre del tipo',
            'descripcion': 'Descripcion'
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre or nombre.strip() == '':
            raise forms.ValidationError("El nombre no puede estar vacio")
        if TipoMascota.objects.filter(nombre__iexact=nombre.strip()).exists():
            raise forms.ValidationError("Este tipo de mascota ya existe")
        return nombre.strip()
    
    def clean(self):
        cleaned = super().clean()
        nombre = cleaned.get('nombre')
        descripcion = cleaned.get('descripcion')
        if nombre and descripcion and nombre.strip().lower() == descripcion.strip().lower():
            raise forms.ValidationError("El nombre y la descripcion no pueden ser iguales")
        return cleaned
    '''
    class PostMascotaForm(form.ModelForm):
        class Meta:
            model = PostMascota
            fields = ['Titulo','Descripcion','Fecha','Foto']
            widgets = {
                'Titulo': forms.TextInput( attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ej. a los 4 años'
                }),
                'Descripcion': forms.Textarea(attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ej. Le inyectaron la vacuna Y',
                    'rows': 5
                }),
                'Fecha': forms.DateField(attrs={
                    'class': 'form-control',
                    'type': 'date'
                }),
                'Foto': forms.ImageField(attrs = {
                    'class': 'form-control',
                    'type': 'file',
                    'id': 'formFile'
                })
            }

            labels={
                'Titulo': 'Titulo del post',
                'Descripcion':'Descripcion',
                'Fecha':'Fecha',
                'Foto':'Foto'
            }
    '''
    
    """
        =========================================================
         SECCIÓN: CREAR EL FORMULARIO PostMascotaForm
         ---------------------------------------------------------
         TODO: Crear el formulario con los campos indicados
        =========================================================
    """