import bpy
from . gp_operator import GP_KEYFRAMES_OT_create_keyframes
from . gp_panel import GP_KEYFRAMES_PL_create_keyframes_panel

bl_info = {
    "name": "GP Keyframes",
    "author": "Tihomir Selak <tknox.dr@gmail.com>",
    "version": (1, 0),
    "blender": (2, 83, 0),
    "category": "Animation",
    "location": "View3D",
    "description": "Automatic creation of animation keyframes for grease pencil.",
    "warning": "",
    "wiki_url": "https://github.com/Tihi321/gp_keyframes/blob/master/README.md",
    "tracker_url": "",
}


blender_classes = [
    GP_KEYFRAMES_OT_create_keyframes,
    GP_KEYFRAMES_PL_create_keyframes_panel
]


def register():
    bpy.types.Scene.gp_first_frame = bpy.props.IntProperty(name="First frame", default=1)
    bpy.types.Scene.gp_last_frame = bpy.props.IntProperty(name="Last frame", default=1)
    bpy.types.Scene.gp_object = bpy.props.StringProperty(name="Object")
    bpy.types.Scene.gp_layer = bpy.props.StringProperty(name="Layer")
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)


def unregister():
    del bpy.types.Scene.gp_object
    del bpy.types.Scene.gp_layer
    del bpy.types.Scene.gp_first_frame
    del bpy.types.Scene.gp_last_frame
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)
