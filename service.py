''' Run all the jobs which need to be run automatically '''

# This is required to work around the ImportError exception
# "Failed to import _strptime because the import lock is held by another thread."
import _strptime

from resources.lib import utils, rpi, funcs


rpi.maybe_restore_config()

funcs.maybe_update_extlinux()

utils.maybe_confirm_installation()

utils.start_new_build_check_timer()

utils.install_cmdline_script()
