from rest_framework import serializers

from . import models


class smsonattenteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.smsonattente
        fields = [
            "last_updated",
            "next_date_send",
            "name",
            "id_pv",
            "created",
            "status",
        ]

class sys_paramtSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.sys_paramt
        fields = [
            "last_updated",
            "name",
            "created",
            "pr_value",
        ]

class smstosendSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.smstosend
        fields = [
            "status",
            "num_phone",
            "last_updated",
            "body_sms",
            "created",
            "id_pv",
            "name",
        ]
