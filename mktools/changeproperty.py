import nuke

def create_panel():

    #PANEL creation
    panel = nuke.Panel('Batch Change Property')
    # panel.setWidth(700)
    panel.addSingleLineInput('Property', '')
    panel.addSingleLineInput('Value', '')

    result = panel.show()

    if result:
    #RETRIEVE VALUES
        property = panel.value('Property')
        value = panel.value('Value')
        def valueConversion(valueToConvert):
            try:
                if valueToConvert.lower() == "true":
                    return True
                elif valueToConvert.lower() == "false":
                    return False
                else:
                    converted_value = float(valueToConvert)
                    return converted_value
            except:
                return str(valueToConvert)

        value = valueConversion(value)

        selectedNodes = nuke.selectedNodes()
        for node in selectedNodes:
            if node.knob(property):
                node.knob(str(property)).setValue(value)

menubar=nuke.menu("Nuke")
menu_mk = menubar.addMenu("MK Tools")
menu_mk.addCommand("Batch change property", create_panel)






# #PANEL creation
# panel = nuke.Panel('Batch Change Property')
# # panel.setWidth(700)
# panel.Multiline_Eval_String_Knob('Explanation of the tool','Hover over the desired property to view its name. Insert a string, float or boolean depending on the property.')
# panel.addSingleLineInput('Property', '')
# panel.addSingleLineInput('Value', '')

# result = panel.show()

# if result:
# #RETRIEVE VALUES
#     property = panel.value('Property')
#     value = panel.value('Value')
#     def valueConversion(valueToConvert):
#         try:
#             if valueToConvert.lower() == "true":
#                 return True
#             elif valueToConvert.lower() == "false":
#                 return False
#             else:
#                 converted_value = float(valueToConvert)
#                 return converted_value
#         except:
#             return str(valueToConvert)

#     value = valueConversion(value)

#     selectedNodes = nuke.selectedNodes()
#     for node in selectedNodes:
#         node.knob(str(property)).setValue(value)