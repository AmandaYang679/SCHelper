from itertools import chain
from rest_framework import serializers
from .models import Item
import jmespath
from apps.tierlist.infoblocks.aggregate import MedicineAggregate, AssaultRifleAggregate
from apps.tierlist.infoblocks.block import *
from apps.tierlist.infoblocks.weapon_infoblock.assault_rifle import Assault_rifle
from apps.tierlist.infoblocks.medicine import Medicine



class BaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "icon", "category", "rank")
        read_only_fields = ("id", "name", "icon", "category", "rank")


class MedicineItemSerializer(BaseItemSerializer):
    stats = serializers.SerializerMethodField()
    
    class Meta(BaseItemSerializer.Meta):
        fields = BaseItemSerializer.Meta.fields + ("stats",)
        
    def get_stats(self, obj: Item):
        aggregate = MedicineAggregate(Medicine(obj.infoblocks))
        
        stats_map = {
            "stamina": aggregate.get_stamina_bonus,
            "priority": aggregate.get_medicine_priority,
            "duration": aggregate.get_medicine_duration,
            "hp_regen": aggregate.get_medicine_hp_regen,
            "poison": aggregate.get_medicine_toxicity,
        }
        
        data = {}
        
        for key, func in stats_map.items():
            try:
                name, value = key, func()
                data[name] = value
            except Exception:
                data[key] = None

        return data
    
    
class AssaultRifleWeaponItemSerializer(BaseItemSerializer):
    stats = serializers.SerializerMethodField()
    
    class Meta(BaseItemSerializer.Meta):
        fields = BaseItemSerializer.Meta.fields + ("stats",)
        
    def get_stats(self, obj: Item):
        aggregate = AssaultRifleAggregate(Assault_rifle(obj.infoblocks))
        
        stats_map = {
            "weight": aggregate.get_weight,
            "durability": aggregate.get_durability,
            "max_durability": aggregate.get_max_durability,
            "ammo_type": aggregate.get_ammo_type,
            "damage": aggregate.get_damage,
            "clip_capacity": aggregate.get_clip_size,
            "max_distance": aggregate.get_max_distance,
            "rate_of_fire": aggregate.get_rate_of_fire,
            "reload": aggregate.get_reload_time,
            "tactical_reload": aggregate.get_tactical_reload_time,
            "spread": aggregate.get_spread,
            "hip_spread": aggregate.get_hip_fire_spread,
            "horizontal_recoil": aggregate.get_horizontal_recoil,
            "vertical_recoil": aggregate.get_vertical_recoil,
            "draw_time": aggregate.get_draw_time,
            "aiming_time": aggregate.get_aiming_time,
            "movement_speed": aggregate.get_movement_speed,
        }
    
        data = {}

        for key, func in stats_map.items():
            try:
                name, value = key, func()
                data[name] = value
            except Exception:
                data[key] = None
        
        return data
        
        