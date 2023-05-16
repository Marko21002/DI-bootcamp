from django import forms
from .models import Gif, Category


class GifForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all())

    class Meta:
        model = Gif
        fields = ['uploader_name', 'title', 'url', 'categories']

    categories = forms.ModelChoiceField(
        queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
# if i wanna use all fields = ('ß__all__')


class Likeform(forms.Form):

    like = forms.ModelChoiceField(queryset=Gif.objects.all())

    dislike = forms.ModelChoiceField(queryset=Gif.objects.all())
