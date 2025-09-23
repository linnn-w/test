#    def is_goblins(height=120):
#        print("身高是", height,"cm")
#        if height > 175:
 #           print("不是哥布林")
  #      elif height > 160:
   #         print("可能不是哥布林")
    #    else:
     #       print("是哥布林")
#    result = is_goblins()
#    print(result)


#--------------------------------
def is_goblins(height):
    if height > 175:
         return "不是哥布林"
    elif height > 160:
         return "可能不是哥布林"
    else:
         return "是哥布林"

def test(height):
    try:
        return is_goblins(height)
    except TypeError:
        print("請輸入身高")
        return None

result = test(135)
print(result)
   


