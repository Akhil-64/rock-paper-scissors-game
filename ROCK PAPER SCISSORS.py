import random
print("WINNING RULES:-")
print("ROCK VS PAPER :- PAPER WINS")
print("PAPER VS SCISSORS :- SCISSORS WINS")
print("ROCK VS SCISSORS :- ROCK WINS")
count1=0
count2=0
while True:
 print("Choose any option")
 print("1 Rock")
 print("2 Paper")
 print("3 Scissors")
 print("ENTER OPTION")
 option=input()
 if (option=="1"):
    print("USER OPTION IS:- 1")
    print("USER OPTION NAME IS:- Rock")
 elif (option=="2"):
    print("USER OPTION IS:- 2")
    print("USER OPTION NAME IS:- Paper")
 elif(option=="3"):
    print("USER OPTION IS:- 3")
    print("USER OPTION NAME IS:- Scissors")
 else:
    print("INVALID OPTION")
 op=int(option)
 if(op<4):    
    
  print("NOW COMPUTER TURNS..................")
  option2=random.randint(1,3)
  if(option2==1):
    print("COMPUTER CHOICE IS:- Rock")
  elif(option2==2):
    print("COMPUTER CHOICE IS:- Paper")
  else:
    print("COMPUTER CHOICE IS:- Scissors")

    
  if(option=="1"):
    rock="Rock"
  elif(option=="2"):
    rock="Paper"
  else:
    rock="Scissors"
  if(option2==1):
    rock2="Rock"
  elif(option2==2):
    rock2="Paper"
  else:
    rock2="Scissors"
  
  print(rock,"VS",rock2)
  if(option=="1" and option2==1):
     print("==> TIE NO POINT")
  elif(option=="1" and option2==2):
     print("==> COMPUTER WINS")
     count1+=1
  elif(option=="1" and option2==3):
     print("==> USER WINS")
     count2+=1
  elif(option=="2" and option2==1):
     print("==> USER WINS")
     count2+=1
  elif(option=="2" and option2==2):
     print("==> TIE NO POINT")
  elif(option=="2" and option2==3):
     print("==> COMPUTER WINS")
     count1+=1
  elif(option=="3" and option2==1):
     print("==> COMPUTER WINS")
     count1+=1
  elif(option=="3" and option2==2):
     print("==> USER WINS")
     count2+=1
  elif(option=="3" and option2==3):
     print("==> TIE NO POINT")
     
  #print("COUNT1",count1)
  #print("COUNT2",count2)
     

  
 print("Do you want to continue? (YES or NO)")
 cont=input()
 if cont=="no" or cont=="NO" or cont=="No":
    break

print("TOTAL COUNT")
print("Total USER count =",count2)
print("Total COMPUTER count =",count1)
if count2>count1:
    print(r"\\USER WINS//")
elif count2<count1:
    print(r"\\COMPUTER WINS//")
else:
    print(r"\\TIE GAME//")



print("***** THANKS FOR PLAYING *****")

 







    
 
