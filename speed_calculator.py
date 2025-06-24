# برنامج يحسب السرعة = المسافة ÷ الزمن

distance = float(input("أدخل المسافة (كم): "))
time = float(input("أدخل الزمن (بالساعات): "))

if time == 0:
    print("خطأ: لا يمكن القسمة على صفر!")
else:
    speed = distance / time
    print("السرعة هي:", speed, "كم/ساعة")
