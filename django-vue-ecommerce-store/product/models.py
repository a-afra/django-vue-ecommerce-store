from io import BytesIO
from PIL import Image

from django.db import models
from django.core.files import File


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=180)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=180)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'https://api-boutique.herokuapp.com' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'https://api-boutique.herokuapp.com' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'https://api-boutique.herokuapp.com' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image):
        img = Image.open(image)
        img.convert('RGB')
        width, height = img.size
        square_size = min(img.size)

        left = (width - square_size) // 2
        top = (height - square_size) // 2
        right = (width + square_size) // 2
        bottom = (height + square_size) // 2

        img = img.crop((left, top, right, bottom))

        img.thumbnail((480, 480))

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=95)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

