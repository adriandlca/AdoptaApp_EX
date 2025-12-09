from django import forms
from datetime import datetime,date
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


class PostMascotaForm(forms.ModelForm):
        class Meta:
            model = PostMascota
            fields = ['titulo','descripcion','fecha','foto']
            
            widgets = {
                'titulo': forms.TextInput( attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ej. a los 4 años'
                }),
                'descripcion': forms.Textarea(attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ej. Le inyectaron la vacuna Y',
                    'rows': 5
                }),
                'fecha': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type': 'date'
                }),
                'foto': forms.FileInput(attrs = {
                    'class': 'form-control', 
                    'type': 'file',
                    'id': 'formFile'
                })
            }

            labels={
                'titulo': 'Titulo del post',
                'descripcion':'Descripcion',
                'fecha':'Fecha',
                'foto':'Foto'
            }
        
        def clean_descripcion(self):
            descripcion = self.cleaned_data.get('descripcion')
            if not descripcion or len(descripcion) < 20:
                raise forms.ValidationError("La descripción debe de tener más de 20 caracteres")
            return descripcion.strip()
        

        def clean_fecha(self):
            fecha = self.cleaned_data.get('fecha')
            hoy = date.today() 
            if fecha and fecha > hoy:
                raise forms.ValidationError('La fecha no puede ser mayor a la de hoy')
            return fecha
    
"""
        =========================================================
         SECCIÓN: CREAR EL FORMULARIO PostMascotaForm
         ---------------------------------------------------------
         TODO: Crear el formulario con los campos indicados
        =========================================================
"""