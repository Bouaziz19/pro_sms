import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_smsonattente_list_view():
    instance1 = test_helpers.create_app1_sms_smsonattente()
    instance2 = test_helpers.create_app1_sms_smsonattente()
    client = Client()
    url = reverse("app1_sms_smsonattente_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_smsonattente_create_view():
    client = Client()
    url = reverse("app1_sms_smsonattente_create")
    data = {
        "next_date_send": datetime.now(),
        "name": "text",
        "id_pv": 1,
        "status": true,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_smsonattente_detail_view():
    client = Client()
    instance = test_helpers.create_app1_sms_smsonattente()
    url = reverse("app1_sms_smsonattente_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_smsonattente_update_view():
    client = Client()
    instance = test_helpers.create_app1_sms_smsonattente()
    url = reverse("app1_sms_smsonattente_update", args=[instance.pk, ])
    data = {
        "next_date_send": datetime.now(),
        "name": "text",
        "id_pv": 1,
        "status": true,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_sys_paramt_list_view():
    instance1 = test_helpers.create_app1_sms_sys_paramt()
    instance2 = test_helpers.create_app1_sms_sys_paramt()
    client = Client()
    url = reverse("app1_sms_sys_paramt_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_sys_paramt_create_view():
    client = Client()
    url = reverse("app1_sms_sys_paramt_create")
    data = {
        "name": "text",
        "pr_value": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_sys_paramt_detail_view():
    client = Client()
    instance = test_helpers.create_app1_sms_sys_paramt()
    url = reverse("app1_sms_sys_paramt_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_sys_paramt_update_view():
    client = Client()
    instance = test_helpers.create_app1_sms_sys_paramt()
    url = reverse("app1_sms_sys_paramt_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "pr_value": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_smstosend_list_view():
    instance1 = test_helpers.create_app1_sms_smstosend()
    instance2 = test_helpers.create_app1_sms_smstosend()
    client = Client()
    url = reverse("app1_sms_smstosend_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_smstosend_create_view():
    client = Client()
    url = reverse("app1_sms_smstosend_create")
    data = {
        "status": true,
        "num_phone": "text",
        "body_sms": "text",
        "id_pv": 1,
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_smstosend_detail_view():
    client = Client()
    instance = test_helpers.create_app1_sms_smstosend()
    url = reverse("app1_sms_smstosend_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_smstosend_update_view():
    client = Client()
    instance = test_helpers.create_app1_sms_smstosend()
    url = reverse("app1_sms_smstosend_update", args=[instance.pk, ])
    data = {
        "status": true,
        "num_phone": "text",
        "body_sms": "text",
        "id_pv": 1,
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
