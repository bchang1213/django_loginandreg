from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATE_STR_REGEX = re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$')
# Create your models here.

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
# VALIDATING THE FIRST NAME
		if len(postData['first_name']) == 0:
			errors['first_name']="Please enter your first name"
# VALIDATING LAST NAME
		if len(postData['last_name']) == 0:
			errors['last_name']="Please enter your last name"
# VALIDATING EMAIL
		if not EMAIL_REGEX.match(postData['email']):
			errors['email']="Please enter a valid email"

# VALIDATING BIRTHDAY
		if len(postData['dob']) == 0:
			errors['dob']= 'Please enter your date of birth.'
		elif not DATE_STR_REGEX.match(postData['dob']):
			errors['dob']= "Please use date picker."
		else:
			try:
				dob = datetime.datetime.strptime(postData['dob'], "%Y-%m-%d")
				cutoff_date = datetime.datetime.now() - datetime.timedelta(days=18*365)
				now = datetime.datetime.now()

				if dob > now:
					errors['doberror']="You cannot be born in the future."

				if dob > cutoff_date:
					errors['doberror1']="You must be 18 join this site."

			except Exception as date_error:
				print date_error
				errors['doberror2']='Please use the date picker.'

# VALIDATING PASSWORD
		if len(postData['password']) == 0:
			errors['password']="Please enter a password"
		else:
			if len(postData['password']) < 8:
				errors['password']= "Password must be at least 8 characters."

			if not any([letter.isupper() for letter in postData['password']]):
				errors['password1']= "Password must contain at least one uppercase letter."

			if not any([letter.isdigit() for letter in postData['password']]):
				errors['password2']= "Password must contain at least one number."

			if not any([letter in "!@#$%^&*()-_=+~`\"'<>,.?/:;\}{][|" for letter in postData['password']]):
				errors['password3']= "Password must contain at least one special character."

			if postData['password'] != postData['passconf']:
				errors['password4']= 'Password and confirmation fields must match.'

		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
	def __repr__(self):
		return ("<User object: id:{} {} {}>".format(self.id, self.name, self.email))