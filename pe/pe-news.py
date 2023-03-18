################################################################################
# 
#                                                                               
#   /$$$$$$   /$$$$$$          /$$$$$$$   /$$$$$$  /$$  /$$  /$$  /$$$$$$$
#  /$$__  $$ /$$__  $$ /$$$$$$| $$__  $$ /$$__  $$| $$ | $$ | $$ /$$_____/
# | $$  \ $$| $$$$$$$$|______/| $$  \ $$| $$$$$$$$| $$ | $$ | $$|  $$$$$$ 
# | $$  | $$| $$_____/        | $$  | $$| $$_____/| $$ | $$ | $$ \____  $$
# | $$$$$$$/|  $$$$$$$        | $$  | $$|  $$$$$$$|  $$$$$/$$$$/ /$$$$$$$/
# | $$____/  \_______/        |__/  |__/ \_______/ \_____/\___/ |_______/ 
# | $$                                                                    
# | $$                                                                    
# |__/                                                                                       
# 
#                                                                         
# Creator: Ⓒ 0xlay (https://github.com/0xlay)
#                                                             
# License: MIT
# 
# Description: The script founds new, and deleted APIs
#                                                                                                                                                    
################################################################################

import pefile
import sys


def get_export_apis(lib: pefile.PE) -> set:
    export_apis = set()
    if hasattr(lib, 'DIRECTORY_ENTRY_EXPORT'):
        for export in lib.DIRECTORY_ENTRY_EXPORT.symbols:
            if export.name is not None:
                export_apis.add(export.name.decode('utf-8'))

    return export_apis


def get_new_apis(old_lib, new_lib) -> set:
    return get_export_apis(new_lib) - get_export_apis(old_lib)


def get_deleted_apis(old_lib, new_lib) -> set:
    return get_export_apis(old_lib) - get_export_apis(new_lib)


def show_apis(apis: set):
    for api in sorted(apis):
        print(f'{api}')


def main():
    if len(sys.argv) < 3:
        print("Invalid arguments! Try again => <old_lib> <new_lib>")
        return -1
    try:
        old_lib = pefile.PE(sys.argv[1])
        new_lib = pefile.PE(sys.argv[2])
        new_apis = get_new_apis(old_lib, new_lib)
        deleted_apis = get_deleted_apis(old_lib, new_lib)

        print('\n==========[NEW APIs]==========\n')
        show_apis(new_apis)

        print('\n==========[DELETED APIs]==========\n')
        show_apis(deleted_apis)

        print('\n==========[SUMMARY]==========\n')
        print(f'Added: {len(new_apis)} APIs')
        print(f'Deleted: {len(deleted_apis)} APIs')

    except pefile.PEFormatError as err:
        print(f'Exception: {err}')


if __name__ == "__main__":
    main()
