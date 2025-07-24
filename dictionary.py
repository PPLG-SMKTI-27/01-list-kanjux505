student1 = {"nama":"ambatukam","asal":"pop aku bilek","nilai": 90}
student2 = {"nama":"bambang","asal":"bontNG","nilai": 90}
student3 = {"nama":"cecep","asal":"CIMAHI","nilai": 80}
student4 = {"nama":"joko","asal":"widodo","nilai": 85}

students = [student1,student2,student3]
print(students)


sum = 0
for i in range(len(students)):
    sum = sum + students [i]["nilai"]
print("total semua nilai siswa adalah ", sum) 

ratarata = sum / len(students)
print("nilai rata rata siswa adalah",ratarata)

nama = str(input())
asal = str(input())
nilai = str(input())
student4 = {"nama":"nama","asal":"asal","nilai": 85}
students.append(student4)
print(students)

print("no\tnama\tasal\tnilai")
for i in range(len(students)):
    print(i+1,"\t", students[i]["nama"],"\t", students[i]["asal"], "\t", students[i]["nilai"])

    print ("nama\tasal\tnilai")
    for s in students:
        print(s["nama"], "\t",s["asal"], "\t",s ["nilai"])