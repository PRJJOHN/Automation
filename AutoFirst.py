from pywinauto.application import Application
## 1: upper back
## 3: middle back 1
## 7: middle back 2
## 11: middle back double
## 24: lower back
## 6,14: back side
tarPressure = [0.0,10.0,0.0,10.0,0.0,10.0,
               0.0,10.0,0.0,0.0,0.0,10.0,
               0.0,10.0,0.0,0.0,0.0,0.0,
               0.0,0.0,0.0,0.0,0.0,10.0]
valve_index = [12,13,14,15,16,17,18,19,20,21,22,23,0,1,2,3,4,5,6,7,8,9,10,11]
auto_cnt = 0
sensor_val = 0.0
error_th = 1
app = Application(backend='uia').connect(path='D:\\bmwseat_gui_tool_v1.4\\bmwseat_gui_tool.exe')
qtdialog = app.Dialog
# qtdialog.GroupBox0.print_control_identifiers()
for anchor_child in qtdialog.children():
    if 'Group' == anchor_child.element_info.control_type:
        for anchor_intermediate in anchor_child.children():
            if 'Group' == anchor_intermediate.element_info.control_type and len(anchor_intermediate.children())>12:
                for anchor_descestor in anchor_intermediate.children():
                    # print(anchor_descestor._control_types)
                    if 'ComboBox' in anchor_descestor._control_types:
                        if tarPressure[valve_index[auto_cnt]] - sensor_val > error_th and tarPressure[valve_index[auto_cnt]] != 0.0:
                            while anchor_descestor.selected_text() != 'INFLATE':
                                anchor_descestor.select('INFLATE')
                        elif tarPressure[valve_index[auto_cnt]] - sensor_val < -error_th and tarPressure[valve_index[auto_cnt]] != 0.0:
                            while anchor_descestor.selected_text() != 'DEFLATE':
                                anchor_descestor.select('DEFLATE')
                        else:
                            while anchor_descestor.selected_text() != 'BLOCK':
                                anchor_descestor.select('BLOCK')
                        # print(valve_index[auto_cnt])
                        auto_cnt = auto_cnt + 1
                    elif 'Text' in anchor_descestor._control_types:
                        sensor_val = float(anchor_descestor.window_text())
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