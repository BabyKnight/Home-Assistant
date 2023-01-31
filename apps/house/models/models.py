from django.db import models

class House(models.Model):
		"""
		Class definition of House
		"""
		name = models.CharField(max_length=30, blank=False, null=False)

		class Meta:
			verbose_name = 'House'

		def __str__(self):
			return "< {} >".format(self.name.capitalize())


class Room(models.Model):
		"""
		Class definition of Room
		"""
		name = models.CharField(max_length=30, blank=False, null=False)

		class Meta:
			verbose_name = 'Room'

		def __str__(self):
			return "< {} >".format(self.name.capitalize())


class Device(models.Model):
		"""
		Class definition of Device
		"""
		name = models.CharField(max_length=30, blank=False, null=False)

		class Meta:
			verbose_name = 'Device'

		def __str__(self):
			return "< {} >".format(self.name.capitalize())
