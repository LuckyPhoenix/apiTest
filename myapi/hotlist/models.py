from django.db import models

# Create your models here.

class Website(models.Model):
    CreateTime = models.CharField(u'时间',max_length=50)
    Desc = models.CharField(u"描述",max_length=50)
    Title = models.CharField(u'标题',max_length=50)
    Url = models.CharField(u'链接', max_length=50)
    approvalNum = models.CharField(u'点赞', max_length=50)
    commentNum = models.CharField(u'评论', max_length=50)
    hotDesc = models.CharField(u'热评', max_length=50)
    idWeb = models.CharField(u'编号', max_length=50)
    imgUrl = models.CharField(u'图片', max_length=50)

    def __str__(self):
        return self.Title
