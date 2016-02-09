from __future__ import division
import sys
sys.path = ['/Library/Python/2.7/site-packages'] + sys.path
import cv2
import os

username = sys.argv[1]

# Open file
path = "../pics/"+username+"_instagram_photos/"
os.system("downstagram -o ../pics "+username)
dirs = os.listdir( path )
cascPath = "haarcascade_frontalface_default.xml"
friendResults = open(username+'_friendResults.csv','a+')

total = 0
selfie = 0 
group = 0
artsy = 0

for file in dirs:
	# Get user supplied values
	# Create the haar cascade
	if file != ".DS_Store" and file.find("mp4") == -1:
		faceCascade = cv2.CascadeClassifier(cascPath)
		# Read the image
		image = cv2.imread(path+file)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.10,
			minNeighbors=5,
			minSize=(30, 30),
			flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		#print "Found {0} faces!".format(len(faces))
		facecount = len(faces)
		total += 1
		if facecount == 0:
			artsy += 1
		elif facecount == 1:
			selfie += 1
		else:
			group += 1
		# Draw a rectangle around the faces
		#for (x, y, w, h) in faces:
		#	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
		#cv2.imshow("Faces found", image)
		#cv2.waitKey(0)

print "Total pictures: %s." % total
print "Artsy Fartsy pictures: %s." % artsy
print "Group pictures: %s." % group
print "Selfie pictures: %s." % selfie
selfiescore = selfie/total
socialscore =  group/total
print "Selfie score: %s." % selfiescore
print "Social score: %s." % socialscore
friendResults.write(str(username)+","+str(total)+","+str(artsy)+","+str(selfie)+","+str(group)+","+str(selfiescore)+","+str(socialscore)+"\n")





