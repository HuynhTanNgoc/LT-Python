#Cấu trúc if

#1.Chương trình kiểm tra số chẳn hay lẻ trong Py:
number = 2
if number % 2 == 0:
    print(number, "là số chẳn")
else:
    print(number, "là số lẻ")

#2.Chương trình tìm số lớn nhất trong 3 số bằng Py:
number1 = float(input("Nhập vào number1: "))
number2 = float(input("Nhập vào number2: "))
number3 = float(input("Nhập vào number3: "))


if number1 > number2 and number1 > number2:
    print("{0} là số lớn nhất".format(number1))
    #print(" %1f là Max" %(number1))
elif number2 > number1 and number2 > number3 :
    print("{0} là số lớn nhất".format(number2))
    #print(" %1f là Max" %(number2))
else:
    print("{0} là số lớn nhất".format(number3))
    #print(" %1f là Max" %(number3))


#3.Chương trình in ra các ngày trong tháng bằng Py:

month = int(input("Nhập vào tháng từ 1->12: "))
month31 = [1,3,5,7,10,12] #Khai báo mảng month31
month30 = [4,6,9,11] 

if month in month31: # kiểm tra xem tháng thuộc mảng month31 hay không nói True thì chạy tiếp ...
    for i in range(1,32):
        print(i)
elif month in month30:
    for i in range(1,31):
        print(i)
elif month == 2:
    for i in range(1,29):
        print(i) 
else:
    print("Nhập vào month sai. Vui lòng nhập lại!")
             
"""
if month in month31: # kiểm tra xem tháng thuộc mảng month31 hay không nói True thì chạy tiếp ...
    print("Tháng {0} Có 31 ngày".format(month))
elif month in month30:
    print("Tháng {0} Có 30 ngày".format(month))
elif month ==2:
    print("Tháng {0} Có 28 ngày".format(month)) 
else:
    print("Nhập vào month sai. Vui lòng nhập lại!")
"""
    
##4.Viết chương trình cho người dùng nhập vào một số nguyên n. 
"""Nếu n lẻ thì in ra màn hình dòng chữ “Số lẻ”. 
Nếu số n chẵn và lớn hơn hoặc bằng 100 thì in ra màn hình dòng chữ “Số chẵn và lớn hơn hoặc bằng 100”, 
ngược lại thì in ra dòng chữ “Số chẵn và bé hơn 100”."""

n = int(input("Nhập vào số nguyên n: "))

#kiểm tra n:
if n % 2 != 0:
    print("Số lẻ")
elif n % 2 == 0 and n >= 100:
    print("Số chẵn và lớn hơn hoặc bằng 100")
else:
    print("Số chẵn và bé hơn 100")


#5.Biện luận phương trình bậc nhất ax+b=0.
a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))

#Nếu a == 0 và b == 0 pt vô số nghiệm (đúng với mọi x) ngược lại a == 0 và b != 0 thì pt vô nghiệm
if a == 0:
    if b == 0:
        print("Phương trình ax+b = 0 vô số nghiệm.")
    else:
        print("Phương trình ax+b = 0 vô nghiệm.")
    
# ngược lại nếu a!= 0 thì phương trình có nghiệm duy nhất x = -b/a    
else:
    print("Phương trình ax+b=0 có nghiệm duy nhất x = -b/a = -{0}/{1} = {2}".format(b, a, -b/a))
    
    
#6.Biện luận phương trình bậc hai ax2+bx+c=0.
import math

a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))

#Điều kiện của pt là a phải khác 0 .
if a == 0:
    print("Nhập lại a khác 0: ")
else:
    delta = b**2 - 4*a*c
    print("delta = {0}".format(delta))
    #Nếu delta > 0 thì pt có 2 nghiệm phân biệt: 
    if delta > 0:
        print("Pt có 2 nghiệm phân biệt x1 = {0} và x2 = {1} ".format((-b) + math.sqrt(delta/(2*a)), (-b) - math.sqrt(delta/(2*a))))
    #Nếu delta == 0 thì pt có 1 nghiệm kép:
    elif delta == 0:
        print("Pt có 1 nghiệm kép x1 = x2 = {0}".format(-b/2*a))

    #Nếu delta < 0 thì pt vô nghiệm:1
    else:
        print("Pt vô nghiệm")


