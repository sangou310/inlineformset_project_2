from django import forms

from .models import JutyuHead, JutyuDetail


class JutyuCreateForm(forms.ModelForm):
    class Meta:
        model = JutyuHead
        fields = ['jutyu_date', 'customer']


class JutyuDetailForm(forms.ModelForm):
    class Meta:
        model = JutyuDetail
        fields = ['part', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


JutyuDetailFormset = forms.inlineformset_factory(
    JutyuHead, JutyuDetail,
    form=JutyuDetailForm,
    extra=1,
)
