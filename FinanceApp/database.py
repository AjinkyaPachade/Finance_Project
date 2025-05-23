import pymysql as pm

class Connection:
    def __init__ (self):
        self.con = pm.connect(host='localhost',user='root',password='admin',database='FinanceDatabase')
        self.cursor=self.con.cursor()

    def storeUser(self,name,email,username,pass1):
        self.cursor.execute("insert into user values ('%s','%s','%s','%s')" % (name,email,username,pass1))
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback()
            self.status=False
        return self.status
    
    def checkLogin(self,username,pass1):
        self.cursor.execute("select * from user where username='%s' and password='%s'" % (username,pass1))
        
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status
    

    def changePass(self,username,oldp,newp1):
        self.cursor.execute("update user set Password= '%s' where username='%s' and password='%s'" % (newp1,username,oldp))

        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback()
            self.status=False
        return self.status
    
    def contactDetail(self,name,email,subject,message):
        self.cursor.execute("insert into ContactDetails values ('%s','%s','%s','%s')" % (name,email,subject,message))
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback()
            self.status=False
        return self.status



    def storeIncome(self,username,title,amount,date,category):
        self.cursor.execute("insert into userincome values ('%s','%s','%f','%s','%s')" % (username,title,amount,date,category))
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback()
            self.status=False
        return self.status
     
    
    def viewIncome(self, username, date):
        try:
            query = "SELECT amount FROM userincome WHERE username = %s AND date = %s"
            self.cursor.execute(query, (username, date))
        
            data = self.cursor.fetchone()

            if data:
                return data[0]
            else:
                return None
        except Exception as e:
            print(f"Error in viewIncome: {e}")
            return None
        
        finally:
            self.cursor.close()
            self.con.close()


    def updateIncome(self,username1,date1,amount1,category1):
        if category1 == 'Deposit Income':

            self.cursor.execute("update userincome set amount = amount + '%f' where username = '%s' and date = '%s' " \
                                % (amount1,username1,date1))
        
        else:
            self.cursor.execute("update userincome set amount = amount - '%f' where username = '%s' and date = '%s' " \
                                % (amount1,username1,date1))
            
        try:
            self.con.commit()
            self.status = True
        except:
            self.con.rollback()
            self.status = False


    def deleteIncome(self, username1, date1):
        self.cursor.execute("delete from userincome where username =  '%s' and date = '%s' " % (username1,date1))
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback()
            self.status=False
        return self.status