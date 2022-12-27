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
    """
        Name: Document
        Description: FileHandler. Produces the result page. Returns a FileName, Returns the WordCount, and Returns the Score
        Dependencies:
            - django.db.models
            - os.path.basename
            - pandas
    """
    file=models.FileField(upload_to='documents/') # put the uploaded files in the document folder

    def FileName(self):
        """
            Name: FileName
            Description: Returns the name of the uploaded file
            Dependencies:
                - os.path.basename
        """
        return os.path.basename(self.file.name) # take the file name and return it

    def Clean(self, string):
        """
            Name: Clean
            Description: Removes punctuation from the uploaded file
        """
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' # define punctuation to remove
        for ele in string: # for each character in the string
            if ele in punc: # if there are any of the punctuation in the characters 
                string = string.replace(ele, "") # then remove it and store it in string
        return string # return the stored clean string

    def WordCount(self):
        """
            Name: WordCount
            Description: Calculates the number of words present in the uploaded document
            Dependencies:
                - models.Clean
        """
        with open(self.file.path) as file: #open the file
            for line in file: # separate each line
                str=line.lower().split() # and for each line, convert characters to lower case and split them into words
            str = [self.Clean(i) for i in str] # then using models.Clean, remove the punctuation
        return len(str) # return the length of the cleaned list of words
    
    def Score(self, dict):
        """
            Name: Score
            Description: Calculates the score given by the gendered language dictionary based on words present in the document
            Dependencies:
                - models.clean
                - pandas
        """
        with open(self.file.path) as file: #open the file
            for line in file: # separate each line
                String=line.lower().split() # and for each line, convert characters to lower case and split them into words
            cleaned = [self.Clean(i) for i in String] # then using models.Clean, remove the punctuation
        Words = list(dict["Word"]) # grab the column of words from the passed dict object and turn a list of them
        matches=list() # intitialize an empty list object
        score=0 # start each analysis with a score of zerio
        for d in Words:
            for e in cleaned:
                if d==e:
                    matches.append(d) # if the words in the dictionary and the document match, put them in the matches list object
        if len(matches)>=1: # if there are 1 or more words listed in the matches column
                score+=dict[dict["Word"].isin(matches)].iloc[0]["Score"] #... then take the score for that corresponding word in the dictionary and add it to the score
        else:
            score # if the matches list is empty, then leave the score alone
        return score/self.WordCount() # return the score divided by the WordCount of the document to give an average score for the document.
