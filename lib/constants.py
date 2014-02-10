import re
import os

__scriptid__ = "script.openelec.devupdate"

try:
    ARCH = open('/etc/arch').read().rstrip()
except IOError:
    ARCH = 'RPi.arm'

UPDATE_DIR = '/storage/.update'

if ARCH == 'ATV.i386':  
    UPDATE_IMAGES = ('SYSTEM', 'MACH_KERNEL')
else:
    UPDATE_IMAGES = ('SYSTEM', 'KERNEL')

UPDATE_FILES = UPDATE_IMAGES + tuple(f + '.md5' for f in UPDATE_IMAGES)
UPDATE_PATHS = tuple(os.path.join(UPDATE_DIR, f) for f in UPDATE_FILES)

HEADERS = {'User-agent': "Mozilla/5.0"}

NOTIFY_FILE = 'installed_build.txt'

UPDATE_EXTLINUX = 'update_extlinux'

RPI_CONFIG_FILE = 'config.txt'
RPI_CONFIG_PATH = '/flash/' + RPI_CONFIG_FILE

RPI_OVERCLOCK_SETTINGS = ('arm_freq',
                          'core_freq',
                          'sdram_freq',
                          'over_voltage.*')

RPI_OVERCLOCK_RE = re.compile(r'^([ \t]*({})[ \t]*=)'.format('|'.join(RPI_OVERCLOCK_SETTINGS)),
                              re.MULTILINE)
