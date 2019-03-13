import picamera
import time 
from time import sleep
import MySQLdb as msql

####### SQL configuration ########
config = {
    'user': 'user',
    'host':'192.168.0.69',
    'passwd':'Motdepasse@123',
    'db':'test',
    'port':'3306'
    }
    #connect to server
db = msql.connect(**config)

#def exe_query(db, dataa,newIne):
    cur = db.cursor()
result=cur.execute("UPDATE `test_test` SET state = "+dataa+" WHERE ine = "+newIne+"")
    db.commit()
    cur.close()



##########################################################################################    
#    func    find_ine
#    param    db             database accessor
#    param    newIne        Ine to check
#
#    brief    serch database blablablabl
#
#    return  0    The student is not in the list
#    return     1    The student is in the list and validate
#
##########################################################################################
def find_ine(db,newIne):
cur = db.cursor()
    result=cur.execute("SELECT `ine`  FROM  `test_test` ")
    db.commit()
    for row in cur:
        if row==newIne:
            res = 1
            

    if res==1:
        print('etudiant figure dans la liste')
        upd = cur.execute("UPDATE `test_test` SET `State`=1")
        return 1
    else:
        print('etudiant intrus')
        return 0
    cur.close()
    ##########################################################################################
# func        print_present
# param     db         database accessor
# param     newIne    Ine to check
#  
# brief     Check if the student is validated and mark him present
#
# return   0    the student isn't validated yet
# return   1    the student is already validated
########################################################################################## 

def print_present(db,newIne):
    cur = db.cursor()
    verif = cur.execute("SELECT `Nom`  FROM  `test_test`  WHERE state ")
    for row in cur:
        if row == 0:
            return 0
            else:
            print ('Letudiant a deja badge')
            return 1
    result=cur.execute("SELECT `Nom`  FROM  `test_test`  WHERE state = 1")
    db.commit()
    for row in cur:
        print('Letudiant %s est present',row)
    cur.close()
##########################################################################################
# func        display present
# param     db         database accessor
# 
# brief     print the number of students that are present 
# 
########################################################################################## 

def display_present(db):
    cur = db.cursor()
    total = cur.execute("SELECT COUNT(State) FROM test_test ")
    present = cur.execute ("SELECT COUNT(State) FROM test_test WHERE State = 1") 
    print ('Il y a %d / %d  de presents', present, total)
    cur.close()
   




def detect_INE():
    newIne="okdh";
    return newIne
    
if __name__ == "__main__":

    print("starting EasyStudentsScan")

#    while 1 :
 # Take a picture using the camera
camera = picamera.PiCamera()
try:
    camera.start_preview()
    time.sleep(10)
    camera.capture('/home/pi/Desktop/Proto204/Examples/imh.jpeg')
    camera.stop_preview()
finally:
    camera.close()

        # Extract INE number from the photo
    detect_INE()

        # Verify if the INE number exists in the database
            
    find_ine(db,newIne)
        # if the student is in the list : Green Led + sound
        # else if the student is not in the list : Red led + sound
    print_present(db,newIne)

        # Print the number of student present on the screen
    display_present(db)

        # If the button is pressed : database is reseted

        # Wait 20 seconds