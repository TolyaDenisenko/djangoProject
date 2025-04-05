from cProfile import label

from django import forms

from .models import News
#класс модели формы
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows' : 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }















    # title = forms.CharField(max_length=150, label='Название',widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label='Текст:',required=False, widget=forms.Textarea(attrs={
    #     "class": "form-control",
    #     "rows":5
    # }))
    # is_published = forms.BooleanField(label='Опубликовано', initial=True)
    # category = forms.ModelChoiceField(label='Категория',queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}),empty_label="Выберите категорию")
