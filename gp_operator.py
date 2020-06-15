import bpy

class GP_KEYFRAMES_OT_create_keyframes(bpy.types.Operator):
    """Adds in between keyframes to animation"""
    bl_idname = 'gp_keyframes.create_keyframes'
    bl_label = "Create keyframes"
    bl_description = "Creates keyframes in between frames for path"

    def execute(self, context):
        print(context.scene.gp_first_frame)
        print(context.scene.gp_last_frame)
        print(context.scene.gp_object)
        print(context.scene.gp_layer)
        return {'FINISHED'}