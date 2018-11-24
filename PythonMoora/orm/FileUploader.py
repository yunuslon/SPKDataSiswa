import time
import os


def file_foto(instance, filename):
    ext = filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "%s.%s" % (str(milis), ext)
    return os.path.join('gambar', filename)
