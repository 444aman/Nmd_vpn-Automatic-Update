import urllib2
import os

response = urllib2.urlopen('https://twitter.com/vpnbook')
html = response.read()  #reads whole page in html format and save it to html variable


def blank_lines(): #for removing blank lines
    Lines1=open("Data.txt").readlines()
    Lines=[x for x in Lines1 if x.strip()]
    open("Data.txt","w").writelines(Lines)


f=open("Data.txt",'w')
f.write(html)  #save html format in txt file
blank_lines()
f.close() 

search='Password:'  
f=open("Data.txt",'r')
for i in f.readlines():
    if search in i:  #will match string Password: in file 
        temp=i.strip() #if string Found will store those line in temp variable
        break  #as we want the latest Password Updated so as soon it is found we break the loop

temp=temp.replace('</p>','') #at the end of the line it will remove tht 
temp1=temp.index(search)
temp2=temp[temp1:]
temp3=temp2.index(':')
temp3+=1
temp4=temp2[temp3:]
final=temp4.strip()
print final #here we will get the Final Password We have been looking For
raw_input("Press Any Key  To Update Password ")


f.close()


f=open('C:\Program Files (x86)\NMDVPN\config\pass.txt','w')
f.write('vpnbook')
f.write('\n')
f.write(final)
f.close()
print 'Password Updated Sucessfully '
raw_input("Press Any Key To Quit This Application ")
os.remove('Data.txt')

