import os
import nuke

def create_panel():

    def create_read_nodes(folder_path):
        created_read_nodes = []
        file_list = nuke.getFileNameList(folder_path)
        
        for seq in file_list:
            if os.path.splitext(seq)[1]:
                file_path = os.path.join(folder_path, seq)
                read_node = nuke.createNode('Read')
                read_node.knob('file').fromUserText(file_path)
                created_read_nodes.append(read_node)
        
        subfolders = [name for name in file_list if os.path.isdir(os.path.join(folder_path, name))]
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            created_read_nodes.extend(create_read_nodes(subfolder_path))
        
        return created_read_nodes

    # Create a panel
    panel = nuke.Panel('Import Image Sequence')

    # Add a folder selection knob to the panel
    panel.addFilenameSearch('Folder', '')

    # Display the panel and get user input
    if panel.show():
        folder_path = panel.value('Folder')
        
        if os.path.isdir(folder_path):
            created_nodes = create_read_nodes(folder_path)
            if created_nodes:
                nuke.message(f"Successfully created {len(created_nodes)} Read nodes.")
            else:
                nuke.message("No image sequences found.")
        else:
            nuke.message("Must select a valid folder!")

menubar=nuke.menu("Nuke")
menu_mk = menubar.addMenu("MK Tools")
menu_mk.addCommand("Import sequences recursively", create_panel)