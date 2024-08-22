#n = int("a") #Value exception
#n = 10/0 # Divid by zero error/exception
#a = [10,20,30]
#print(a[20]) # Index Error
#print(a[-1]) # No error Error
#a = None
#b= a+10 #TypeError
#b= 'Ahmad' + 10 #TypeError

try:
    #n = int("a") #Value Error / exception
    #a = {20201:"ahmad",20202:"Saed"}
    #print(a[20203]) #Key Error
    #fh = open('data1.txt') #File Not Found Error
    #fh.close()
    pass
except FileNotFoundError:
    print("Invalid File name")
except KeyError:
    print("Invalid Student ID")
except:
    print("Unknown Error")
finally:
    print("Error in system... ")
