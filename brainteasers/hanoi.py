""" Towers of Hanoi.
"""
# Constants

#: character for end of lines
END_LINE = "\n"
#: string for a piece of a disk
PIECE    = "*"
#: string for a pillar
PILLAR   = "||"

# // Constants

def print_towers(towers, pillar=PILLAR, piece=PIECE, end_line=END_LINE):
    """ Print the towers of hanoi state.

        :param list tower: the state of the towers
        :param str pillar: how to print an empty part of a tower
        :param str piece: how to print a part of a disk
        :param str end_line: how to print end of a line
    """
    len_towers = len(towers)
    highest    = 0
    longest    = 0
    for tower in range(len_towers):
        highest += len(towers[tower])
        try:
            longest = max(longest, towers[tower][0] * 2)  # start is correct
        except IndexError:
            pass

    rows = []
    while highest:
        row = ""
        for tower in range(len_towers):
            pil = ""
            try:
                size = towers[tower][highest - 1] * 2
                pil += piece * size
            except IndexError:
                pil = pillar
            row += pil.center(longest)
        rows.append(row)
        highest -= 1

    print(end_line + end_line.join(rows))
    print(towers)


def hanoi(disk_size, towers, src, dst, tmp):
    """ Move a disk of <size> from <sr> to <dst> passing by <tmp>.

        :param int disk_size: size of the disk to move
        :param list towers: current state of the towers
        :param int src: where is the disk to move
        :parma int dst: where to move the disk
        :param int tmp: what tower to use for temporary move
    """
    if disk_size > 0:
        # move the smallest disks to the temp tower
        hanoi(disk_size - 1, towers, src, tmp, dst)
        # move the disk to the destination
        if towers[src]:
            towers[dst].append(towers[src].pop())
            print_towers(towers)
        # move the smaller from the tmp tower to the destination
        hanoi(disk_size - 1, towers, tmp, dst, src)


def main():
    """ To avoid constants.
    """
    towers = ([6, 5, 4, 3, 2, 1], [], [])
    hanoi(len(towers[0]), towers, 0, 2, 1)


if __name__ == "__main__":
    main()
