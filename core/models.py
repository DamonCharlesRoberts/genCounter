from django.db import models
import pandas as pd
import os
# Create your models here.
class Dictionary(models.Model):
    Word = models.CharField(max_length=100)
    Score = models.IntegerField(max_length=100)
    class Meta:
        db_table = "dictionary"
#class Document(models.Model):
#    description = models.CharField(max_length=255, blank=True)
#    document = models.FileField(upload_to='documents/')
#    uploaded_at = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    file=models.FileField(upload_to='documents/')
    #dict = Dictionary.get.objects.all()
    def FileName(self):
        return os.path.basename(self.file.name)
#
#    def __str__(self):
#        return self.fileName()
#    
    def Clean(self, string):
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in string:
            if ele in punc:
                string = string.replace(ele, "")
        return string

    def WordCount(self):
        p = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        with open(self.file.path) as file:
            for line in file:
                str=line.split()
        for ele in str:
            if ele in p:
                str=str.replace(ele, "")
        return len(str)
    
    def Score(self, dict):
        with open(self.file.path) as file:
            for line in file:
                String=line.lower().split()
            cleaned = [self.Clean(i) for i in String]
        Words = list(dict["Word"])
        matches=list()
        score=0
        for d in Words:
            for e in cleaned:
                if d==e:
                    matches.append(d)
        if len(matches)>=1:
                #score+=dict[dict["Word"].isin(matches).iloc[0]["Score"]]
                score+=1
        else:
            score
        return score