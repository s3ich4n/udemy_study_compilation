def build_good_suffix_table(pattern):
    pattern_length = len(pattern)
    table = [pattern_length] * (pattern_length + 1)
    last_prefix_position = pattern_length

    # Step 1: Fill the table with default values
    for i in range(pattern_length, 0, -1):
        if is_prefix(pattern, i):
            last_prefix_position = i
        table[pattern_length - i] = last_prefix_position + (pattern_length - i)

    # Step 2: Fill the table with values for the "good suffix" rule
    for i in range(pattern_length):
        j = pattern_length - 1
        while j >= 0:
            if pattern[j] != pattern[i]:
                if table[j] > pattern_length - i:
                    table[j] = pattern_length - i
                break
            j -= 1

    return table

def is_prefix(pattern, position):
    subpattern_length = len(pattern) - position
    for i in range(subpattern_length):
        if pattern[i] != pattern[position + i]:
            return False
    return True

# 테스트를 위한 예시
pattern = "ababcab"
good_suffix_table = build_good_suffix_table(pattern)
print(good_suffix_table)
