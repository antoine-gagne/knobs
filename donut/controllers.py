"""Controllers are the switcher elements in Donut.

They return True or False depending on their implementation.
"""

import logging

log = logging.getLogger('donut')


class DonutController(object):
    """Interface class which concrete classes must implement."""

    def __init__(self):
        """Save all important things here."""

    def is_active(self):
        """Return a bool depending on implementation."""
        raise NotImplementedError


class DonutToggle(DonutController):
    """Object defining Toggles.

    Toggles have a library-wide value.
    """

    def __init__(self, name, is_active):
        super(DonutToggle, self).__init__()
        self.name = name
        self._active = is_active

    def is_active(self):
        return self._active


class DonutFlag(DonutController):
    """Object defining Flags

    Flags values depends on how they have been configured and the current
    environment.
    """

    def __init__(self, name, conditions):
        super(DonutFlag, self).__init__()
        self.name = name
        self.conditions = conditions

    def is_active(self):
        return False

    def add_condition(self, new_condition):
        self.conditions.append(new_condition)