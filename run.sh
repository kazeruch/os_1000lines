#!/bin/bash
set -xue

# QEMUのファイルパス
QEMU=qemu-system-riscv32

# clangのパス
CC=clang

CFLAGS="-std=c11 -O2 -g3 -Wall -Wextra --target=riscv32 -ffreestanding -nostdlib"

OBJCOPY=/usr/lib/llvm-14/bin/llvm-objcopy

# シェルをビルド
$CC $CFLAGS -Wl,-Tuser.ld -Wl,-Map=shell.map -o shell.elf shell.c user.c common.c
$OBJCOPY --set-section-flags .bss=alloc,contents -O binary shell.elf shell.bin
$OBJCOPY -Ibinary -Oelf32-littleriscv shell.bin shell.bin.o

# カーネルをビルド
$CC $CFLAGS -Wl,-Tkernel.ld -Wl,-Map=kernel.map -o kernel.elf \
    kernel.c common.c shell.bin.o

# QEMUを起動
$QEMU -machine virt -bios default -nographic -serial mon:stdio --no-reboot \
    -kernel kernel.elf


## memo 

# -machine virt: virtマシンとして駆動する。-machine ? オプションで対応している環境を確認できる
# -bios default: デフォルトのBIOS(ここではOpenSBI)を使用する。
# -nographic: QEMUをウィンドウなしで起動する
# -serial mon:stdio: QEMU の標準入出力を仮想マシンのシリアルポートに接続する。mon: を指定することで、QEMUモニターへの切り替えも可能になる。
# シリアルポートへの接続：仮想マシン内のゲストＯＳのシリアルデバイスと通信するためのもの。
# QEMUモニターへの接続：QEMUの管理インターフェースにアクセスし、仮想マシンの制御や設定変更を行うためのもの。
# --no-reboot: 仮想マシンがクラッシュしたら、再起動せずに停止させる（デバッグに便利）。

# -std=c11: C11を使用する。
# -O2: 最適化を有効にして、効率の良い機械語を生成する。
# -g3: デバッグ情報を最大限に出力する。
# -Wall: 主要な警告を有効にする。
# -Wextra: さらに追加の警告を有効にする。
# --target=riscv32: 32ビットRISC-V用にコンパイルする。
# -ffreestanding: ホスト環境（開発環境）の標準ライブラリを使用しない。
# -nostdlib: 標準ライブラリをリンクしない。
# -Wl, -Tkernel.ld: リンカスクリプトを指定する
# -Wl, -Map=kernel.map: マップファイル（リンカ―による配置結果）を出力する。
# -Wl, は Cコンパイラではなく、リンカ(LLD)にオプションを渡すことを意味する。

# OBJCOPY: ビルドした実行ファイル　→　生バイナリ形式