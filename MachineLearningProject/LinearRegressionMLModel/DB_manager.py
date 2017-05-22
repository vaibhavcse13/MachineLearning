import pymysql 

class DatabaseUtility : 
    
    def __init__(self):
        self.con = pymysql.connect("localhost", "root","vaibhav" , "save2")
        self.cur = self.con.cursor()
    
    def Calculation(self, state, year, area):
        self.cur.execute(("Select Annual_Rain from %s where Year = %s " )%(state,year))
        row = self.cur.fetchone()
        rain = float(row[0])
        water_saved = area * (rain / 25.4) * 0.623 * 3.7
        return water_saved
    
    def ShowAnalysis(self, state,flag):
        self.cur.execute(("Select * from metric where state = '%s' && junsep=%s")%(state,flag))
        row = self.cur.fetchone()
        data= row
        return data
        