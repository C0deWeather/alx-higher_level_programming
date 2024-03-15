#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    
    if len(argv) - 1 == 0:
        print(f"0 arguments.")
    elif len(argv) - 1 == 1:
        print(f"1 argument:")
    else:
        print(f"{len(argv) - 1} arguments:")
 
    i = 0
    for argument in argv:
        if i == 0:
            i += 1
            continue
        print(f"{i}: {argument}")
        i += 1
        
    
    
