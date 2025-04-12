from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import DepartmentEvent, DepartmentEventType, DepartmentEventName, DepartmentEventLocation
from accounts.models import Profile

class DepartmentEventForm(forms.ModelForm):
    class Meta:
        model = DepartmentEvent
        fields = ['datetime', 'type', 'name', 'location', 'description', 'staff']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'staff': CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        department = user.profile.podrazdelenie
        self.fields['type'].queryset = DepartmentEventType.objects.filter(department=department)
        self.fields['type'].empty_label = "Выбери тип"
        self.fields['name'].queryset = DepartmentEventName.objects.filter(department=department)
        self.fields['name'].empty_label = "Выбери название"
        self.fields['location'].queryset = DepartmentEventLocation.objects.filter(department=department)
        self.fields['location'].empty_label = "Выбери место"
        self.fields['staff'].queryset = Profile.objects.filter(podrazdelenie=department)
        self.fields['staff'].label_from_instance = lambda obj: f"{obj.last_name} {obj.first_name[0]}."

        self.fields['description'].widget.attrs['placeholder'] = 'Добавь описание'

        for field_name in self.fields:
            if field_name != 'staff':
                self.fields[field_name].widget.attrs['class'] = 'form-control'

        self.fields['staff'].widget.attrs['class'] = 'form-check-input'
