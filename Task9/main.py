не работает
def main(input_str):
    result = {}
    input_str = input_str.strip()[2:-2].strip()
    blocks = input_str.split('||.||') if '||.||' in input_str else input_str.split('|| . ||')
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        
        start = block.find('set{') + 4
        end = block.find('}')
        nums_str = block[start:end]
        nums = []
        for num in nums_str.split('.'):
            num = num.strip()
            if num.startswith('#'):
                nums.append(int(num[1:]))
        
        var_start = block.find('|>') + 2
        var_end = block.find(';', var_start)
        var_name = block[var_start:var_end].strip()
        
        result[var_name] = nums
    
    return result