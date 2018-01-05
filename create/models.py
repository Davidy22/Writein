from django.db import models

# Create your models here.
class poll(models.Model):
	
	def __str__(self):
		return '{0}'.format(self.id)


#class bin(models.Model):
#	pollID = models.BigIntegerField(help_text="Poll ID")
#	binHead = models.CharField(max_length=140,help_text="Dominant identifier")
#	
#	def __str__(self):
#		return self.binHead

class entry(models.Model):
	pollID = models.ForeignKey('poll',to_field='id',on_delete=models.CASCADE)
	IP = models.GenericIPAddressField(protocol='both',unpack_ipv4=False,help_text="Recipient IP address")
	text = models.CharField(max_length=140,help_text="Poll entry")
	
	class Meta:
		unique_together = ('pollID', 'IP')
	
	def __str__(self):
		return self.text
