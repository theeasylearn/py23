try:
    n = int(input("enter a number:"))  # value error

    print(n+"hello")   #typeerror


    # indexerror
    l1 = [1,2,3]
    for i in range(0,4):
        print(l1[i])
        
except ValueError:
    print("give valid input")

except TypeError:
    print("give valid type")
    
except(IndexError,KeyError,KeyboardInterrupt):
    print("out of range")
    
except:
    print("error")
    
finally:
    print("code...")
    