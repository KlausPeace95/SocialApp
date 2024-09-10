
from django import forms
from .models import Posts
from django.contrib.auth.forms import UserCreationForm

class PostsForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
          attrs={
              "placeholder": "Post Something... (Maximum of 2000 Characters)",
              "class": "textarea is-info is-medium",
          }
        ),
        label="",
    )

    class Meta:
        model = Posts
        exclude = ("user", )

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)