import os, getpass, platform, requests
ver = platform.python_version().split(".");ver.pop();ver = ''.join(ver)
rpath = f"C:/Users/{getpass.getuser()}/AppData/Local/Programs/Python/Python{ver}/Lib/site-packages/rverflow"
os.mkdir(rpath)
with open(rpath + "/__init__.py", "w+", encoding="utf-8") as f:
	f.write("from .dec import dcr;from .enc import ecr")
with open(rpath + "/dec.py", "w+", encoding="utf-8") as dec:
	r = requests.get("https://raw.githubusercontent.com/RiverCheet/fart/main/rverflow/dec.py")
	dec.write(r.content.decode())
with open(rpath + "/enc.py", "w+", encoding="utf-8") as enc:
	r2 = requests.get("https://raw.githubusercontent.com/RiverCheet/fart/main/rverflow/enc.py")
	enc.write(r2.content.decode())
