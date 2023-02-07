from django.db import models

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
		category = models.CharField(max_length=3, blank=False, null=False, choices=CATEGORY_CHOICES, default='U')
		detail = models.CharField(null=True, blank=True, max_length=50)
		location = models.CharField(null=True, blank=True, max_length=50)
		status = models.CharField(max_length=3, blank=False, null=False, choices=STATUS_CHOICES, default='T')
		time = models.DateTimeField(null=True, blank=True)
		tag = models.CharField(null=True, blank=True, max_length=30)
		
		class Meta:
			verbose_name = 'Event'

		def __str__(self):
			return "<{}, {}>".format(
					self.category,
					self.detail[:20],
					)
