message_arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

idx = 0
while idx < len(message_arr):
    if message_arr[idx].isdigit():
        message_arr.insert(idx, '"')
        message_arr[idx + 1] = f'{int(message_arr[idx + 1]):02}'
        message_arr.insert(idx + 2, '"')
        idx += 2

    elif (message_arr[idx].startswith('+') or message_arr[idx].startswith('-')) and \
            message_arr[idx][1:].isdigit():

        message_arr.insert(idx, '"')
        message_arr[idx + 1] = f'{message_arr[idx + 1][0]}{int(message_arr[idx + 1][1:]):02}'
        message_arr.insert(idx + 2, '"')
        idx += 2
    idx += 1

out_info = ' '.join(message_arr)  # to perfect out go to task 2
print(out_info)

# to perfect out (delete whitespaces):
# find indexes with " symbol
symbol_idxs = []
for idx, letter in enumerate(out_info):
    if letter == '"':
        symbol_idxs.append(idx)

# some logic to find delete indexes
for idx in range(len(symbol_idxs)):
    if idx % 2 == 0:
        symbol_idxs[idx] = symbol_idxs[idx] + 1
    else:
        symbol_idxs[idx] = symbol_idxs[idx] - 1

# delete indexes from original string
for del_idx in reversed(symbol_idxs):
    out_info = out_info[:del_idx] + out_info[del_idx + 1:]

print(out_info)
