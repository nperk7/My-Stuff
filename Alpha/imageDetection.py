__author__ = 'naperkins'
import numpy, cv2, imutils

def getFeed():
    cv2.namedWindow("Alpha's Eye")
    vc = cv2.VideoCapture(1)
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    while rval:
        cont = contours(frame)
        cv2.flip(frame, 1, frame)
        cv2.imshow("Alpha's Eye", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27 or key == ord("q"): # exit on ESC
            break
    cv2.destroyWindow("Alpha's Eye")

def contours(frame):
    conts = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 150, 200, apertureSize = 3)
    cnts = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    """for c in cnts:
        try:
            if cv2.contourArea(c) > 75:
                conts.append(c)
        except:
            pass"""
    #cv2.HoughLines(edges, numpy.pi/180, 15, 30)
    try:
        cv2.drawContours(frame, cnts, -1, (255, 0, 0), 3)
    except:
        pass
    return [edges]

getFeed()
