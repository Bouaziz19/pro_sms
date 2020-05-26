import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from app1_sms import models as app1_sms_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_app1_sms_smsonattente(**kwargs):
    defaults = {}
    defaults["next_date_send"] = datetime.now()
    defaults["name"] = ""
    defaults["id_pv"] = ""
    defaults["status"] = ""
    defaults.update(**kwargs)
    return app1_sms_models.smsonattente.objects.create(**defaults)
def create_app1_sms_sys_paramt(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["pr_value"] = ""
    defaults["pr_name"] = ""
    defaults.update(**kwargs)
    return app1_sms_models.sys_paramt.objects.create(**defaults)
def create_app1_sms_smstosend(**kwargs):
    defaults = {}
    defaults["status"] = ""
    defaults["num_phone"] = ""
    defaults["body_sms"] = ""
    defaults["id_pv"] = ""
    defaults["name"] = ""
    defaults.update(**kwargs)
    return app1_sms_models.smstosend.objects.create(**defaults)
