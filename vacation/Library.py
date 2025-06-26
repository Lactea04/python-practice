import sys
from os import getcwd, chdir
import shutil
import glob #파일 이름 찾기
import tempfile


path = "C:\\Users\\kimtg\\OneDrive\\Desktop\\python"
#f = os.popen("dir") #시스템 명렁어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려줌.


#print(sys.argv) #['C:\\Users\\kimtg\\OneDrive\\Desktop\\python\\vacation\\Library.py']

chdir(path)
#print(glob.glob("*pdf")) #pdf 파일 모두 출력

#print(getcwd())
#print(f.read())
#with open("%s\\text.txt"%path, "w") as f:
#    f.write("hello world")
#shutil.copy("text.txt", "dst.txt")

#filename = tempfile.mktemp()
#print(filename) #C:\Users\kimtg\AppData\Local\Temp\tmp3ioe5hww

#f = tempfile.TemporaryFile()
#f.close()
