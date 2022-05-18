from rest_framework import serializers
from .models import Website

class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Website
        fields = ('CreateTime','Desc','Title','Url','approvalNum','commentNum','hotDesc','idWeb','imgUrl')