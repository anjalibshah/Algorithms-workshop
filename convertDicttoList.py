"""
	Convert dict (which may be nested) to list.
"""

def grab_children(line_dict):
    local_list = []
    if isinstance(line_dict, dict):
        for key, value in line_dict.items():
            local_list.append(key)
            local_list.extend(grab_children(value))
    else:
        local_list.append(line_dict)
    return local_list
    
def main():
    sample_dict = {'jack': 4098, 'sape': 4139, 'nested': {'inner': 1234}}
    list_from_dict = grab_children(sample_dict)
    print list_from_dict

if __name__ == '__main__':
    main()
