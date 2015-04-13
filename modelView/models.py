from django.db import models
from django.contrib import admin

class Account(models.Model):
	username = models.CharField(max_length=50,null=True)
	password = models.CharField(max_length=50,null=True)
	firstname = models.CharField(max_length=150,null=True)
	lastname = models.CharField(max_length=50,null=True)
	company = models.CharField(max_length=100,null=True)
	address = models.CharField(max_length=100,null=True)


	# email    = models.EmailField(null=True)

	def __str__(self):
		return 'username:%s password:%s' % (self.username, self.password)	
	class Admin:
		pass
# put before download
class Media(models.Model):
	# filename length is large engough
	filename 	= models.CharField(max_length=150,null=True)
	# account  = models.ForeignKey(Account)
	username 	= models.CharField(max_length=50,null=True)
	type 	 	= models.CharField(max_length=50,null=True)
	path	 	= models.FileField(upload_to='static/media/%Y/%m/%d')
	IP 	     	= models.IPAddressField(null=True)
	uploadTime  = models.DateTimeField(auto_now_add=True, blank=True)
	meta 		= models.CharField(max_length=200,null=True)
	keyword 	= models.CharField(max_length=200,null=True)

	def __str__(self):
		return 'name:%s type:%s' % (self.path, self.type)	
	class Admin:
		pass

class Download(models.Model):
	IP 			 = models.IPAddressField(null=True)
	downloadTime = models.DateTimeField(null=True)
	# account 	 = models.ForeignKey(Account)
	username     = models.CharField(max_length=50,null=True)
	#may need change media to path of Media
	media 		 = models.ForeignKey(Media)
	
	def __str__(self):
		return self.IP
	class Admin:
		pass

# class Upload(models.Model):
# 	IP 		   = models.IPAddressField(null=True)
# 	uploadTime = models.DateTimeField(null=True)

# 	def __str__(self):
# 		return self.IP
# 	class Admin:
# 		pass
# admin.site.unregister(Account)
# admin.site.unregister(Media)
# admin.site.unregister(Download)

# class UploadFile(models.Model):
# 	# title = models.CharField(max_length=30,null=True)
# 	file = 
# 	type 
# 	def __str__(self):
# 		return 'name:%s type:%s' % (self.file.name, self.file.content_type)	
# 	class Admin:
# 		pass