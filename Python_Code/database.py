import MySQLdb as msql

####### SQL configuration ########
config = {
    'user': 'user',
    'host':'192.168.1.100',
    'passwd':'Motdepasse@123',
    'db':'student_database',
    'port':3306
	 }


#connect to server
db = msql.connect(**config)

##########################################################################################	
#	func	find_ine
#	param	db 			database accessor
#	param	newIne		Ine to check
#
#	brief	serch database blablablabl
#
#	return  0	The student is not in the list
#	return 	1	The student is in the list and validate
#
##########################################################################################
def find_ine(db,newIne):
    cur = db.cursor()
    result=cur.execute("SELECT *  FROM  Std_db where INE= " + newIne)
    db.commit()
    for row in cur:
    	if row==newIne:
		result = 1

    if result == 1:
		print('etudiant figure dans la liste')
		upd = cur.execute("UPDATE `Std_db` SET `State`=1 WHERE INE =" + newIne )
		db.commit()
		return 1
    else:
		print('etudiant intrus')
		return 0
    cur.close()


  
##########################################################################################
##### func validate
# return 0 if student exists and state =0 , return 1 if student exists and state =1
##########################################################################################
def validate_student (db, newIne):
  cur = db.cursor()
  result=cur.execute("SELECT State  FROM  Std_db where INE= " + newIne)
  db.commit()

  if (result == 0) :
    # not in the list
    return -1

  db.commit()
  for row in cur:
    if row[0] == 1:
      #already badged
      return 1
    if row[0] == 0:  
      upd = cur.execute("UPDATE `Std_db` SET `State`=1 WHERE INE =" + newIne )
      db.commit()
      cur.close()
      return 0
  
  
  
##########################################################################################
# func		print_present
# param 	db 		database accessor
# param 	newIne	Ine to check
#  
# brief     Check if the student is validated and mark him present
#
# return   0    the student isn't validated yet
# return   1    the student is already validated
########################################################################################## 

def is_present(db,newIne):
    cur = db.cursor()
    verif = cur.execute("SELECT State  FROM  Std_db  WHERE INE= " + newIne)
    for row in cur:
    	if row == 0:
    		return 0
	else:
    		print ('Letudiant a deja badge')
    		return 1

    result=cur.execute("SELECT `Nom`  FROM  `Std_db`  WHERE state = 1")
    db.commit()
    for row in cur:
    	print('Letudiant %s est present',row)
    cur.close()
##########################################################################################
# func		display present
# param 	db 		database accessor
# 
# brief     print the number of students that are present 
# 
########################################################################################## 

def display_present(db):
    cur = db.cursor()
    total = cur.execute("SELECT COUNT(State) FROM `Std_db` ")
    present = cur.execute ("SELECT COUNT(State) FROM `Std_db` WHERE State = 1") 
    print ('Il y a' present '/' total 'de presents')
    cur.close()
