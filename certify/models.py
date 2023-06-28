from django.db import models
import uuid
# Create your models here.


class Captcha(models.Model):
	id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	value=models.CharField(max_length=30)
	image=models.ImageField(upload_to="captcha")

	def __str__(self):
		return 'Captcha {} with value - {}'.format(self.id, self.value)
