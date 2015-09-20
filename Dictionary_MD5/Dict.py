import crypt
import hashlib

def create_pass(first):
    PassW = hashlib.md5(first).hexdigest()
    return PassW

def pass_break(word):
 dicfile = open('passwords.txt','r')
 for Word in dicfile.readlines():
     Word = Word.strip('\n')
     PassWord = create_pass(Word)
     if(PassWord == word):
         print 'Password is ' + Word
         return

word = pass_break('0d378caceeaf25845ea380b7e9833f6d')
