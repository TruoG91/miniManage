from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Apartment(models.Model):
	name = models.CharField(max_length=10)
	address = models.CharField(max_length=255)
	phone_no = models.CharField(max_length=12)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Apartment'
		verbose_name_plural = 'Apartments'

class Room(models.Model):
	room_choice = [('A', 'Type A'), ('B', 'Type B'), ('C', 'Type C')]
	room_no = models.CharField(max_length=3)
	room_type = models.CharField(choices=room_choice, max_length=1, default=room_choice[1])
	room_available_status = models.BooleanField(default=True) #True = available /False = unavailable
	apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='rooms')
	price = models.IntegerField(blank=True)

	class Meta:
		ordering = ('room_no',)
		verbose_name = 'Room'
		verbose_name_plural = 'Rooms'

	def __str__(self):
		return self.room_no

	def save(self, *args, **kwargs):
		if self.room_type == 'A':
			self.price = 1000000
		elif self.room_type == 'B':
			self.price = 1200000
		else:
			self.price = 1500000
		return super(Room, self).save(*args, **kwargs)


class Service(models.Model):
	name = models.CharField(max_length=50)
	price = models.IntegerField(blank=False)
	description = models.CharField(max_length=100, help_text='Mô tả trong 100 ký tự')

	class Meta:
		verbose_name = 'Service'
		verbose_name_plural = 'Services'


class Contract(Room):
	contract_choice = [('HĐ1T', '1 Month'), ('HĐ3T', '3 Months'), ('HĐ6T', '6 Months'), ('HĐ1N', '1 Year')]
	contract_type = models.CharField(choices=contract_choice, max_length=4, default=contract_choice[1])
	contract_no = models.CharField(max_length=10)
	contract_started_at = models.DateTimeField(auto_now_add=True)
	contract_end_at = models.DateTimeField(null=True)
	services = models.ManyToManyField(Service, related_name='contracts')
	
	def __str__(self):
		return self.contract_no

	class Meta:
		verbose_name = 'Contract'
		verbose_name_plural = 'Contracts'


class ElectricNumber(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	electric_number = models.IntegerField(blank=True,
										validators=[MinValueValidator(0),
													MaxValueValidator(99999)
										]
	)
	room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='electric_numbers')

	def __str__(self):
		return "{} {}".format(self.room.room_no, self.electric_number)

	class Meta:
		verbose_name = 'ElectricNumber'
		verbose_name_plural = 'ElectricNumbers'

