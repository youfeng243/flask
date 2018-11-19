# encoding: utf-8
"""
@author: youfeng
@file: demo.py
@time: 2018/11/18 下午10:40
"""


def main():
    array = [4, 5, 0, 0, 0]

    sort_array = sorted(array)

    need_zero_count = 0
    have_zero_count = 0

    for index, num in enumerate(sort_array):
        if num == 0:
            have_zero_count += 1
            continue
        if index == 0:
            continue

        if sort_array[index - 1] == 0:
            continue

        need_zero_count += (sort_array[index] - sort_array[index - 1] - 1)

    if need_zero_count > have_zero_count:
        return False

    return True


if __name__ == '__main__':
    print main()
