from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from showcase.settings import SHOWCASE_UPLOAD_TO
from django.utils import timezone

class ServicesEntry(models.Model):
	title = models.CharField(
			_('Services Title'), max_length=255)

	content = RichTextField()

class Subject(models.Model):
	title = models.CharField(
			_('Subjet Title'), max_length=255)	

class TeachingEntry(models.Model):
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

	title = models.CharField(
			_('Teaching Title'), max_length=255)

	content = RichTextField()

	tag = models.CharField(
			_('tag'), max_length=255)

	category = models.CharField(
			_('category'), max_length=255)


def image_upload_to_dispatcher(entry, filename):
    return entry.image_upload_to(filename)

class TechTools(models.Model):

	title = models.CharField(
			_('Image Title'), max_length=255)

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

class HomePageHeadings(models.Model):
	services_title = models.CharField(
			_('Services Title'), max_length=255)

	teaching_title = models.CharField(
			_('Teaching Title'), max_length=255)

	technologies_title = models.CharField(
			_('Technologies Title'), max_length=255)