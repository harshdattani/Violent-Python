import crypt

def create_pass(first, second):
    PassW = crypt.crypt(first,second)
    return PassW

def pass_break(word):
 Salt = word[0:2]
 dicfile = open('list.txt','r')
 for Word in dicfile.readlines():
     PassWord = create_pass(Word,Salt)
     if(PassWord == word):
         print 'Password is ' + Word
         return

word = pass_break('HXn/NPiDjtpY6')
