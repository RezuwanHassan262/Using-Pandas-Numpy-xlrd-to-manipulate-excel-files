# -*- coding: utf-8 -*-
"""4. Combining all the sheets datas in one single sheet

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gzu5RUAPJS9_Y1QryaqvE926WaXRInYC
"""

# Code to read csv file into colaboratory:
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

downloaded = drive.CreateFile({'id':'1QON0M2gj698LM8hIU3n-OaM-8nTRfD0W'}) # replace the id with id of file you want to access
downloaded.GetContentFile('ca.xlsx')

import pandas as pd
path0 = "ca.xlsx"
path1 = "SampleData.xlsx"
path2 = "SampleData4.xlsx"

df0 = pd.read_excel(path0, sheet_name = None)
df1 = pd.read_excel(path1)
df2 = pd.read_excel(path2)

cdf = pd.concat(df0, sort = False)
writer = pd.ExcelWriter("New_output.xlsx")
cdf.to_excel(writer)
writer.save()

