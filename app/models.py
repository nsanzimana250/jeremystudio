from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True) 
    phone_number = models.CharField(max_length=15, blank=True, null=True)  
    message = models.TextField()

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    imagefile = models.ImageField(upload_to='images/')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
      
      
      
class Video(models.Model):
    name = models.CharField(max_length=100)
    videofile = models.FileField(upload_to='videos/')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name    
    

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class CustomerProduct(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='products')
    image_file = models.ImageField(upload_to='customer_products/')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.full_name} - {self.description}'

class customer_videos(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='videos')
    name = models.CharField(max_length=100)
    videofile = models.FileField(upload_to='customervideos/')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.full_name} - {self.name}'

