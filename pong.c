#include "user.h"

struct pong {
  int width;
  int height;
  int bar1_x;
  int bar1_y;
  int bar2_x;
  int bar2_y;
  int bar_length;
  int ball_x;
  int ball_y;
  int velocity_x;
  int velocity_y;
};

struct pong init() {
  struct pong init;
  init.height = 30;
  init.width = 80;
  init.bar1_x = 13;
  init.bar1_y = 2;
  init.bar2_x = 13;
  init.bar2_y = 79;
  init.bar_length = 6;
  init.ball_x = 15;
  init.ball_y = 3;
  init.velocity_x = 1;
  init.velocity_y = 1;
  return init;
}

void draw_game_init(struct pong *p) {
  // 大枠を作る
  for(int i = 0; i < p->width; i++) {
    printf("#");
  }
  printf("\n");
  for(int i = 0; i < p->height-2; i++) {
    printf("#");
    for(int j = 0; j < p->width-2; j++) {
      printf(" ");
    }
    printf("#\n");
  }
  for(int i = 0; i < p->width; i++) {
    printf("#");
  }
  printf("\n");

  // ２つのバーを用意する
  for(int i = p->bar1_x; i < p->bar1_x + p->bar_length; i++) {
    printf("\033[%d;%dH|", i, p->bar1_y);
    printf("\033[%d;%dH|", i, p->bar2_y);
  }

  // ボールを用意する
  printf("\033[%d;%dHo", p->ball_x, p->ball_y);

  printf("\033[31;0H");
}

// 左のバーを描画しなおす
void redraw_bar1(struct pong *p) {
  printf("\033[%d;2H|", p->bar1_x);
  printf("\033[%d;2H ", p->bar1_x+p->bar_length);
}

// 右のバーを描画しなおす
// void redraw_bar2 {

// }

// ユーザーからの入力を受け付け、その入力に
void check_input(struct pong *p) {
  char c = getchar();
  if (c > 0) {
    // w が押された場合
    if (c == 'w') {
      if (p->bar1_x > 2) {
        p->bar1_x--;
        printf("\033[%d;2H|", p->bar1_x);
        printf("\033[%d;2H ", p->bar1_x+p->bar_length);
      }
    }

    // s が押された場合
    if (c == 's') {
      if (p->bar1_x < 24) {
        p->bar1_x++;
        printf("\033[%d;2H ", p->bar1_x-1);
        printf("\033[%d;2H|", p->bar1_x+p->bar_length-1);
      }
    }

    // o が押された場合
    if (c == 'o') {
      if (p->bar2_x > 2) {
        p->bar2_x--;
        printf("\033[%d;79H|", p->bar2_x);
        printf("\033[%d;79H ", p->bar2_x+p->bar_length);
      }
    }

    // l が押された場合
    if (c == 'l') {
      if (p->bar2_x < 24) {
        p->bar2_x++;
        printf("\033[%d;79H ", p->bar2_x-1);
        printf("\033[%d;79H|", p->bar2_x+p->bar_length-1);
      }
    }

    // sleep の代わり
    int cnt = 0;
    while(cnt < 100000) {
      cnt++;
    }
  }
}

void main(void) {
  struct pong p;
  p = init();
  printf("\033[1;1H");
  draw_game_init(&p);
  while(true) {
    check_input(&p);
  }
}