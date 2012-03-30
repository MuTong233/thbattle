# -*- coding: utf-8 -*-
# Cards and Deck definition

from .base import *

def card_meta(clsname, bases, _dict):
    cls = type(clsname, (Card,), _dict)
    for a in ('associated_action', 'target'):
        assert hasattr(cls, a)
    Card.card_classes[clsname] = cls
    return cls

__metaclass__ = card_meta

# ==================================================

from . import basic

class AttackCard:
    associated_action = basic.Attack
    target = t_OtherOne
    distance = 1

class GrazeCard:
    associated_action = None
    target = t_None

class HealCard:
    associated_action = basic.Heal
    target = t_Self

class WineCard:
    associated_action = basic.Wine
    target = t_Self

# --------------------------------------------------

from . import spellcard

class DemolitionCard:
    associated_action = spellcard.Demolition
    target = t_OtherOne

class RejectCard:
    associated_action = None
    target = t_None

class SealingArrayCard:
    associated_action = spellcard.SealingArray
    target = t_OtherOne

class NazrinRodCard:
    associated_action = spellcard.NazrinRod
    target = t_Self

class WorshiperCard:
    associated_action = spellcard.Worshiper
    target = t_Self

class YukariDimensionCard:
    associated_action = spellcard.YukariDimension
    target = t_OtherOne
    distance = 1

class DuelCard:
    associated_action = spellcard.Duel
    target = t_OtherOne

class MapCannonCard:
    associated_action = spellcard.MapCannon
    target = t_All

class WorshipersCarnivalCard:
    associated_action = spellcard.WorshipersCarnival
    target = t_All

class FeastCard:
    associated_action = spellcard.Feast
    target = t_AllInclusive

# --------------------------------------------------

from . import equipment

class OpticalCloakCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.OpticalCloakSkill
    equipment_category = 'shield'

class GreenUFOCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.GreenUFOSkill
    equipment_category = 'greenufo'

class RedUFOCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.RedUFOSkill
    equipment_category = 'redufo'

class HakuroukenCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.HakuroukenSkill
    equipment_category = 'weapon'

class ElementalReactorCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.ElementalReactorSkill
    equipment_category = 'weapon'

class UmbrellaCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.UmbrellaSkill
    equipment_category = 'shield'

class RoukankenCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.RoukankenSkill
    equipment_category = 'weapon'

class GungnirCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.GungnirSkill
    equipment_category = 'weapon'

class LaevateinCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.LaevateinSkill
    equipment_category = 'weapon'

class ThoridalCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.ThoridalSkill
    equipment_category = 'weapon'

class RepentanceStickCard:
    associated_action = equipment.WearEquipmentAction
    target = t_Self
    equipment_skill = equipment.RepentanceStickSkill
    equipment_category = 'weapon'

# ==================================================

__metaclass__ = type

