import bpy

class GP_KEYFRAMES_PL_create_keyframes_panel(bpy.types.Panel):
    bl_idname = 'gp_keyframes.create_keyframes_panel'
    bl_label = "GP Keyframes"
    bl_category = "Item"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(context.scene, 'gp_object')

        row = layout.row()
        row.prop(context.scene, 'gp_layer')

        row = layout.row(align=True)
        row.prop(data=context.scene, property='gp_first_frame', text='First')
        row.prop(data=context.scene, property='gp_last_frame', text='Last')

        row = layout.row()
        row.operator('gp_keyframes.create_keyframes', text="Add keyframes")