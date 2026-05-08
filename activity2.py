Amount = int(input("please enter the amount for deposit: "))

note_1 = (Amount//500)
note_2 = (Amount%500)//100
note_3 = ((Amount%500)%100)//50
note_4 = (((Amount%500)%100)%50)//10

print("notes of 500 rupee", note_1)
print("notes of 100 rupee", note_2)
print("notes of 50 rupee", note_3)
print("notes of 10 rupee", note_4)