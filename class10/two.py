#read abc.txt file and write data in into new file

fp1=open("abc.txt" ,'r')
fp2=open("xyz.txt" ,'w')

data=fp1.read()

fp2=open("xyz.txt" ,'a')
fp2.write(data)
print("new file created successfully")
fp1=close()
fp2=close()
