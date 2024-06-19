ENTRY(boot)   /* カーネルのエントリポイントはboot関数である。 */

SECTIONS {
    . = 0x80200000;   /* ベースアドレスは0x80200000である。 */
    __kernel_base = .;

    .text :{   /* コード(CPUの命令コード)領域 */
        KEEP(*(.text.boot));   /* 必ず.text.bootセクションを先頭にする。 */
        *(.text .text.*);
    }

    .rodata : ALIGN(4) {   /* 定数データ領域。読み取り専用 */
        *(.rodata .rodata.*);
    }

    .data : ALIGN(4) {   /* 読み書き可能データ領域。 */
        __bss = .;
        *(.bss .bss.* .sbss .sbss.*);
        __bss_end = .;
    }

    .bss : ALIGN(4) {   /* 読み書き可能データ領域。.dataと違い、初期値がゼロ(またはない)の変数を配置する。 */
        __bss = .;
        *(.bss .bss.* .sbss .sbss.*);
        __bss_end = .;
    }

    . = ALIGN(4);   /* ４バイト境界になるようにアドレスを調整する */
    . += 128 * 1024;   /* 現在のアドレスから128KB進める */
    __stack_top = .;

    . = ALIGN(4096);
    __free_ram = .;
    . += 64 * 1024 * 1024; /* 64MB */
    __free_ram_end = .;
}

/* memo
↓ 分かりやすいサイト
https://monoist.itmedia.co.jp/mn/articles/1003/26/news096_2.html

.rodata : ALIGN(4) のような"ALIGN(4)"は最初の時のみアライメントを行っているらしく、途中はコンパイラがやってくれるらしい。
*/
