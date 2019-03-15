import picamera
from time import sleep

# Our library
from text_recognition import *
from database import *
from HMI import *





##########################################################################################
#
#	
#
##########################################################################################
def is_student_validated(newIne):

  # Verify if the INE number exists in the database
  ine_exists = validate_student(db,newIne)
  
  # if the student is in the list : Green Led + sound
  if (ine_exists == 1):
    print("Student in the list but refused : already badged")
    #display_result(1)
    
  elif (ine_exists == 0):
    print("Student in the list and accepted")
    #display_result(1) 
      
  elif (ine_exists == -1):
    print("Student in not the list")
    #display_result(1)   

  
  
##########################################################################################
#
#	
#
########################################################################################## 
if __name__ == "__main__":
  
  print("starting EasyStudentsScan")
  
  
  #init_HMI()
  
  
  
  
  #    while 1 :
  
  ## Take a picture using the camera
  camera = picamera.PiCamera()
  try:
  camera.start_preview()
  time.sleep(10)
  camera.capture('carte_1.jpeg')
  camera.stop_preview()
  finally:
  camera.close()
  
  # Extract INE number from the photo
  newIne = read_picture('carte_1.jpg')
  print ("Detected Ine : " + newIne)
  
  
  print("test 1")
  is_student_validated(newIne)
  print("test 2")
  is_student_validated(newIne)

  
  
  
  # Print the number of student present on the screen

  # If the button is pressed : database is reseted
  
  # Wait 20 seconds
  time.sleep(20)
