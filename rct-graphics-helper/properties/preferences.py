'''
Copyright (c) 2022 RCT Graphics Helper developers

For a complete list of all authors, please refer to the addon's meta info.
Interested in contributing? Visit https://github.com/oli414/Blender-RCT-Graphics

RCT Graphics Helper is licensed under the GNU General Public License version 3.
'''

import bpy
from bpy.types import AddonPreferences


class RCTGraphicsHelperPreferences(AddonPreferences):
    bl_idname = "rct-graphics-helper"

    orct2_object_directory: bpy.props.StringProperty(
        name="OpenRCT2 Object Folder",
        description="Directory to copy the .parkobj file to.",
        maxlen=1024,
        subtype='DIR_PATH',
        default="")

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "orct2_object_directory")
