from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    slug = models.SlugField(max_length=255, db_index=True, unique=True)        

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.title



class Equipment(models.Model):
    tags = TaggableManager(verbose_name='теги')

    title = models.CharField(max_length=255, verbose_name='название')
    place = models.CharField(max_length=255, blank=True, verbose_name='место установки')
    description = models.TextField(blank=True, verbose_name='описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления') 
    slug = models.SlugField(max_length=255, db_index=True, unique=True)     
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='equip', verbose_name='категория')
    
    class Meta:
        verbose_name = 'Оборудование' 
        verbose_name_plural = 'Оборудование' 
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def __str__(self):
        return self.title     
    
    def get_absolute_url(self):
        return reverse('equipment', kwargs={'equipment_slug':self.slug})
    

