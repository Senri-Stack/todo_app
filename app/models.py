from django.db import models

class Todo(models.Model):
    task =  models.CharField(
            verbose_name='タスク',
            max_length=40,
        )

    start_day = models.DateField(
            verbose_name='開始日',
            default=None,
            null=True,
        )

    end_day = models.DateField(
            verbose_name='終了日',
            default=None,
            null=True,
        )

    start_time = models.TimeField(
            verbose_name='開始時間',
            default=None,
            null=True,
        )

    end_time = models.TimeField(
            verbose_name='終了時間',
            default=None,
            null=True,
        )

    CATEGORY_CHOICES = [
        ('PR','Private'),
        ('ST','Study'),
        ('WR','Work'),
    ]
    category = models.CharField(
        verbose_name = 'カテゴリ',
        max_length=2,
        choices=CATEGORY_CHOICES,
        default='PR',
    )

    completed = models.BooleanField(default=False)

    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'タスク'
        verbose_name_plural = 'タスク'