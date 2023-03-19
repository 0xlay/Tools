#########################################################################################################
#                                                                                
#                                                            /$$                           /$$      
#                                                           | $$                          | $$      
#   /$$$$$$   /$$$$$$           /$$$$$$$  /$$$$$$   /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$ 
#  /$$__  $$ /$$__  $$ /$$$$$$ /$$_____/ /$$__  $$ /$$_____/| $$__  $$ |____  $$ /$$_____/| $$__  $$
# | $$  \ $$| $$$$$$$$|______/|  $$$$$$ | $$$$$$$$| $$      | $$  \ $$  /$$$$$$$|  $$$$$$ | $$  \ $$
# | $$  | $$| $$_____/         \____  $$| $$_____/| $$      | $$  | $$ /$$__  $$ \____  $$| $$  | $$
# | $$$$$$$/|  $$$$$$$         /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$
# | $$____/  \_______/        |_______/  \_______/ \_______/|__/  |__/ \_______/|_______/ |__/  |__/
# | $$                                                                                              
# | $$                                                                                              
# |__/                                                                                              
#                                                                         
# Creator: Ⓒ 0xlay (https://github.com/0xlay)
#                                                             
# License: MIT
# 
# Description: The script generate hash for sections
#                                                                                                                                                    
#########################################################################################################

import pefile
import sys


def main():
    if len(sys.argv) < 2:
        print("Invalid arguments! Try again => <sample.exe>")
        return -1
    try:
        pe = pefile.PE(sys.argv[1])
        for section in pe.sections:
            print(f'{section.Name.decode("utf-8")} - { section.get_hash_md5()}',)
    except pefile.PEFormatError as err:
        print(f'Exception: {err}')


if __name__ == "__main__":
    main()
