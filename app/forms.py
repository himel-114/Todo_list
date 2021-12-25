from django.forms import ModelForm, fields, models


from app.models import TODO
class TODOForm(ModelForm):
    class Meta:
        model=TODO
        fields=['title','status','priority']