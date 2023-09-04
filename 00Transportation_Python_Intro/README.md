# Python Tutorial

## Instructions:
  1. You can either use Google Colab or your own Jupyter Notebook if you have Anaconda Python installed and downloaded on your local machine. You can go to this website to download **Anaconda: [link](https://www.anaconda.com/download)** If not, you will have to download this entire folder which contains all the datasets you will be working on with the Python stuff I organized. Make sure to name your folder **00Transportation_Python_Intro** if you are going to download this folder onto your local Google Drive account. When mounting this folder into Google drive, be sure to rename your file path as the following:

         path = '/content/drive/MyDrive/00Transportation_Python_Intro/datasets/
         import numpy as np  IMPORTANT IF YOU WANT TO USE GOOGLE COLAB
         import pandas as pd 
         from google.colab import drive
         drive.mount('/content/drive')
         path = '/content/drive/MyDrive/03ITE_Python/datasets/'
         students = path + 'students.csv'
         df = pd.read_csv(students)
         df.head()

      If you are going to use the Jupyter notebook on your local machine, then ignore the mounting the Google drive process. All you got to do is copy the following        code into your terminal:
  
         df = pd.read_csv('datasets/students.csv')
  
  3. Fill out the **00Louis_Python_Notes_Blank** and **01Louis_Python_Continued_Blank** while you follow the tutorial video I will attach here: 
