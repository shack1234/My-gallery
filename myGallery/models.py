from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null='True', blank=True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null='True', blank=True)
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()   

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
    
    @classmethod
    def all_pics(cls):
        pics = cls.objects.all()
        return pics 

    @classmethod
    def pic_locations(cls):
        pics = cls.objects.order_by('location')
        return pics 
    
    @classmethod
    def pic_categories(cls):
        pics = cls.objects.order_by('category')
        return pics 

    @classmethod
    def get_pic(cls, id):
        pic = cls.objects.get(id=id)
        return pic
  
    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images       
    
    @classmethod
    def get_image_by_id(cls,search_term):
        image = cls.objects.filter(id__icontains=search_term)
        return image
    
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(name=location).all()
        return image_location

# creating a model for the location of the photo
class Location(models.Model):
    
    name = models.CharField(max_length=20) 
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    def delete_location(self):
        Location.objects.filter(id = self.pk).delete()
    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

# creating a model for category
class Category(models.Model):
    
    name = models.CharField(max_length=15) 

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()    

    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()
    