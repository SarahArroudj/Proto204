import pytesseract
from PIL import Image


############################################################################
#
#	func    read_picture(img_path)
#
#	brief	1 - convert image to text
#               2 - extract the student id string from a picture
#
#	param	img_path	path of the picture to process (.jpg)
#
#	return	student id string
#
############################################################################
def read_picture(img_path):
    
    print ('--- Start recognize text from image ---')
    
    stringToMatch = '(NI)'

    result1 = pytesseract.image_to_string(Image.open(img_path))
    print (result1)
    #print("=============================================")

    idx_string = result1.find(stringToMatch)
    #result2 = result1[idx_string:]
    result2 = filter(lambda x : x.isdigit(), result1[idx_string:])
    print("NI Result2 : " + result2)


    if(idx_string >= 0 ):
	print ("Student ID : " + result2)
        f = open("extraction_result.txt","w+")
        f.write(result2.encode('utf-8'))
        f.close()

    return result2

############################################################################
if __name__ == "__main__":

	student_id = read_picture("CarteTest.jpg")
        print(student_id)
