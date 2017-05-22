import xlrd
import MySQLdb

# open book 
book = xlrd.open_workbook("G:/AreaData.xls")
sheet = book.sheet_by_name("SUBDIV_Data")

#Connect with database 
database = MySQLdb.connect (host="localhost", user = "root", passwd = "vaibhav", db = "save")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

query = """INSERT INTO Regdata (regid,SD_Name,YEAR, JAN, FEB, MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEM,ANNUAL,JAN_FEB,Mar_May,Jun_Sep, OCT_Dem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"""

for r in range(1, sheet.nrows):
      regid     = sheet.cell(r,).value
      SD_Name = sheet.cell(r,1).value
      YEAR = sheet.cell(r,2).value
      JAN        = sheet.cell(r,3).value
      FEB     = sheet.cell(r,4).value
      MAR       = sheet.cell(r,5).value
      APR = sheet.cell(r,6).value
      MAY        = sheet.cell(r,7).value
      JUN       = sheet.cell(r,8).value
      JUL    = sheet.cell(r,9).value
      AUG        = sheet.cell(r,10).value
      SEP        = sheet.cell(r,11).value
      OCT          = sheet.cell(r,12).value
      NOV   = sheet.cell(r,13).value
      DEM   = sheet.cell(r,14).value
      ANNUAL = sheet.cell(r,15).value
      JAN_FEB   = sheet.cell(r,16).value
      Mar_May  = sheet.cell(r,17).value
      Jun_Sep = sheet.cell(r,18).value
      Oct_Dem   = sheet.cell(r,19).value


# Assign values from each row
      values = (regid,SD_Name,YEAR, JAN, FEB, MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEM,ANNUAL,JAN_FEB,Mar_May,Jun_Sep, OCT_Dem)

      # Execute sql Query
      cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ""
print "All Done! Bye, for now."
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)
#print "I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!"
