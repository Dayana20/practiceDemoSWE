'''
this module encapsulates details about character types
'''

WIZARD = 'Wizard'
WARRIOR = 'Warrior'
MAGE = 'Mage'

CHAR_TYPES = {WIZARD: {"health":7}, WARRIOR: {"health":7}, MAGE: {"health":7}}


def get_char_types():
    return CHAR_TYPES
