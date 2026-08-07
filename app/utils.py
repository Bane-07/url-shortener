BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_62(num):
     ans = ""

     while num > 0:
           rem = num%62
           ans += BASE62[rem]
           num //= 62
  
     return ans[::-1] 