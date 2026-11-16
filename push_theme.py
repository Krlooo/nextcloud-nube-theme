"""Pack C:/Users/Krlo/krlo/nube_theme, upload it to the StorageBox and enable it. Usage: python push_theme.py [extra shell]"""
import io
import sys
import tarfile

sys.path.insert(0, r"C:/Users/Krlo/AppData/Local/hermes/profiles/infra/cache/scratch/sbox")
from runner import run, upload  # noqa: E402

SRC = r"C:/Users/Krlo/krlo/nube_theme"
buf = io.BytesIO()
with tarfile.open(fileobj=buf, mode="w:gz") as tar:
    for sub in ("appinfo", "lib", "css", "img"):
        tar.add(f"{SRC}/{sub}", arcname=sub)
upload("nube_theme.tgz", buf.getvalue())
upload("deploy_theme.sh", open(f"{SRC}/deploy.sh", "rb").read().replace(b"\r\n", b"\n"))
extra = sys.argv[1] if len(sys.argv) > 1 else ""
print(run("#!/bin/sh\n/bin/sh $HOME/hermes/deploy_theme.sh\n" + extra + "\necho FIN\n", wait=70, max_wait=400))
