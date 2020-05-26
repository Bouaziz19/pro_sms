from django.db import models
from django.urls import reverse


class smsonattente(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    next_date_send = models.DateField()
    name = models.CharField(max_length=60)
    id_pv = models.IntegerField()
    data = models.CharField(max_length=800,default="e")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("app1_sms_smsonattente_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("app1_sms_smsonattente_update", args=(self.pk,))


class sys_paramt(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    pr_value = models.CharField(max_length=100)
    # pr_name = models.CharField(max_length=60)
    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("app1_sms_sys_paramt_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("app1_sms_sys_paramt_update", args=(self.pk,))


class smstosend(models.Model):

    # Fields
    status = models.BooleanField(default=False)
    num_phone = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    body_sms = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id_pv = models.IntegerField()
    name = models.CharField(max_length=60)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("app1_sms_smstosend_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("app1_sms_smstosend_update", args=(self.pk,))
