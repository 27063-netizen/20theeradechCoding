print("โปรแกรมคำนวณความเร็ว")

speed = int(input("โปรดกรอกความเเร็ว(km/h): "))

if speed <=80:
    print("ปลอดภัย")
elif speed <=100:
    print("เตือน")
elif speed <=120:
    print("เสี่ยงถูกปรับ")
else:
    print("ผิดกฏหมายปรับทันที")

print("จัดทำโดย นายธีรเดช สีม่วง 4/4 เลขที่20")