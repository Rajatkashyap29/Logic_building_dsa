def calculate_gcd(n1,n2):
    ans=None
    
    if n1 > n2 :
        big = n1
        small = n2
    else :
        big = n2
        small = n1
        
    while small > 0:
        r = big % small 
        if r == 0 :
            ans= small
            break
        big = small
        small = r
    return  ans