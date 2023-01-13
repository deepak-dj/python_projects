

def ceasor(code,shift):
    store=[]
    
    for i in code:
        if ord(i)+shift>ord('z'):
            store.append(chr(ord(i)+shift-ord('z')+ord('a')-1))
        else:
            store.append(chr(ord(i)+shift))
    print(''.join(store))
   

def cipher(code,shift):
    data = []
    for i in code:
        if ord(i)-shift<ord('a'):
            data.append(chr(ord('z')-(ord('a')-(ord(i)-shift))+1))
        else:
            data.append(chr(ord(i)-shift))    
    print(''.join(data))

    
     
while True:
    operation = input('plz enter the operstions decode/encode : ').strip()
    try:
        if operation == 'encode':
            try:
                encode = input('enter your code to encode : ')
                if encode.isalpha():
                    try:
                        shift = int(input('enter shift : '))
                    except Exception as e:
                        print(f'input must be an integer')
                    else:
                        ceasor(encode,shift)
                else:
                    raise Exception(f'input : {encode}, input must contain english alphabets only')        
            except Exception as e:
                raise

        elif operation == 'decode':
            try:
                decode = input('enter your code to decode : ')
                if decode.isalpha():
                    try:
                     shift = int(input('enter shift : '))
                    except Exception as e:
                        print(f'input must be an integer')
                    else:    
                     cipher(decode,shift)
                else:
                    raise Exception(f'input : {decode}, input must contain english alphabets only')    
            except Exception as e:
                raise   
             
        else:
            raise Exception(f'invalid input : "{operation}", input must be string of either "encode" or "decode"') 
        
    except Exception as e:
        raise
        
    else:          
        done = input('type "yes" if you want to go again else type "no" : ').lower().strip()
        try:
            if done == 'yes':
                continue
            elif done == 'no':
                print('Thanks to visit !!! ')
                break
            else:
                raise Exception('invalid input, input must be either "yes" or "no"')
        except:
            raise








