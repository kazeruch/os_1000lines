typedef unsigned char uint8_t; // uint8_t を１バイトの符号なし整数を表すものとして型定義
typedef unsigned int uint32_t; // uint32_t を４バイトの符号なし整数を表すものとして型定義
typedef uint32_t size_t; // size_t を32ビットアーキテクチャのときに合わせてる

extern char __bss[], __bss_end[], __stack_top[];

void *memset(void *buf, char c, size_t n) {
    uint8_t *p = (uint8_t *) buf;
    while (n--) 
        *p++ = c; // ポインタ p が指すメモリ位置に文字 c を格納し、その後にポインタ p を次のメモリ位置に進める。
    return buf;
}

void kernel_main(void) {
    memset(__bss, 0, (size_t) __bss_end - (size_t) __bss);

    for (;;);
}

__attribute__((section(".text.boot")))
__attribute__((naked)) //関数の本文の前後のプロローグとエピローグを生成しないようにする。
void boot(void) {
    __asm__ __volatile__(
        "mv sp, %[stack_top]\n"
        "j kernel_main\n" // j - jump の意。
        :
        : [stack_top] "r" (__stack_top) 
        /*
        [stack_top] - 入力オペランドの名前
        "r" - オペランドが整数レジスタに保存されていることを示す
        __stack_top - レジスタにマップする変数の名前
        */
    );
}