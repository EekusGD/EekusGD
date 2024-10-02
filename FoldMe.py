while True:
    import os
    import time
    print('''type if you want to remove or create a folder.
            
INSTRUCTIONS:
Type Add folder to add a folder
                
Type Remove folder if you want to remove a folder. ''')
    parent_dir = "/storage/emulated/0"
    x = input().lower()
    if x == "add folder":
        print("What would be your folder name?")
        name = input()
        parent_dir_new = "/storage/emulated/0/FoldMe"
        path = os.path.join(parent_dir_new, name)
        mkdir = os.mkdir(path)
        print("Created!")
        print()
        time.sleep(1)