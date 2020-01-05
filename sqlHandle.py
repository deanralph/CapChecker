# sqlHandle v1
# Dean Ralph
# Jan 2020

# Description:
# Designed to interface between python and MySQL
# Create a connection object in your main code by passing the appropiate
# creds and then use the pre-defined functions to manipulate the database

#Imports
import pymysql

#Main Code

class mySQL:

    def __init__(self, server, dbusername, dbpassword, dbname):
        self.con = pymysql.connect(host=f"{server}", user=f"{dbusername}", password=f"{dbpassword}", db=f"{dbname}")

    def AddBat(self, batMake, barcode):
        cur = self.con.cursor()
        cur.execute(f"INSERT INTO batteryChecker.batteryHeader (make, barcode, statusID) VALUE ('{batMake}','{barcode}','1');")
        return cur.fetchone()

    def GetBatData(self, barcode):    
        cur = self.con.cursor()
        cur.execute(f"SELECT batteryHeader.barcode, batteryHeader.make, batteryStatus.statusName FROM batteryChecker.batteryHeader INNER JOIN batteryStatus on batteryHeader.statusID=batteryStatus.statusID WHERE barcode = '{barcode}';")
        return cur.fetchone()

    def AddHoc(self, sqlCode):
        cur = self.con.cursor()
        cur.execute(sqlCode)
        return cur.fetchall()

    def GetVersion(self):
        cur = self.con.cursor()
        cur.execute("SELECT VERSION();")
        return cur.fetchone()