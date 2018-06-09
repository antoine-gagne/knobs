import logging

from donut.internals import DonutInternals
from donut.exceptions import DonutError
log = logging.getLogger('donut')


def create_toggle(name, active=False):
    log.debug('Called create_toggle with name {} and active value {}'.format(
        name, active))
    DonutInternals.add_toggle(name, active)

def is_toggle_active(name):
    log.debug('Called is_toggle_active with name {}'.format(name))
    toggle = DonutInternals.get_toggle(name)
    if not toggle:
        raise DonutError
    return toggle.is_active()


def create_flag(name, conditions=None):
    log.debug('Called create_flag with name {} and conditions'.format(
        name, conditions))
    if conditions is None:
        conditions = []
    DonutInternals.add_flag(name, conditions)

def is_flag_active(name):
    log.debug('Called is_flag_active with name {} and conditions'.format(name))
    flag = DonutInternals.get_flag(name)
    if not flag:
        raise DonutError
    return flag.is_active()