# Unzip the dataset

# !pip install patool

from patoolib import extract_archive
import os

zipfile = 'dataset.rar'

extract_to = 'hoda'

os.mkdir(extract_to) 

extract_archive(zipfile, outdir=extract_to)