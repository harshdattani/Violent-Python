import zipfile

def pass_break():
 File = zipfile.ZipFile('breakme.zip')
 dicfile = open('passwords.txt','r')
 for Word in dicfile.readlines():
     Word = Word.strip('\n')
     try:
         File.extractall(pwd=Word)
         print 'Password is ' + Word
         return
     except Exception, e:
         print 'Trying Password ' + Word

pass_break()
