from django.db import models

class Article(models.Model):
	article_title = models.CharField('Названия статьи', max_length = 200 )
	article_text = models.TextField('Текст статьи')
	article_photo = models.ImageField('Фото статьи')
	pub_date = models.DateTimeField('дата публикации')

	def __str__(self):
		return self.article_title

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('Автор статьи', max_length = 50)
	commen_text = models.CharField("Текст статьи", max_length = 200)


	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Коментарии'