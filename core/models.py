from django.db import models
import pandas as pd
# Create your models here.
#class Document(models.Model):
#    description = models.CharField(max_length=255, blank=True)
#    document = models.FileField(upload_to='documents/')
#    uploaded_at = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    file=models.FileField(upload_to='documents/')
    fileName=models.CharField(max_length=50)

    def __str__(self):
        return self.fileName()
    
    def Clean(self):
        p = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        with open(self.files.path) as file:
            for line in file:
                str=line.split()
        for ele in string:
            if ele in p:
                string=string.replace(ele, "")
        return string

    def WordCount(self):
        return len(self.Clean())
    
    def Score(self):
        matches=list()
        score=0
        string=self.Clean()
        for d in Words:
            for e in String:
                if d==e:
                    matches.append(d)
        for i in matches:
            if len(dict[dict["Word"].isin(matches)].index)==1:
                score+=dict[dict["Word"].isin(matches).iloc[0]["Score"]]
            else:
                score
        return score