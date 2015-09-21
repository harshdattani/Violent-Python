import pxssh
s = pxssh.pxssh()
a = s.login('192.168.43.33','zero','0')
print a
s.sendline('ls')
s.prompt()
print s.before
s.sendline('pwd')
s.prompt()
print s.before
