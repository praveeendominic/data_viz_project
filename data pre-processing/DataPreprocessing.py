
import zipfile
import glob
import os, shutil
import time
import zlib, sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

print('*****************Removal of Incremental and Data files in Destination folder starts*************************')
if os.path.exists("E:\\PythonWorkspace\\PycharmDataViz\\master.csv"):
    os.remove("E:\\PythonWorkspace\\PycharmDataViz\\master.csv")
else:
    print("The file does not exist")

if os.path.exists("E:\\PythonWorkspace\\PycharmDataViz\\Fin US Monthly Air Passengers.csv"):
    os.remove("E:\\PythonWorkspace\\PycharmDataViz\\Fin US Monthly Air Passengers.csv")
else:
    print("The file does not exist")

print('*****************Selenium Script to scrap the webpage and download 2021 data*************************')
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.transtats.bts.gov/DL_SelectFields.asp?gnoyr_VQ=FMF")
print(driver.title)
driver.find_element_by_xpath("//input[@value='All']").click()
driver.find_element_by_xpath("//select[@name='XYEAR']/option[text()='2021']").click()
driver.find_element_by_xpath("//BUTTON[@class='tsbutton' and @name='Download']").click()


print('**************Waiting for files to download*************************')
time.sleep(90)


print('****************checking list of Zip files in the destination folder*****************')
# check for the latest file in the folder
list_of_files = glob.glob('C:\\Users\\niran\\Downloads\\*ALL_CARRIER.zip')
latest_file = max(list_of_files, key=os.path.getctime, default=0)
print(latest_file)

print('***************Extraction of the latest zipped file *****************************')
# Extraction of the zip file.
with zipfile.ZipFile(latest_file, 'r') as zip_ref:
    zip_ref.extractall('C:\\Users\\niran\\Downloads\\unzipped\\')

print('***************Renaming of the zipped file to master.csv*****************************')
for filename in os.listdir('C:\\Users\\niran\\Downloads\\unzipped'):
    if filename.endswith(".csv"):
        os.rename(
            *(os.path.join('C:\\Users\\niran\\Downloads\\unzipped', filename) for filename in (filename, 'master.csv')))

print('***************Moving of file to project folder *****************************')
# Move a file from one folder to another:
shutil.move('C:\\Users\\niran\\Downloads\\unzipped\\master.csv', 'E:\\PythonWorkspace\\PycharmDataViz\\master.csv')

print('***********************Removal of root folder in destination to avoid file Already exists error*******************')
# Remove file in destination:
folder = 'C:/Users/niran/Downloads'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

print('***********************File upload to google drive starts here ********************')

# Authenticating google drive using Pydrive module
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

print('**********************Downloading master file from Google Drive*********************')
fileDownloaded = drive.CreateFile({'id': '1eWdjkpI637y-yhDk7FAFcLND9nM6RlGH'})
fileDownloaded.GetContentFile('Fin US Monthly Air Passengers.csv', mimetype='application/zip')


print('***********************Preprocessing and merging of latest data into Data file***********************************')
import pandas as pd

print('************************Reading data file and loading it to a dataframe******************************************')
drive_df = pd.read_csv('Fin US Monthly Air Passengers.csv')
print(drive_df.count())
print(drive_df.columns.values.tolist())

print('***********************Reading incremental file and loading it to a dataframe************************************')
delta_df_org = pd.read_csv('E:\\PythonWorkspace\\PycharmDataViz\\master.csv')
print(delta_df_org.count())
delta_df = delta_df_org[
    ["PASSENGERS", "AIRLINE_ID", "CARRIER_NAME", "ORIGIN", "ORIGIN_CITY_NAME", "ORIGIN_STATE_ABR", "ORIGIN_STATE_NM",
     "ORIGIN_COUNTRY", "ORIGIN_COUNTRY_NAME", "DEST", "DEST_CITY_NAME", "DEST_STATE_ABR", "DEST_STATE_NM",
     "DEST_COUNTRY", "DEST_COUNTRY_NAME", "YEAR", "MONTH"]].copy()
delta_df.rename(columns={'PASSENGERS': 'Sum_PASSENGERS'}, inplace=True)
print(delta_df.columns.tolist())

print('***********************Concatinating Incremental data into csv file************************************')
final_df = pd.concat([drive_df, delta_df])
rslt_df = final_df.loc[
    final_df['ORIGIN_COUNTRY_NAME'].str.contains('United States') & final_df['DEST_COUNTRY'].str.contains('US')]
print(rslt_df.count())
rslt_df.to_csv('Fin US Monthly Air Passengers.csv', index=False)


print('***********************Uploading the concatenated file into Google drive folder*************************')
file1 = drive.CreateFile({"mimeType": "text/csv"})
file1.SetContentFile("Fin US Monthly Air Passengers.csv")
file1.Upload()





