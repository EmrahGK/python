def rotate(input,d): 
  
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    
    print ("Left Rotation : ", (Lsecond + Lfirst) )