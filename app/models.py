from django.db import models


class Product(models.Model):
	title = models.CharField(
		'Название',
		max_length=2048,
	)
	price = models.PositiveIntegerField(
		'Цена'
	)
	color = models.CharField(
		'Цвет',
		max_length=2048,
		blank=True,
		null=True
	)
	description = models.TextField(
		'Описание',
		blank=True,
		null=True
	)
	
