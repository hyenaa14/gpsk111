number_list= [[10,50],[20,40],[30,60],[40,70]]
print(number_list)
for i in number_list:
    for j in i:
        print(j)


my_list=[[1000,20],[400,800],[1000,1400]]
for i in my_list:
    var=0
    for j in i:
        var=var+j
    print(var/len(j))



number=0
while number<10:
    number=number+1
    print("나무를", str(number)+"번 찍었습니다")
else:
    print("나무가 넘어갑니다")



