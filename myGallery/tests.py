from django.test import TestCase
from .models import Image,Location,Category


# Create your tests here.
class ImageTestClass(TestCase):
    
    def setUp(self):
        self.location = Location(name = 'Madaraka')
        self.location.save_location()
        
        self.category = Category(name = 'nature')
        self.category.save_category()
        
        self.myImage = Image(id= 5, name = 'test', description = 'cool pic',location=self.location,category=self.category)
        self.myImage.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.myImage, Image))
    
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_save_method(self):
        self.myImage.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 

    def test_delete_image(self):
        self.myImage.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)
        
  
# test for the location of the photo

class LocationTestClass(TestCase):    
    def setUp(self):
        self.locName = Location(name = 'Madaraka')

    def test_instance(self):
        self.assertTrue(isinstance(self.locName, Location))

    def test_save_method(self):
        self.locName.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.new_location = Location(name = 'Canaan')
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)



class CategoryTestClass(TestCase):
    def setUp(self):
        self.nature = Category(name = 'nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.nature, Category))

    def test_save_method(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)        

    def test_delete_method(self):
        self.new_category = Category(name = 'autumn')
        self.new_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)  