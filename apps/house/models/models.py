from django.db import models

class House(models.Model):
		"""
		Class definition of House
		"""
		address = models.CharField(max_length=200, null=False, blank=False, unique=True) 
		name = models.CharField(max_length=20, blank=True, null=True, unique=True)
		zip_code = models.CharField(max_length=9, null=True, blank=True)
		total_area = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
		floor_plan = models.CharField(max_length=255, null=True, blank=True)

		class Meta:
			verbose_name = 'House'

		def __str__(self):
			return "< {}, {}, {}... >".format(
					self.id,
					"HOUSE {}".format(self.id) if self.name is None else self.name.capitalize(),
					self.address[:20]
					)


class Room(models.Model):
		"""
		Class definition of Room
		"""
		house = models.ForeignKey(House, on_delete=models.CASCADE, blank=False, null=True, related_name='room')
		name = models.CharField(max_length=30, blank=False, null=False)
		total_area = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
		#owner = 

		class Meta:
			verbose_name = 'Room'

		def __str__(self):
			return "< {}, {} >".format(
					self.name.capitalize(),
					"House {}".format(self.house.id) if self.house.name is None else self.house.name.capitalize()
					)


class Device(models.Model):
		"""
		Class definition of Device
		"""
		room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
		name = models.CharField(max_length=30, blank=False, null=False, unique=True)
		#owner = 
		mac_address = models.CharField(max_length=16, blank=True, null=True)
		status = models.CharField(max_length=20, blank=True, null=True)

		class Meta:
			verbose_name = 'Device'

		def __str__(self):
			return "< {} ({}, {}) >".format(
					self.name.capitalize(),
					self.room.name.capitalize(),
					"House {}".format(self.room.house.id) if self.room.house.name is None else self.room.house.name.capitalize()
					)
