import logging

from donut.internals import DonutInternals
from donut.exceptions import DonutError
log = logging.getLogger('donut')

def is_toggle_active(name):
    """Evaluate if a flag is active."""
    log.debug('Called is_toggle_active with name {}'.format(name))
    toggle = DonutInternals.get_toggle(name)
    if not toggle:
        raise DonutError
    return toggle.is_active()


def create_flag(name, conditions=None, active=False):
    log.debug('Called create_flag with name {} and conditions'.format(
        name, conditions))
    if conditions is None:
        conditions = []
    DonutInternals.add_toggle(name, active)

def create_toggle(name, active):
    pass