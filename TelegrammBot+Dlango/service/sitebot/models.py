from django.db import models

class ListCommand(models.Model):
    title = models.CharField(max_length=30, verbose_name='Список команд')
    content = models.TextField(verbose_name='Сообщение от бота', null=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Команды'
        verbose_name_plural = 'Команды'
    

class TgUser(models.Model):
    id_tg_user = models.BigIntegerField(unique=True, verbose_name='Пользователь TG')
    first_name = models.CharField(max_length=50, verbose_name='Фамилия', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Имя', null=True, blank=True)
    user_name = models.CharField(max_length=50, verbose_name='Логин', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}'
    
    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
    
class MessageUser(models.Model):
    command = models.ForeignKey(ListCommand, on_delete=models.CASCADE, verbose_name='Сообщение от пользователя', null=True)
    author = models.ForeignKey(TgUser, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    text = models.TextField(verbose_name='Текст комментария', null=True)
    create_data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)

    def __str__(self):
        return f'{self.author}'
    
    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'
