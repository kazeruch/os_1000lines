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
  init.bar1_x = 30;
  init.bar1_y = 20;
  init.bar2_x = 30;
  init.bar2_y = 20;
  init.bar_length = 10;
  init.ball_x = 50;
  init.ball_y = 35;
  init.velocity_x = 1;
  init.velocity_y = 1;
  return init;
}

void draw_game_init(struct pong *p) {
  for(int i = 0; i < p->width; i++) {
    printf("#");
  }
  printf("\n");
  for(int i = 0; i < p->height; i++) {
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
}

// 左のバーを描画しなおす
void redraw_bar1(void) {
  printf("");
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
      if (p->bar1_x > 1) {
        p->bar1_x--;
      }
      redraw_bar1();
    }

    // s が押された場合
    if (c == 's') {
      if (p->bar1_x < 29) {
        p->bar1_x++;
      }
      redraw_bar1();
    }

    // ↑ が押された場合

    // ↓ が押された場合

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
  // while(true) {
  //   check_input(&p);
  // }
}