from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Event(models.Model):
		"""
		Class definition of Event
		"""
		CATEGORY_CHOICES = [
				('A', 'Anniversary'),
				('B', 'Birthday'),
				('P', 'Package'),
				('U', 'Undefined'),
		]
		STATUS_CHOICES = [
				('T', 'TODO'),
				('I', 'IN PROGRESS'),
				('D', 'DONE'),
		]
		title = models.CharField(null=False, blank=False, max_length=50, default='Undefined Event')
		detail = models.CharField(null=True, blank=True, max_length=200)
		category = models.CharField(max_length=3, blank=False, null=False, choices=CATEGORY_CHOICES, default='U')
		status = models.CharField(max_length=3, blank=False, null=False, choices=STATUS_CHOICES, default='T')
		location = models.CharField(null=True, blank=True, max_length=50)
		deadline = models.DateTimeField(null=True, blank=True)
		reporter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='reporter')
		assignee = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='assignee')
		created_time = models.DateTimeField(default=datetime.now)
		closed_time = models.DateTimeField(null=True, blank=True)
		last_update_time = models.DateTimeField(null=True, blank=True)
		tag = models.CharField(null=True, blank=True, max_length=30)

		def save(self, *args, **kwargs):
			"""
			Override the default save method, Set the last updated time as the timestamp when the instance saved
			"""
			self.last_update_time = datetime.now()
			super(Event, self).save(*args, **kwargs)

		class Meta:
			verbose_name = 'Event'

		def __str__(self):
			return "<{}, {}, {}>".format(
					self.get_status_display(),
					self.get_category_display(),
					self.title[:20],
					)
