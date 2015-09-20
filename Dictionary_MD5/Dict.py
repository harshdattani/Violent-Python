import crypt
import hashlib

def create_pass(first):
    PassW = hashlib.md5(first).hexdigest()
    return PassW

def pass_break(word):
 dicfile = open('list.txt','r')
 for Word in dicfile.readlines():
     PassWord = create_pass(Word)
     if(PassWord == word):
         print 'Password is ' + Word
         return

word = pass_break('987b337f4eececd83b220e8aa44cefde')
