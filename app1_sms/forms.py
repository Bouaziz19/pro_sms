from django import forms
from . import models


class smsonattenteForm(forms.ModelForm):
    class Meta:
        model = models.smsonattente
        fields = [
            "next_date_send",
            "name",
            "id_pv",
            "status",
        ]


class sys_paramtForm(forms.ModelForm):
    class Meta:
        model = models.sys_paramt
        fields = [
            "name",
            "pr_value",
        ]


class smstosendForm(forms.ModelForm):
    class Meta:
        model = models.smstosend
        fields = [
            "status",
            "num_phone",
            "body_sms",
            "id_pv",
            "name",
        ]
