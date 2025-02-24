from django import forms
from . models import MarvelModel,DcModel

# class MarvelForm(forms.Form):
#     name = forms.CharField()
#     heroic_name = forms.CharField()


class MarvelForm(forms.ModelForm):

    class Meta:
        model = MarvelModel
        # fields='__all__'
        fields=['name','heroic_name']
        
        # labels ={
        #     'name':'Full Name'
        # }

        # error_messages={
        #     'name':{'required':'Please enter Name properly'},
        #     'heroic_name':{'required':'Please enter Heoric Name properly'}
        # }
        # help_texts= {
        #     'name':'Enter the name'
        # }

        # widgets={
        #     'name':forms.PasswordInput,
        #     'heroic_name':forms.TextInput(attrs={'class':'form-control'})
        # }

class DcForm(forms.ModelForm):

    class Meta:
        model = DcModel
        fields=['name','heroic_name']