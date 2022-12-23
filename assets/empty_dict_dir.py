"""
    Title: empty the dictionary directory
    Notes:
        - Description: Scheduled script to delete the contents in the dictionary directory daily.
        - Updated: 2022-12-23
        - Updated by: dcr
"""

from os import remove # for removing files
from glob import glob # for path management

files = glob.glob("/home/damoncroberts/gencounter/media/documents/")
for file in files:
    remove(file)
