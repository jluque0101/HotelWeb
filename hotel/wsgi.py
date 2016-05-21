import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "hotel.settings.development")

wsgi_application = get_wsgi_application()
application = DjangoWhiteNoise(wsgi_application)
