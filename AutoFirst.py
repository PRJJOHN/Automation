from pywinauto.application import Application
app = Application(backend='uia').connect(path='D:\\bmwseat_gui_tool_v1.4\\bmwseat_gui_tool.exe')

qtdialog = app.Dialog
# qtdialog.GroupBox0.print_control_identifiers()
for anchor_child in qtdialog.children():
    if 'Group' == anchor_child.element_info.control_type:
        for anchor_intermediate in anchor_child.children():
            if 'Group' == anchor_intermediate.element_info.control_type and len(anchor_intermediate.children())>12:
                for anchor_descestor in anchor_intermediate.children():
                    if 'ComboBox' in anchor_descestor._control_types:
                        # anchor_descestor.set_focus()
                        # anchor_descestor.wait_for_idle()
                        while anchor_descestor.selected_text() != 'BLOCK':
                            anchor_descestor.select('BLOCK')
                #     print(anchor_descestor)
                # print('')
        # for list_items in child.children():
        #     for elem in list_items.children():
        #         if elem.window_text() == 'INFLATE':
        #             elem.select()
# qtdialog.print_control_identifiers()
# qtdialog.GroupBox0.GroupBox5.ComboBox2.ListBox2
# qtdialog.GroupBox0.GroupBox5.ComboBox2.ListBox2.type_keys("{HOME}{DOWN 2}{ENTER}")
# app.kill()