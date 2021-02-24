import time
def remove_duplicates():
    start_time = time.time()
    text=input("enter you text:")
    s1=""
    for letter in text:
        if letter not in s1:
            s1+= letter
    print(s1)
    end_time = time.time()
    print(end_time-start_time)
    
    
    
            
    
    
 
