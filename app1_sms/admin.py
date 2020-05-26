from django.contrib import admin
from django import forms

from . import models


class smsonattenteAdminForm(forms.ModelForm):

    class Meta:
        model = models.smsonattente
        fields = "__all__"


class smsonattenteAdmin(admin.ModelAdmin):
    form = smsonattenteAdminForm
    list_display = [
        "last_updated",
        "next_date_send",
        "name",
        "id_pv",
        "created",
        "status",
    ]
    readonly_fields = [
        "last_updated",
        "next_date_send",
        "name",
        "id_pv",
        "created",
        "status",
    ]


class sys_paramtAdminForm(forms.ModelForm):

    class Meta:
        model = models.sys_paramt
        fields = "__all__"


class sys_paramtAdmin(admin.ModelAdmin):
    form = sys_paramtAdminForm
    list_display = [
        "last_updated",
        "name",
        "created",
        "pr_value",
    ]
    readonly_fields = [
        "last_updated",
        "name",
        "created",
        "pr_value",
    ]


class smstosendAdminForm(forms.ModelForm):

    class Meta:
        model = models.smstosend
        fields = "__all__"


class smstosendAdmin(admin.ModelAdmin):
    form = smstosendAdminForm
    list_display = [
        "status",
        "num_phone",
        "last_updated",
        "body_sms",
        "created",
        "id_pv",
        "name",
    ]
    readonly_fields = [
        "status",
        "num_phone",
        "last_updated",
        "body_sms",
        "created",
        "id_pv",
        "name",
    ]


admin.site.register(models.smsonattente, smsonattenteAdmin)
admin.site.register(models.sys_paramt, sys_paramtAdmin)
admin.site.register(models.smstosend, smstosendAdmin)
