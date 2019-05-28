import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mental.settings")

import django
django.setup()



from assetManagement import models as asset


if __name__ == '__main__':
    print(asset.Cproom.objects.get_queryset())

