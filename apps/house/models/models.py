from django.db import models

class House(models.Model):
		"""
		Class definition of House
		"""
		name = models.CharField(max_length=30, blank=False, null=False)
		address = models.CharField(max_length=200, null=True, blank=False) 
		zip_code = models.CharField(max_length=15, null=True, blank=True)
		total_area = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
		floor_plan = models.CharField(max_length=300, null=True, blank=True)

		class Meta:
			verbose_name = 'House'

		def __str__(self):
			return "< {}, {}... >".format(self.name.capitalize(), self.address)


class Room(models.Model):
		"""
		Class definition of Room
		"""
		name = models.CharField(max_length=30, blank=False, null=False)
		total_area = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
		house = models.ForeignKey(House, on_delete=models.CASCADE, blank=False, null=True, related_name='room')
		#owner = 

		class Meta:
			verbose_name = 'Room'

		def __str__(self):
			return "< {}, {} >".format(self.name.capitalize(), self.house.name.capitalize())


class Device(models.Model):
		"""
		Class definition of Device
		"""
		name = models.CharField(max_length=30, blank=False, null=False)
		room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
		#owner = 
		mac_address = models.CharField(max_length=60, blank=True, null=True)
		status = models.CharField(max_length=20, blank=True, null=True)

		class Meta:
			verbose_name = 'Device'

		def __str__(self):
			return "< {} ({}, {}) >".format(
					self.name.capitalize(),
					self.room.name.capitalize(),
					self.room.house.name.capitalize()
					)