'''
card_definition = [
    (OpticalCloakCard, Card.SPADE, 1), (OpticalCloakCard, Card.SPADE, 1), (HealCard, Card.SPADE, 1), (DemolitionCard, Card.SPADE, 1),
    (OpticalCloakCard, Card.SPADE, 2), (OpticalCloakCard, Card.SPADE, 2), (HealCard, Card.SPADE, 2), (DemolitionCard, Card.SPADE, 2),
    (OpticalCloakCard, Card.SPADE, 3), (OpticalCloakCard, Card.SPADE, 3), (HealCard, Card.SPADE, 3), (DemolitionCard, Card.SPADE, 3),
    (OpticalCloakCard, Card.SPADE, 4), (OpticalCloakCard, Card.SPADE, 4), (HealCard, Card.SPADE, 4), (DemolitionCard, Card.SPADE, 4),
    (OpticalCloakCard, Card.SPADE, 5), (OpticalCloakCard, Card.SPADE, 5), (HealCard, Card.SPADE, 5), (DemolitionCard, Card.SPADE, 5),
    (OpticalCloakCard, Card.SPADE, 6), (OpticalCloakCard, Card.SPADE, 6), (HealCard, Card.SPADE, 6), (DemolitionCard, Card.SPADE, 6),
    (OpticalCloakCard, Card.SPADE, 7), (OpticalCloakCard, Card.SPADE, 7), (HealCard, Card.SPADE, 7), (DemolitionCard, Card.SPADE, 7),
    (OpticalCloakCard, Card.SPADE, 8), (OpticalCloakCard, Card.SPADE, 8), (HealCard, Card.SPADE, 8), (DemolitionCard, Card.SPADE, 8),
    (OpticalCloakCard, Card.SPADE, 9), (OpticalCloakCard, Card.SPADE, 9), (HealCard, Card.SPADE, 9), (DemolitionCard, Card.SPADE, 9),
    (OpticalCloakCard, Card.SPADE, 10), (OpticalCloakCard, Card.SPADE, 10), (HealCard, Card.SPADE, 10), (DemolitionCard, Card.SPADE, 10),
    (OpticalCloakCard, Card.SPADE, 11), (OpticalCloakCard, Card.SPADE, 11), (HealCard, Card.SPADE, 11), (DemolitionCard, Card.SPADE, 11),
    (RejectCard, Card.SPADE, 12), (RejectCard, Card.SPADE, 12), (RejectCard, Card.SPADE, 12), (RejectCard, Card.SPADE, 12),
    (RejectCard, Card.SPADE, 13), (RejectCard, Card.SPADE, 13), (RejectCard, Card.SPADE, 13), (RejectCard, Card.SPADE, 13),

    (SealingArrayCard, Card.HEART, 1), (NazrinRodCard, Card.HEART, 1), (HealCard, Card.HEART, 1), (DemolitionCard, Card.HEART, 1),
    (SealingArrayCard, Card.HEART, 2), (NazrinRodCard, Card.HEART, 2), (HealCard, Card.HEART, 2), (DemolitionCard, Card.HEART, 2),
    (SealingArrayCard, Card.HEART, 3), (NazrinRodCard, Card.HEART, 3), (HealCard, Card.HEART, 3), (DemolitionCard, Card.HEART, 3),
    (SealingArrayCard, Card.HEART, 4), (NazrinRodCard, Card.HEART, 4), (HealCard, Card.HEART, 4), (DemolitionCard, Card.HEART, 4),
    (SealingArrayCard, Card.HEART, 5), (NazrinRodCard, Card.HEART, 5), (HealCard, Card.HEART, 5), (DemolitionCard, Card.HEART, 5),
    (SealingArrayCard, Card.HEART, 6), (NazrinRodCard, Card.HEART, 6), (HealCard, Card.HEART, 6), (DemolitionCard, Card.HEART, 6),
    (SealingArrayCard, Card.HEART, 7), (NazrinRodCard, Card.HEART, 7), (HealCard, Card.HEART, 7), (DemolitionCard, Card.HEART, 7),
    (SealingArrayCard, Card.HEART, 8), (NazrinRodCard, Card.HEART, 8), (HealCard, Card.HEART, 8), (DemolitionCard, Card.HEART, 8),
    (SealingArrayCard, Card.HEART, 9), (NazrinRodCard, Card.HEART, 9), (HealCard, Card.HEART, 9), (DemolitionCard, Card.HEART, 9),
    (SealingArrayCard, Card.HEART, 10), (NazrinRodCard, Card.HEART, 10), (HealCard, Card.HEART, 10), (DemolitionCard, Card.HEART, 10),
    (SealingArrayCard, Card.HEART, 11), (NazrinRodCard, Card.HEART, 11), (HealCard, Card.HEART, 11), (DemolitionCard, Card.HEART, 11),
    (RejectCard, Card.HEART, 12), (RejectCard, Card.HEART, 12), (RejectCard, Card.HEART, 12), (RejectCard, Card.HEART, 12),
    (RejectCard, Card.HEART, 13), (RejectCard, Card.HEART, 13), (RejectCard, Card.HEART, 13), (RejectCard, Card.HEART, 13),

    (AttackCard, Card.CLUB, 1), (GrazeCard, Card.CLUB, 1), (HealCard, Card.CLUB, 1), (DemolitionCard, Card.CLUB, 1),
    (AttackCard, Card.CLUB, 2), (GrazeCard, Card.CLUB, 2), (HealCard, Card.CLUB, 2), (DemolitionCard, Card.CLUB, 2),
    (AttackCard, Card.CLUB, 3), (GrazeCard, Card.CLUB, 3), (HealCard, Card.CLUB, 3), (DemolitionCard, Card.CLUB, 3),
    (AttackCard, Card.CLUB, 4), (GrazeCard, Card.CLUB, 4), (HealCard, Card.CLUB, 4), (DemolitionCard, Card.CLUB, 4),
    (AttackCard, Card.CLUB, 5), (GrazeCard, Card.CLUB, 5), (HealCard, Card.CLUB, 5), (DemolitionCard, Card.CLUB, 5),
    (AttackCard, Card.CLUB, 6), (GrazeCard, Card.CLUB, 6), (HealCard, Card.CLUB, 6), (DemolitionCard, Card.CLUB, 6),
    (AttackCard, Card.CLUB, 7), (GrazeCard, Card.CLUB, 7), (HealCard, Card.CLUB, 7), (DemolitionCard, Card.CLUB, 7),
    (AttackCard, Card.CLUB, 8), (GrazeCard, Card.CLUB, 8), (HealCard, Card.CLUB, 8), (DemolitionCard, Card.CLUB, 8),
    (AttackCard, Card.CLUB, 9), (GrazeCard, Card.CLUB, 9), (HealCard, Card.CLUB, 9), (DemolitionCard, Card.CLUB, 9),
    (AttackCard, Card.CLUB, 10), (GrazeCard, Card.CLUB, 10), (HealCard, Card.CLUB, 10), (DemolitionCard, Card.CLUB, 10),
    (AttackCard, Card.CLUB, 11), (GrazeCard, Card.CLUB, 11), (HealCard, Card.CLUB, 11), (DemolitionCard, Card.CLUB, 11),
    (RejectCard, Card.CLUB, 12), (RejectCard, Card.CLUB, 12), (RejectCard, Card.CLUB, 12), (RejectCard, Card.CLUB, 12),
    (RejectCard, Card.CLUB, 13), (RejectCard, Card.CLUB, 13), (RejectCard, Card.CLUB, 13), (RejectCard, Card.CLUB, 13),

    (AttackCard, Card.DIAMOND, 1), (GrazeCard, Card.DIAMOND, 1), (HealCard, Card.DIAMOND, 1), (DemolitionCard, Card.DIAMOND, 1),
    (AttackCard, Card.DIAMOND, 2), (GrazeCard, Card.DIAMOND, 2), (HealCard, Card.DIAMOND, 2), (DemolitionCard, Card.DIAMOND, 2),
    (AttackCard, Card.DIAMOND, 3), (GrazeCard, Card.DIAMOND, 3), (HealCard, Card.DIAMOND, 3), (DemolitionCard, Card.DIAMOND, 3),
    (AttackCard, Card.DIAMOND, 4), (GrazeCard, Card.DIAMOND, 4), (HealCard, Card.DIAMOND, 4), (DemolitionCard, Card.DIAMOND, 4),
    (AttackCard, Card.DIAMOND, 5), (GrazeCard, Card.DIAMOND, 5), (HealCard, Card.DIAMOND, 5), (DemolitionCard, Card.DIAMOND, 5),
    (AttackCard, Card.DIAMOND, 6), (GrazeCard, Card.DIAMOND, 6), (HealCard, Card.DIAMOND, 6), (DemolitionCard, Card.DIAMOND, 6),
    (AttackCard, Card.DIAMOND, 7), (GrazeCard, Card.DIAMOND, 7), (HealCard, Card.DIAMOND, 7), (DemolitionCard, Card.DIAMOND, 7),
    (AttackCard, Card.DIAMOND, 8), (GrazeCard, Card.DIAMOND, 8), (HealCard, Card.DIAMOND, 8), (DemolitionCard, Card.DIAMOND, 8),
    (AttackCard, Card.DIAMOND, 9), (GrazeCard, Card.DIAMOND, 9), (HealCard, Card.DIAMOND, 9), (DemolitionCard, Card.DIAMOND, 9),
    (AttackCard, Card.DIAMOND, 10), (GrazeCard, Card.DIAMOND, 10), (HealCard, Card.DIAMOND, 10), (DemolitionCard, Card.DIAMOND, 10),
    (AttackCard, Card.DIAMOND, 11), (GrazeCard, Card.DIAMOND, 11), (HealCard, Card.DIAMOND, 11), (DemolitionCard, Card.DIAMOND, 11),
    (RejectCard, Card.DIAMOND, 12), (RejectCard, Card.DIAMOND, 12), (RejectCard, Card.DIAMOND, 12), (RejectCard, Card.DIAMOND, 12),
    (RejectCard, Card.DIAMOND, 13), (RejectCard, Card.DIAMOND, 13), (RejectCard, Card.DIAMOND, 13), (RejectCard, Card.DIAMOND, 13),
]
'''

