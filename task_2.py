pl=int(input("Сколько осталось немытых тарелок? "))
wash=float(input("Сколько осталось моющего средства? "))
i=0
while i<wash and wash>0:
    pl=pl-1
    wash=wash-0.5
    if wash >= 0:
        print("Осталось"+" "+str(wash)+" "+"моющего средства")
print("Моющее средство закончилось, а осталось помыть"+" "+str(pl)+" "+"тар.")




