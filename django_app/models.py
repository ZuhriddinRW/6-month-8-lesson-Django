from django.db import models


class Category ( models.Model ) :
    category_id = models.AutoField ( primary_key=True )
    category_name = models.CharField ( max_length=100 )
    description = models.TextField ( default='Default Description' )
    image = models.ImageField ( upload_to='photo/%Y/%m/%d', default='images/category.png' )

    def __str__(self) :
        return self.category_name

    class Meta :
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class News ( models.Model ) :
    title = models.CharField ( max_length=100, verbose_name='Title' )
    content = models.TextField ( verbose_name='Content' )
    created_at = models.DateTimeField ( auto_now_add=True, verbose_name='Add_date' )
    updated_at = models.DateTimeField ( auto_now=True )
    photo = models.ImageField ( upload_to='photo/%Y/%m/%d' )
    bool = models.BooleanField ( default=False, verbose_name='Bool' )
    category = models.ForeignKey ( Category, on_delete=models.CASCADE, default=1 )
    views = models.IntegerField ( default=0 )

    def __str__(self) :
        return self.title

    class Meta :
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['-created_at']