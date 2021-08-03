from django.forms import ModelForm
from . models import MaternalRecord


class MaternalRecordForm(ModelForm):
    class Meta:
        model = MaternalRecord
        fields = '__all__'

