from django.conf import settings

SHOWCASE_UPLOAD_TO = getattr(settings, 'SHOWCASE_UPLOAD_TO', 'uploads/portfolio')