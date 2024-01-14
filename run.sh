#!/bin/bash
set -xue

# QEMUのファイルパス
QEMU=qemu-system-riscv32

# clangのパス
CC=clang

CFLAGS="-std=c11 -O2 -g3 -Wall -Wextra --target=riscv32 -ffreestanding -nostdlib"

# カーネルをビルド
$CC $CFLAGS -Wl,-Tkernel.ld -Wl,-Map=kernel.map -o kernel.elf \
    kernel.c

# QEMUを起動
$QEMU -machine virt -bios default -nographic -serial mon:stdio --no-reboot \
    -kernel kernel.elf

# -serial mon:stdio でシリアルポートを使用して仮想マシンの標準入出力をやり取りしている