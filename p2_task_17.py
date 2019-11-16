otvet = input("Hello: ")
list_country = {1 : "google_kazakstan",
 2 : "google_paris",  
 3: "google_uar", 
 4: "google_kyrgystan",
 5 : "google_san franciso", 
 6: "google_germany", 
 7: "google_moscow", 
 8: "google_sweden"
  }
for key, value in list_country.items():
    print(key , ":" , value)
if otvet == "hello":
    country = input("Введите номер офиса в вашей стране: ")
if list_country[1]:
    j = input("Напишите вашу жалобу: ")
    with open("test1", "w") as filename1:
        filename1.write(j)
elif list_country[2]:
    j = input("Напишите вашу жалобу: ")
    with open("test2", "w") as filename2:
        filename2.write(j)
elif list_country[3]:
    j = input("Напишите вашу жалобу: ")
    with open("test3", "w") as filename3:
        filename3.write(j)
elif list_country[4]:
    j = input("Напишите вашу жалобу: ")
    with open("test4", "w") as filename4:
        filename4.write(j)
elif list_country[5]:
    j = input("Напишите вашу жалобу: ")
    with open("test5", "w") as filename5:
        filename5.write(j)
elif list_country[6]:
    j = input("Напишите вашу жалобу: ")
    with open("test6", "w") as filename6:
        filename6.write(j)
elif list_country[7]:
    j = input("Напишите вашу жалобу: ")
    with open("test7", "w") as filename7:
        filename7.write(j)
elif list_country[8]:
    j = input("Напишите вашу жалобу: ")
    with open("test8", "w") as filename8:
        filename8.write(j)
else:
    print('False')





