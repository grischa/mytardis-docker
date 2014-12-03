from tardis.settings_changeme import *

import sys
sys.path.append('/mytardis_settings')

try:
    from docker_settings import *
except:
    print 'no Docker specific MyTardis settings available'
    raise
