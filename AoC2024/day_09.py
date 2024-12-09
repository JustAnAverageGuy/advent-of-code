import aoc_helper

raw = aoc_helper.fetch(9, 2024)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    disk = []
    file_block = 1
    file_id = 0 
    for i in data:
        if file_block:
            disk.extend([file_id]*int(i))
            file_id += 1
        else:
            disk.extend("."*int(i))
        file_block = 1 - file_block
    l = 0
    r = len(disk)-1
    while l < r:
        if disk[l] != '.':
            l += 1
            continue
        if disk[r] == '.':
            r -= 1
            continue
        disk[l], disk[r] = disk[r], disk[l]
        l += 1
        r -= 1
    ans = 0
    for i in range(r+1):
        ans += disk[i] * i
    return ans



aoc_helper.lazy_test(day=9, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)

from tqdm import tqdm
def part_two(data=data):
    blocks = []
    totlen = 0
    isfile = 1
    file_idx = 0
    for i in data:
        ln = int(i)
        if isfile:
            blocks.append((totlen, totlen+ln-1, file_idx))
            file_idx += 1
        else:
            blocks.append((totlen, totlen+ln-1, -1))
        isfile = 1-isfile
        totlen += ln

    for f in tqdm(range(file_idx-1, -1, -1)):
        file_idx = None
        for i,j in enumerate(blocks):
            if j[-1] == f: file_idx = i; break
        assert file_idx is not None

        fs, fe,ff = blocks.pop(file_idx)
        f_len = fe - fs + 1

        void_idx = None
        for i,b in enumerate(blocks):
            if b[0] > fs: break
            if b[-1] == -1 and b[1]-b[0]+1 >= f_len:
                void_idx = i
                break
        if void_idx is None: 
            blocks.insert(file_idx, (fs,fe,ff))
            continue

        vs, ve, _ = blocks.pop(void_idx)

        blocks.append((vs,vs + f_len - 1, ff))
        if vs+f_len-1 != ve:
            blocks.append((vs+f_len, ve, -1))
        blocks.append((fs, fe, -1))

        ## merge any consecutive voids into a single void
        blocks.sort()
        merged_blocks = []
        for b in blocks:
            if not merged_blocks or (b[-1] != -1) or (merged_blocks[-1][-1] != -1) or (merged_blocks[-1][1] < b[0]): merged_blocks.append(b); continue
            a = merged_blocks.pop()
            merged_blocks.append((
                a[0],max(a[1],b[1]),-1
            ))
        blocks = merged_blocks[::]
    disk = []
    for bs, be, tp in blocks:
        if tp == -1:
            disk.extend([0]*(be-bs+1))
        else:
            disk.extend([tp]*(be-bs+1))
    ans = 0

    for i,j in enumerate(disk):
        ans += i * j

    return ans





        

aoc_helper.lazy_test(day=9, year=2024, parse=parse_raw, solution=part_two)

# aoc_helper.lazy_submit(day=9, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=9, year=2024, solution=part_two, data=data)
