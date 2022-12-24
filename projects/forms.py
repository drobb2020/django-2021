from django.forms import ModelForm

from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'live_link', 'code_link', 'tags']
