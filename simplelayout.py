import argparse
import sys
import os
import scipy.io as sio
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--board_grid", type=int)
    parser.add_argument("--unit_grid", type=int)  # board_grid 能整除 unit_grid 不满足退出
    parser.add_argument("--unit_n", type=int)
    parser.add_argument("--positions", type=int, nargs="*")  # 与unit_n一致 代表每个组件的位置编号 从1开始 上限 不满足退出
    parser.add_argument("--outdir", type=str, default="example_dir")
    parser.add_argument("--file_name", type=str, default="example")

    # args = parser.parse_args('--board_grid 100 --unit_grid 10 --unit_n 3 --positions 1 15 13 --outdir dir1/dir2 --file_name example'.split())
    args = parser.parse_args()


    board_grid = args.board_grid
    unit_grid = args.unit_grid
    unit_n = args.unit_n
    positions = args.positions
    outdir = args.outdir
    file_name = args.file_name
    res = (board_grid / unit_grid)**2

    if board_grid % unit_grid != 0:
        print("board_grid 不能整除 unit_grid！")
        sys.exit()

    if len(positions) != unit_n or positions[0] != 1:
        print("positions与unit_n数量不一致或positions位置不是从1开始！")
        sys.exit()

    for position in positions:
        if position > res:
            print("超过上限！")
            sys.exit()

    print(args)
    file_name_mat = outdir + "/" + file_name + ".mat"
    file_name_jpg = outdir + "/" + file_name + ".jpg"

    os.makedirs(outdir)
    sio.savemat(file_name_mat, {})
    plt.savefig(file_name_jpg)



if __name__ == "__main__":
    main()
