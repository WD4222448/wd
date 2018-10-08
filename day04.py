#1
'''
import math
def getPentagonalNumber(n):
    return n*(3*n-1)/2

k=0
for i in range(1,101):
    print('{} '.format(round(getPentagonalNumber(i))),end='')
    k+=1
    if k==10:
        print()
k=0
'''
#2
'''
def sumDigits(n):
    s=0
    while n!=0:
       s=s+n%10
       n=n/10
    return s

x=eval(raw_input('>>'))
print(sumDigits(x))
'''
#3
'''
import math
def displaySortedNumbers(num1,num2,num3):
    n=max(num1,num2,num3)
    m= min(num1,num2,num3)
    if num1!=n and num1!=m:
        return m,num1,n

    elif num2!=n and num2!=m:import math
def futureInverstmentValue(m,l,y):
    m=m*((1+l/12)**12)
    print(str(y)+'\t'+str(round(m,2)))
    return m

money=raw_input('The amount invested:')
li=raw_input('Annual interest rate:')

num_money=int(money)
num_li=int(li)
num_li=num_li*0.01

print('Years\tFuture Value')

for i in range(1,31):
num_money=futureInverstmentValue(num_money,num_li,i)
        return m,num2,n

    else:
        return m,num3,n

x,y,z=eval(raw_input('Enter three numbers:'))
print('THE sorted numbers are {}'.format(displaySortedNumbers(x,y,z)))
'''
#4
'''
import math
def futureInverstmentValue(m,l,y):
    m=m*((1+l/12)**12)
    print(str(y)+'\t'+str(round(m,2)))
    return m

money=raw_input('The amount invested:')
li=raw_input('Annual interest rate:')

num_money=int(money)
num_li=int(li)
num_li=num_li*0.01

print('Years\tFuture Value')

for i in range(1,31):
num_money=futureInverstmentValue(num_money,num_li,i)
'''
#5
'''
import math
def printChars(ch1,ch2,numberPerLine):
    for i in range(1,ord(ch2)-ord(ch1)):
        print('{} '.format(chr(ord(ch1)+i)),end='')
        if i%numberPerLine==0:
            print()
s1='1'
s2='Z'
n=10
printChars(s1,s2,n)
'''
#6
'''
import math
def printChars(ch1,ch2,numberPerLine):
    for i in range(1,ord(ch2)-ord(ch1)):
        print('{} '.format(chr(ord(ch1)+i)),end='')
        if i%numberPerLine==0:
            print()
s1='1'
s2='Z'
n=10
printChars(s1,s2,n)
'''
#7
'''
import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

x,y,n,m=eval(raw_input('>>'))
print(distance(x,y,n,m))
'''
#8
'''
import math

def sushu(n):
    for i in range (2,int(math.sqrt(n))):
        if n%i==0:
            return 0
            break
    else:
        return 1

print('p\t2^p-1')
for j in range (2,32):
    if sushu(j)==1:
        if sushu (2**j-1)==1:
            print(str(j)+'\t'+str(2**j-1))
            j+=1
    else:
        j+=1

'''
#9
'''
import time
 
now=time.time()
print(now)
mon=time.localtime(now)[1]
day=time.localtime(now)[2]
year=time.localtime(now)[0]
hour=time.localtime(now)[3]
mins=time.localtime(now)[4]
sec=time.localtime(now)[5]

print('Current date and time is '+str(mon)+' '+str(day)+','+str(year)+' '+str(hour)+':'+str(mins)+':'+str(sec))
'''
#10
'''
import random
def sezi():
    x=random.randint(1,6)
    y=random.randint(1,6)
    s=x+y
    print('Yor rolled '+str(x)+'+'+str(y)+'='+str(s))
    return s
S=sezi()
if (S==2) or (S==3) or (S==12):
    print('You lose')
elif (S==7) or (S==11):
    print('You win')
else:
    n=S
    S=sezi()
    while (S!=7) and (S!=n):
        S=sezi()
    if S==7:
        print('You lose')
    else:
print('You win')
'''
#11
'''
#coding: utf-8    
  
import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header   
    
#设置smtplib所需的参数
#下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.163.com'
username = '15047919190@163.com'
password='xxxxx'
sender='15047919190@163.com'
#receiver='XXX@126.com'
#收件人为多个收件人
receiver=['kafeioulei@qq.com']

subject = 'Python email test'
#通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
#subject = '中文标题'
#subject=Header(subject, 'utf-8').encode()
    
#构造邮件对象MIMEMultipart对象
#下面的主题，发件人，收件人，日期是显示在邮件页面上的。
msg = MIMEMultipart('mixed') 
msg['Subject'] = subject
msg['From'] = '15047919190@163.com <15047919190@163.com>'
msg['To'] = '896446511@qq.com'
#收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
#msg['To'] = ";".join(receiver) 
#msg['Date']='2012-3-16'

#构造文字内容   
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"    
text_plain = MIMEText(text,'plain', 'utf-8')    
msg.attach(text_plain)
       
#发送邮件
smtp = smtplib.SMTP()    
smtp.connect('smtp.163.com')
#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
#smtp.set_debuglevel(1)  
smtp.login(username, password)    
smtp.sendmail(sender, receiver, msg.as_string())    
smtp.quit()
'''

