from django.db import models

class Company(models.Model):
    name = models.CharField(
        max_length=255,verbose_name='会社名',blank=False,null=False)
    image = models.ImageField(
        upload_to='images/',verbose_name='会社画像',blank=False,null=False,default='images/default.png')
    job_description = models.TextField(
        verbose_name='仕事内容',blank=False,null=False)
    strengths = models.CharField(max_length=255,blank=True,null=True,default="特になし",verbose_name='強み')
    location = models.CharField(max_length=255, blank=False, null=False, default="未定", verbose_name='勤務地')
    working_hours = models.CharField(max_length=255, blank=True, null=True, default="不明", verbose_name='勤務時間')
    salary = models.CharField(max_length=255, blank=True, null=True, default="要相談", verbose_name='給料')
    benefits = models.CharField(max_length=255, blank=True, null=True, default="特になし", verbose_name='福利厚生')
    annual_holidays = models.CharField(max_length=255, blank=True, null=True, default="未定", verbose_name='年間休日')
    hires = models.CharField(max_length=255, blank=True, null=True, default="不明", verbose_name='採用人数')
    selection_process = models.TextField(blank=True, null=True, default="選考フローは未定", verbose_name='選考フロー')
    notes = models.TextField(blank=True, null=True, default="特記事項なし", verbose_name='備考')

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title