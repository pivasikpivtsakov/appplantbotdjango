from django.conf import settings

# secure root of our api
API_ROOT = f'{settings.HOSTNAME}/{settings.TG_API_TOKEN}'

TGBOTAPIURL = f'https://api.telegram.org/bot{settings.TG_API_TOKEN}'
