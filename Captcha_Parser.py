from PIL import Image
import collections
def CaptchaParse(img):
    datadict={"0":[["0", "0", "0", "1", "1", "1", "1", "0", "0", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "0", "0", "1", "1", "0"], ["1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "0", "0", "0", "1", "1", "0", "1", "1"], ["1", "1", "0", "0", "1", "1", "0", "0", "1", "1"], ["1", "1", "0", "1", "1", "0", "0", "0", "1", "1"], ["1", "1", "1", "1", "0", "0", "0", "0", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1"], ["0", "1", "1", "0", "0", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "0", "0", "1", "1", "1", "1", "0", "0", "0"]],"1":[["0", "0", "0", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1"]],"2":[["0", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["1", "1", "0", "0", "0", "1", "1", "1", "1", "0"], ["1", "0", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "0", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "0", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "0", "0", "0", "0", "1", "1", "1", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "1", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "1", "1", "1", "1", "0", "0", "0", "0"], ["0", "1", "1", "1", "1", "0", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]],"3":[["0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1"], ["0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"]],"4":[["0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "0"], ["0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "0", "0", "1", "1", "0", "1", "1", "1", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"], ["0", "1", "1", "1", "0", "0", "0", "1", "1", "1", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0"]],"5":[["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0"], ["0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1"], ["0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"]],"6":[["0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0"], ["0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "0"], ["1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["0", "1", "1", "1", "0", "0", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0"]],"7":[["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1"], ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0"], ["0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0"], ["0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "0"], ["0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0"], ["0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0"]],"8":[["0", "0", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "0"]],"9":[["0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1"], ["0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1"], ["0", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1"], ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0"]],"A":[["0", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"], ["0", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1"]],"B":[["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"]],"C":[["0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "1", "1", "1", "1", "0", "0", "0", "0", "1", "1"], ["0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0"], ["0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "1"], ["0", "1", "1", "1", "1", "0", "0", "0", "0", "1", "1"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "0"]],"D":[["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0"]],"E":[["1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1"]],"F":[["1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"]],"G":[["0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["0", "1", "1", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "0", "0"]],"H":[["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"]],"I":[["1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1"], ["0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1"]],"J":[["0", "0", "1", "1", "1", "1", "1", "1"], ["0", "0", "1", "1", "1", "1", "1", "1"], ["0", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "0", "0", "0", "1", "1", "1"], ["0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "1", "0", "0"]],"K":[["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "1", "1", "1", "1", "0", "0"], ["1", "1", "1", "0", "0", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "0", "1", "1", "1", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "0", "0", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "1", "1", "1", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"]],"L":[["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1"]],"M":[["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "1", "1", "0", "1", "1", "0", "1", "1", "1"], ["1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "1", "1", "1", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "1", "1", "1", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"]],"N":[["1", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "1", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "1", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"], ["1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"]],"O":[["0", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["0", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "0"]],"P":[["1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0"]],"Q":[["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1"], ["1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1"], ["1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1"], ["1", "1", "0", "0", "0", "0", "0", "1", "0", "0", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "0", "1", "1"], ["0", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "1", "0"]],"R":[["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["1", "1", "1", "0", "0", "1", "1", "1", "1", "0", "0"], ["1", "1", "1", "0", "0", "0", "1", "1", "1", "0", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"]],"S":[["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0", "0", "0", "0", "1", "1", "0"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "0"], ["1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"]],"T":[["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"]],"U":[["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0"]],"V":[["1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1"], ["0", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0"], ["0", "0", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "0"]],"W":[["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "1", "1", "1"], ["0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "1", "1", "0", "0", "0", "1", "1", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "0", "1", "1", "0", "0", "0", "1", "1", "0", "1", "1", "1", "0"], ["0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "0"]],"X":[["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["0", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "0"], ["0", "0", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"], ["0", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1"]],"Y":[["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1"], ["0", "1", "1", "1", "0", "0", "0", "1", "1", "1", "0"], ["0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0"], ["0", "0", "1", "1", "1", "0", "1", "1", "1", "0", "0"], ["0", "0", "1", "1", "1", "1", "1", "1", "1", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0"]],"Z":[["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["0", "0", "0", "0", "0", "0", "1", "1", "1", "1"], ["0", "0", "0", "0", "0", "1", "1", "1", "1", "0"], ["0", "0", "0", "0", "0", "1", "1", "1", "0", "0"], ["0", "0", "0", "0", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "1", "0", "0", "0"], ["0", "0", "0", "1", "1", "1", "0", "0", "0", "0"], ["0", "0", "1", "1", "1", "0", "0", "0", "0", "0"], ["0", "1", "1", "1", "1", "0", "0", "0", "0", "0"], ["1", "1", "1", "1", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]}
    order=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    tcopy=img.copy()
    copy=tcopy.crop((19,2,108,23)) 
    bitwise=copy.load()
    for y in range(0,20):
        for x in range(0,88):
            temp=bitwise[x,y]
            if y!=0 and y!=20:
                if bitwise[x,y+1]==0 and temp==1 and bitwise[x,y-1]==0:
                    bitwise[x,y]=0
    def GetCharWidth(char):
            temp=(datadict[char])
            for i in temp:
                return len(i)
    def ReturnSplitMatrix(x,y,listwidth):
        matrix=[]
        temp=[]
        for i in range(x,x+13):
            for j in range(y,y+listwidth):
                temp.append(str(bitwise[j,i]))
            if '1' not in temp:                
                return False
            matrix.append(temp)
            temp=[]
        return matrix              
    def MatchLetter(SplitMatrix,z):
            i=datadict[z]
            flag=0
            for j in range(0,13):
                count=0
                indexval=[]
                templist=i[j]
                for k in range(0,len(templist)):
                    if templist[k]=='1':
                        indexval.append(k)
                temp=SplitMatrix[j]
                for m in indexval:
                    if temp[m]=='1':
                        count+=1
                if count<len(indexval):
                    return False
                else:
                    flag=1
                indexval=[]
                count=0
            if flag==1:
                return True
            else :
                return False
    def ParseThroughMatrix():
        print "Fetching Captcha:"
        sorter={}
        captcha=''
        for i in order:
            listwidth=GetCharWidth(i)
            for x in range(0,8):
                for y in range(0,89-listwidth):
                    k=ReturnSplitMatrix(x,y,listwidth)                    
                    if k:
                        letter=MatchLetter(k,i)
                        if(letter):
                            dict={y:i}
                            sorter.update(dict)
                            break
        od = collections.OrderedDict(sorted(sorter.items()))
        for i in od.values():
            captcha+=i
        return captcha
    return ParseThroughMatrix()
