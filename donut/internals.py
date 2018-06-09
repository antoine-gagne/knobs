
import logging

from donut.controllers import DonutFlag
from donut.controllers import DonutToggle


log = logging.getLogger('donut.internals')


class DonutInternals(object):
    """Stores all the delicious donut filling in this static class."""
    __variables = {}
    __flags = {}
    __toggles = {}

    @staticmethod
    def validate_key_available(name):
        name_in_vars = name in DonutInternals.__variables
        name_in_flags = name in DonutInternals.__flags
        name_in_toggles = name in DonutInternals.__toggles
        return not any([name_in_vars, name_in_flags, name_in_toggles])

    @staticmethod
    def add_variable(name, value):
        if DonutInternals.validate_key_available(name):
            DonutInternals.__variables[name] = value
        else:
            log.warning('Name already in use.')

    @staticmethod
    def add_flag(name, conditions):
        if DonutInternals.validate_key_available(name):
            new_flag = DonutFlag(name, conditions=conditions)
            DonutInternals.__flags[name] = new_flag
        else:
            log.warning('Name already in use.')

    @staticmethod
    def get_flag(name):
        return DonutInternals.__flags.get(name, None)

    @staticmethod
    def add_toggle(name, active_state):
        if DonutInternals.validate_key_available(name):
            new_toggle = DonutToggle(name, is_active=active_state)
            DonutInternals.__toggles[name] = new_toggle
        else:
            log.warning('Name already in use.')

    @staticmethod
    def get_toggle(name):
        return DonutInternals.__toggles.get(name, None)