card_definition = [
    (OpticalCloakCard, Card.SPADE, 1),
    (AttackCard, Card.CLUB, 1),
    (AttackCard, Card.CLUB, 3),
    (AttackCard, Card.CLUB, 5),
    (AttackCard, Card.CLUB, 1),
    (AttackCard, Card.CLUB, 3),
    (AttackCard, Card.CLUB, 5),

    (GrazeCard, Card.CLUB, 1),
    (GrazeCard, Card.CLUB, 1),
    (GrazeCard, Card.CLUB, 1),
    (HealCard, Card.CLUB, 3),
    (DemolitionCard, Card.DIAMOND, 1),
    (GreenUFOCard, Card.HEART, 3),
    (RedUFOCard, Card.DIAMOND, 4),
    (MapCannonCard, Card.SPADE, 12),
    (GungnirCard, Card.DIAMOND, 1),
    (LaevateinCard, Card.CLUB, 1),
    (ThoridalCard, Card.CLUB, 1),
    (RepentanceStickCard, Card.SPADE, 10),
    (WineCard, Card.HEART, 12),
    (FeastCard, Card.DIAMOND, 12),
    (FeastCard, Card.DIAMOND, 12),
    (FeastCard, Card.DIAMOND, 12),
    (FeastCard, Card.DIAMOND, 12),

] * 2