"""
    Title: models
    Notes:
        - Description: script to create main functions (models) for web app
        - Updated: 2022-12-23
        - Updated by: dcr
"""
from django.db import models # to create models
import pandas as pd # to manage dataframes
import os # to manage paths


# Create models
class Dictionary(models.Model):
    """
        Name: Dictionary
        Description: Initializes the dictionary table in the database.
        Dependencies:
            - django.db.models
    """
    Word = models.CharField(max_length=100) # create Word column and set max length of characters to 100 characters
    Score = models.IntegerField(max_length=100) # create Score column
    class Meta:
        db_table = "dictionary" # call the database table dictionary
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