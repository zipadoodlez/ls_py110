def count_blocks_left(initial):
    block_count = initial
    layer_count = 0
    while block_count:
        layer_count += 1
        blocks_required = layer_count ** 2
        if block_count >= blocks_required:
            block_count -= blocks_required
        else:
            break
    return block_count


print(count_blocks_left(0) == 0)  # True
print(count_blocks_left(1) == 0)  # True
print(count_blocks_left(2) == 1)  # True
print(count_blocks_left(4) == 3)  # True
print(count_blocks_left(5) == 0)  # True
print(count_blocks_left(6) == 1)  # True
print(count_blocks_left(14) == 0) # True
