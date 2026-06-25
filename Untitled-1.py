print("โปรแกรมคำนวณความเร็ว")
speed1 = int(input("ความเร็วรถ 1: "))
speed2 = int(input("ความเร็วรถ 2: "))
speed3 = int(input("ความเร็วรถ 3: "))

total = (speed1 + speed2 + speed3)
average = total / 3
print("ความเร็วรวม",total)
print("ความเร็วเฉลี่ย",average)
if speed1 >=80:
    print("ระดับความเร็ว: ปลอดภัย")
elif speed2 >=81-100:
    print("ระดับความเร็ว: เตือน")
elif speed3 >=101-120:
    print("ระดับความเร็ว: เสี่ยงถูกปรับ")
else:
    print("ระดับความเร็ว: ผิดกฏหมาย")
