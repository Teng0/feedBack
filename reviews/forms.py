from django import forms
from django.db.models.base import Model
from django.forms import fields
from django.forms.widgets import Textarea
from .models import Reviews
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name",max_length=30,error_messages={
#         'required':"შენი სახელი არ შეიძლება იყოს ცარიელი",
#         'min_length':"saxeli unda Sheicavdes minimum 8 simbolos",     
#     })
#     review_text = forms.CharField(label="Your FeedBack",widget=forms.Textarea,max_length=50)
#     rating = forms.IntegerField(label="Your taring",min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields ='__all__'
        exclude= ["id"]
        labels= {
            "user_name":"Your review",
            "review_text":"Your Text",
            "rating":"rating"
        }
        error_messages= {
            'user_name':{
                 'required':"შენი სახელი არ შეიძლება იყოს ცარიელი",
                 'min_length':"saxeli unda Sheicavdes minimum 8 simbolos",
            },
        }

