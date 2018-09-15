from django.db import models
from django.utils.translation import ugettext_lazy as _
import os
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from showcase.settings import SHOWCASE_UPLOAD_TO
from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    content = RichTextField()



def image_upload_to_dispatcher(entry, filename):
    """
    Dispatch function to allow overriding of ``image_upload_to`` method.

    Outside the model for fixing an issue with Django's migrations on Python 2.
    """
    return entry.image_upload_to(filename)

class Portfolio(models.Model):    
    title = models.CharField(
        _('title'), max_length=255)

    slug = models.SlugField(
        _('slug'), unique=True, max_length=255,
        help_text=_("Used to build the category's URL."))

    # content = models.TextField(_('content'), blank=True)

    content = RichTextField()

    def image_upload_to(self, filename):
        now = timezone.now()
        filename, extension = os.path.splitext(filename)

        return os.path.join(
            SHOWCASE_UPLOAD_TO,
            now.strftime('%Y'),
            now.strftime('%m'),
            now.strftime('%d'),
            '%s%s' % (slugify(filename), extension))

    image = models.ImageField(
        _('image'), blank=True,
        upload_to=image_upload_to_dispatcher,
        help_text=_('Used for illustration.'))

    image_caption = models.TextField(
        _('caption'), blank=True,
        help_text=_("Image's caption."))

    github_link = models.CharField(
        _('Github url'), default='aurthurm/', blank=True, max_length=255,
        help_text=_('Github link as: username/repository'))

    creation_date = models.DateTimeField(
        _('creation date'),
        default=timezone.now)

    def get_absolute_url(self):
        return reverse('showcase:portfolio-detail', kwargs={'portfolio_id':self.pk, 'portfolio_slug':self.slug})

    def __str__(self):
        return self.title
