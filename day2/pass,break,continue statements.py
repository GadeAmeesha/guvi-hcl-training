students = ["Ameesha", "Ravi", "Priya"]

for s in students:
    if s == "Priya":
        pass   # later we will write special logic for Priya
    else:
        print(s, "is present")


pin = 1234
entered_pins = [1111, 2222, 1234, 4444]

for p in entered_pins:
    if p == pin:
        print("✅ Correct PIN. Access Granted.")
        break   # stop checking once correct pin entered
    else:
        print("❌ Wrong PIN")


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days:
    if d in ["Sat", "Sun"]:
        continue   # skip weekends
    print("Working Day:", d)
