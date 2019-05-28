import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mental.settings")

import django
django.setup()
from django.conf import settings


class LogHandleClass:
    def __init__(self,filename,level):
        pass
