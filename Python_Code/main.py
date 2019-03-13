import Rpi.GPIO as GPIO
import MySQLdb as msql
from picamera import Picamera
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def takephoto () :
camera=Picamera()
# réglage de la résolution
camera.resolution = (1024,768)

# rotation de l'image (utile si la caméra est à l'envers)
camera.rotation = 180

# aperçu, mais dans une portion de l'écran seulement
camera.start_preview(fullscreen = False, window = (50,50,640,480))

# un délai est nécessaire pour laisser le temps aux capteurs de se régler
sleep(5)

#on enregistre le fichier sur le bureau
camera.capture('/home/pi/Bureau/image.jpeg')

#on fait disparaître l'aperçu.
camera.stop_preview()
# réglage de la résolution
camera.resolution = (1024,768)

# rotation de l'image (utile si la caméra est à l'envers)
camera.rotation = 180

# aperçu, mais dans une portion de l'écran seulement
camera.start_preview(fullscreen = False, window = (50,50,640,480))

# un délai est nécessaire pour laisser le temps aux capteurs de se régler
sleep(5)

#on enregistre le fichier sur le bureau
camera.capture('/home/pi/Bureau/image.jpeg')

#on fait disparaître l'aperçu.
camera.stop_preview()
sleep (20)

def detect_INE():



    ####### SQL configuration ########
    config = {
        'user': 'root',
        'host': '192.168.0.66',
        'db': 'test',
    }

    # connect to server
    db = msql.connect(**config)

 def find_ine(db, newIne):
        cur = db.cursor()
        result = cur.execute("SELECT `ine`  FROM  `test_test` ")
        db.commit()
        for row in cur:
            if row == newIne:
                res = 1
        if res == 1:
            print('etudiant figure dans la liste ')
            GPIO.output(21, GPIO.HIGH)
        else :
            print('etudiant intrus')
            GPIO.output(22, GPIO.HIGH)
        cur.close()

def print_present(db, newIne):
            cur = db.cursor()

        result = cur.execute("SELECT `Nom`  FROM  `test_test`  WHERE state = 1")
        db.commit()
        for row in cur:
            print('Letudiant %s est present', row)
        cur.close()

