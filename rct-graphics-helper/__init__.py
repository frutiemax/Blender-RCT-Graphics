'''
Copyright (c) 2022 RCT Graphics Helper developers

For a complete list of all authors, please refer to the addon's meta info.
Interested in contributing? Visit https://github.com/oli414/Blender-RCT-Graphics

RCT Graphics Helper is licensed under the GNU General Public License version 3.
'''

import traceback

from .properties.preferences import RCTGraphicsHelperPreferences
from .properties.vehicle_properties import register_vehicles_properties, unregister_vehicles_properties
from .properties.tiles_properties import register_tiles_properties, unregister_tiles_properties
from .properties.general_properties import register_general_properties, unregister_general_properties

from .rct_graphics_helper_panel import GraphicsHelperPanel
from .operators.init_operator import Init
from .operators.render_tiles_operator import RenderTiles
from .operators.vehicle_render_operator import RenderVehicle
from .properties.general_properties import GeneralProperties
from .properties.tiles_properties import TilesProperties
from .properties.vehicle_properties import VehicleProperties

from . import developer_utils
import importlib
import bpy

bl_info = {
    "name": "RCT Graphics Helper",
    "description": "Render tool to replicate RCT graphics",
    "author": "Olivier Wervers",
    "version": (0, 3, 3),
    "blender": (2, 80, 0),
    "location": "Render",
    "support": "COMMUNITY",
    "category": "Render"}

# load and reload submodules
##################################

importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(
    __path__, __name__, "bpy" in locals())

#addon preferences
class RCTGraphicsHhelperPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    object_path: bpy.props.StringProperty(name="Path:", subtype='FILE_PATH')

    def draw(self, context):
        layout = self.layout
        layout.label(text="Path to the OpenRCT2 objects folder")
        layout.prop(self, "object_path")

# register
##################################

classes = (GraphicsHelperPanel, Init, RenderTiles, RenderVehicle, GeneralProperties, TilesProperties, VehicleProperties, RCTGraphicsHhelperPreferences)
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    register_general_properties()
    register_tiles_properties()
    register_vehicles_properties()

    print("Registered {} with {} modules".format(
        bl_info["name"], len(modules)))


def unregister():
    unregister_general_properties()
    unregister_tiles_properties()
    unregister_vehicles_properties()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    print("Unregistered {}".format(bl_info["name"]))
