from django import forms
from .models import *

from crispy_forms.helper import  FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class MovieForm(forms.ModelForm):

    title = forms.CharField(label="Tytuł filmu",
                            widget=forms.TextInput(attrs={"placeholder":"Wprowadź tytuł filmu"}) )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('title', css_class="form-group col-md-6"),
                Column('released', css_class="form-group col-md-6"),
                css_class="form-row"
            ),

            Row(
                Column('description', css_class="form-group col-md-12"),
                css_class="form-row"
            ),

            Row(
                Column('imdb', css_class="form-group col-md-3"),
                Column('mpaa_rating', css_class="form-group col-md-3"),
                Column('trailer', css_class="form-group col-md-3"),
                Column('poster', css_class="form-group col-md-3"),
                css_class="form-row"
            ),
            Submit('submit', "Zapisz")

        )

    class Meta:
        model = Movie
        #fields = "__all__"
        exclude = ("created_by", )