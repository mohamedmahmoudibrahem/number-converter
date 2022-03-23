
a=input("enter number you want to convert: ")
b=int(input("enter number base: "))
c=int(input("enter base that you want convert to it: "))
if b==10:
 decimal_num=float(a)
 base_num=c
 left1=[]
 decimal_point="0"
 decimal_lift=[]
 for i in range(0,len(str(decimal_num))):
  if  str(decimal_num)[i]==".":
      decimal_point=decimal_point+(str(decimal_num)[i:]) 
 while float(decimal_point)!=0:
    decimal_lift.append(int(float(decimal_point)*base_num))
    decimal_point=str(float(float(decimal_point)*base_num)-int(float(decimal_point)*base_num))
    if len(decimal_lift)>20:
        print("infinty decimal point")
        break
    if decimal_point=="0.0":
        break          
 while decimal_num >=1 :  
  if int(decimal_num)%base_num==10:
      left1.append("A")
      decimal_num=int(decimal_num)//base_num 
  elif int(decimal_num)%base_num==11:
      left1.append("B")
      decimal_num=int(decimal_num)//base_num 
  elif int(decimal_num)%base_num==12:
      left1.append("C")
      decimal_num=int(decimal_num)//base_num 
  elif int(decimal_num)%base_num==13:
      left1.append("D")
      decimal_num=int(decimal_num)//base_num 
  elif int(decimal_num)%base_num==14:
      left1.append("E")
      decimal_num=int(decimal_num)//base_num 
  elif decimal_num%base_num==15:
      left1.append("F")
      decimal_num=int(decimal_num)//base_num   
  if int(decimal_num)%base_num<10:              
    left1.append(int(decimal_num)%base_num)
    decimal_num=int(decimal_num)//base_num 
 print(left1[::-1],".",decimal_lift)
else: 
 number=a
 base_num=b
 number1=[]
 decimal_lift1=[]
 decimal_num=0
 dec_num_lift=0
 v="."
 for i in range(0,len(number)):
   if number[i] !=v:  
    number1.append(number[i])
   else:
    decimal_lift1.append(number[i]) 
    if i==len(number)-1:
      break
    v=number[i+1] 
 for i in range(0,len(decimal_lift1)):
  if decimal_lift1[i]=="A":
    decimal_lift1[i]="10"
  elif decimal_lift1[i]=="B":
    decimal_lift1[i]="11" 
  elif decimal_lift1[i]=="C":
    decimal_lift1[i]="12"
  elif decimal_lift1[i]=="D":
    decimal_lift1[i]="13"
  elif decimal_lift1[i]=="E":
    decimal_lift1[i]="14"
  elif decimal_lift1[i]=="F":
    decimal_lift1[i]="15"    
 for i in range(1,len(decimal_lift1)):
  decimal_lift1[i]=(int(decimal_lift1[i])*base_num**(i*-1)) 
 for i in range(1,len(decimal_lift1)):
  dec_num_lift=dec_num_lift+decimal_lift1[i]
 for i in range(0,len(number1)):
  if number1[i]=="A" or number1[i]=="a" :
    number1[i]="10"
  elif number1[i]=="B" or number1[i]=="b":
    number1[i]="11" 
  elif number1[i]=="C" or number1[i]=="c":
    number1[i]="12"
  elif number1[i]=="D" or number1[i]=="d":
    number1[i]="13"
  elif number1[i]=="E" or number1[i]=="e":
    number1[i]="14"
  elif number1[i]=="F" or number1[i]=="f":
    number1[i]="15"
 number1=number1[::-1] 
 for i in range(0,len(number1)):
  number1[i]=int(number1[i])*base_num**i  
 for i in number1:
  decimal_num=decimal_num+i
 decimal_num=float(decimal_num+dec_num_lift)
 base_num=c
 left1=[]
 decimal_point="0"
 decimal_lift=[]
 for i in range(0,len(str(decimal_num))):
   if  str(decimal_num)[i]==".":
       decimal_point=decimal_point+(str(decimal_num)[i:]) 
 while float(decimal_point)!=0:
     decimal_lift.append(int(float(decimal_point)*base_num))
     decimal_point=str(float(float(decimal_point)*base_num)-int(float(decimal_point)*base_num))
     if len(decimal_lift)>25:
         print("infinty decimal point")
         break
     if decimal_point=="0.0":
         break          
 while decimal_num >=1 :  
   if int(decimal_num)%base_num==10:
       left1.append("A")
       decimal_num=int(decimal_num)//base_num 
   elif int(decimal_num)%base_num==11:
       left1.append("B")
       decimal_num=int(decimal_num)//base_num 
   elif int(decimal_num)%base_num==12:
       left1.append("C")
       decimal_num=int(decimal_num)//base_num 
   elif int(decimal_num)%base_num==13:
       left1.append("D")
       decimal_num=int(decimal_num)//base_num 
   elif int(decimal_num)%base_num==14:
       left1.append("E")
       decimal_num=int(decimal_num)//base_num 
   elif decimal_num%base_num==15:
       left1.append("F")
       decimal_num=int(decimal_num)//base_num   
   if int(decimal_num)%base_num<10:              
      left1.append(int(decimal_num)%base_num)
      decimal_num=int(decimal_num)//base_num 
 print(left1[::-1],".",decimal_lift)