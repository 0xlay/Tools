################################################################################
#                                                                               
#  _______   __             ______    ______   _______   _______  
# /       \ /  |           /      \  /      \ /       \ /       \ 
# $$$$$$$  |$$/  _______  /$$$$$$  |/$$$$$$  |$$$$$$$  |$$$$$$$  |
# $$ |__$$ |/  |/       \ $$____$$ |$$ |  $$/ $$ |__$$ |$$ |__$$ |
# $$    $$< $$ |$$$$$$$  | /    $$/ $$ |      $$    $$/ $$    $$/ 
# $$$$$$$  |$$ |$$ |  $$ |/$$$$$$/  $$ |   __ $$$$$$$/  $$$$$$$/  
# $$ |__$$ |$$ |$$ |  $$ |$$ |_____ $$ \__/  |$$ |      $$ |      
# $$    $$/ $$ |$$ |  $$ |$$       |$$    $$/ $$ |      $$ |      
# $$$$$$$/  $$/ $$/   $$/ $$$$$$$$/  $$$$$$/  $$/       $$/ 
# 
#                                                                         
# Creator: Ⓒ 0xlay (https://github.com/0xlay)
#                                                             
# License: MIT
# 
# Description: The script converts a binary file to the cpp array
#                                                                                                                                                    
################################################################################

import sys


def parse_integer(bin, int_size, field_size) -> str:
    cpp_src = ""
    cnt = 0
    for i, j in zip(range(0, len(bin), int_size), range(int_size, len(bin), int_size)):
        if cnt % field_size == 0:
            cpp_src += '\n    '
        hex_str = hex(int.from_bytes(bin[i:j], 'little'))
        cpp_src += hex_str + ', '
        cpp_src += (int_size * 2 - (len(hex_str) - 2)) * ' '
        cnt += 1
    return cpp_src


def parse(bin, data_type) -> str:
    cpp_src_begin = '#include <cstdint>\n\n\n'
    cpp_src_end = ' \n};\n'

    if  data_type == 'u64':
        cpp_src_begin += 'static constexpr std::uint64_t binData[]\n{ '
        cpp_src_begin += parse_integer(bin, 8, 5)
    elif data_type == 'u32':
        cpp_src_begin += 'static constexpr std::uint32_t binData[]\n{ '
        cpp_src_begin += parse_integer(bin, 4, 10)
    elif data_type == 'u16':
        cpp_src_begin += 'static constexpr std::uint16_t binData[]\n{ '
        cpp_src_begin += parse_integer(bin, 2, 15)
    elif data_type == 'u8':
        cpp_src_begin += 'static constexpr char binData[]\n{ '
        cpp_src_begin += parse_integer(bin, 1, 20)
    else:
        cpp_src_begin += 'static constexpr char binData[]\n{'

    cpp_src_begin += cpp_src_end    
    return cpp_src_begin
    

def convert(source_path, target_path, data_type):
    bin: str

    with open(source_path, 'rb') as file:
        bin = file.read()

    src = parse(bin, data_type)

    with open(target_path, 'w') as file:
        file.write(src)


def main():
    if len(sys.argv) < 4:
        print('You must to pass 4 arguments: '
              '<bin file, target file, (u8, u16, u32, u64)>.\n'
              'Example: bin-file.exe target-file.cpp u8')
    else:
        convert(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
