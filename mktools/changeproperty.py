import nuke

def create_panel():

    selectedNodes = nuke.selectedNodes()

    if selectedNodes:
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
            if property and value:
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
                propertyExists = False
                for node in selectedNodes:
                    if node.knob(property):
                        propertyExists = True
                        node.knob(str(property)).setValue(value)
                if not propertyExists:
                    nuke.message('The given property does not exist or cannot be found in any of the selected nodes.')
            else:
                nuke.message('A property and a value are required.')
    else:
        nuke.message('Must select the nodes to change the properties to first.')

menubar=nuke.menu("Nuke")
menu_mk = menubar.addMenu("MK Tools")
menu_mk.addCommand("Batch change property", create_panel)