#7.Người dùng nhập vào một năm là một số nguyên dương bất kì. Cho biết năm đó có là năm nhuận hay không?

#Năm nhuận nếu year %400 == 0 or year % 4 == 0 and year % 100 != 0
year = int(input("Nhập vào year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0): # or(|) , and(&) 
    print("Năm {0} là năm nhuận".format(year))
else:
    print("Năm {0} không phải là năm nhuận".format(year))
    
    
#8.Hãy nhập vào tuổi của một người và đưa ra kết quá kết luận lứa tuổi của người đó theo quy tắc sau:
#Nếu Tuổi >0 và <=2 là trẻ sơ sinh
#Nếu Tuổi >2 và <=10 là nhi đồng
#Nếu Tuổi >10 và <17 là vị thành niên
#Nếu Tuổi >17 và <= 39 là thanh niên    
#Nếu Tuổi >39 và <=50 là trung niên  
#Nếu Tuổi >50 là cao niên

age = int(input("Nhập vào tuổi của bạn : "))

if age <= 0:
    print("Nhập sai. Vui lòng nhập lại tuổi lớn hơn 0!")
elif age <= 2:
    print("Trẻ sơ sinh")
elif age <= 10:
    print("Nhi đồng")
elif age < 17:
    print("Vị thành niên")
elif age <= 39:
    print("Thanh niên")
elif age <= 50:
    print("Trung niên")
else:
    print("Cao niên")

#9.Hãy nhập vào năm sản xuất của một chiếc máy tính, sau đó đưa ra đề xuất với máy tính đó theo quy tắc sau:
#Nếu năm sx >=15 thì đưa ra đề xuất"thay the"
#Nếu nsx >=10 và <15 thì đưa ra đề xuất"Bao tri"
#Những trường hợp khác đưa ra đề xuất "Khong co de xuat"

manufacture = int(input("Nhập năm sản xuất: ")) # year of manufacture : năm sản xuất

if manufacture >= 15:
    print("Thay the")
elif manufacture >=10 and manufacture < 15:
    print("Bao tri")
else:
    print("Khong co de xuat")  
    
#10.Hãy nhập vào 1 điểm tb và xét học bổng đối với điểm trung bình đó theo quy trình
#Nếu đtb >=9 thì học bổng là 5000000
#Nếu đtb >=8 và <9 thì học bổng là 3000000
#Nếu đtb >=7 và <8 thì học bổng là 1000000
#Những trường hợp còn lại học bổng = 0.

score = float(input("Nhập vào điểm: ")) #medium(trung bình) score(điểm) 

if score >= 9:
    print("Học bổng là 5000000")
elif score >=8:
    print("Học bổng là 3000000")
elif score >=7:
    print("Học bổng là 1000000")
else:
    print("Học bổng = 0")
    
    
#11.Nhập một số N bất kỳ từ bàn phím.
# N có phải là số nguyên không?
# Kiểm tra tính chẵn lẻ của N.
# N có phải là số chẳn dương không?
# N Có phải là số lẻ âm không?
# N có phải là số chính phương không?

N = float(input("Nhập vào số N bất kỳ: "))

#N có phải là số nguyên không?
if N % 1 == 0:
    print("N là số nguyên")
else:
    print("N không phải là số nguyên")

# Kiểm tra tính chẵn lẻ của N.
if N % 2 == 0: 
    print("N là số chẵn")
else:
    print("N là số lẻ")
    
# N có phải là số chẳn dương không?       
if N % 2 == 0 and N > 0:
    print("N là số chẳng dương")
else:
    print("N không phải là số chẵn dương")
    
# N Có phải là số lẻ âm không?        
if N % 2 != 0 and N < 0:
    print("N là số lẻ âm")
else:
    print("N không phải là số lẻ âm")
        
# N có phải là số chính phương không?        
if N > 0 and math.sqrt(N) % 1 == 0: 
    print("N là số chính phương")
else:
    print("N không phải là số chính phương")