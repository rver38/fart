import os, base64
def dcr(sex):
     cheeks = []
     ok = 1
     sex = sex.split("_rverflow_")
     for i in sex:
          for x in i:
               if x == u"\u200c":
                    cheeks.append("0")
               elif x == u"\ufeff":
                    cheeks.append("1")
          ok += 1
          if ok == 5:
               cheeks.append("poop")
               ok = 1
          else:
               cheeks.append("fart")
     sex2 = ''.join(cheeks)[:-8]
     butt = []
     for y in sex2.split("poop"):
          for i in y.split("fart"):
               butt.append(chr(int(i, 2)))
          butt.append("fart")
     butt.pop()
     sex3 = ''.join(butt)
     buttock = []
     for i in sex3.split("fart"):
          buttock.append(base64.b64decode(i))
     result = b''.join(buttock).decode()
     return result


