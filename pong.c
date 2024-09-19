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
  init.bar1_y = 3;
  init.bar2_x = 13;
  init.bar2_y = 78;
  init.bar_length = 6;
  init.ball_x = 15;
  init.ball_y = 4;
  init.velocity_x = 1;
  init.velocity_y = 1;
  return init;
}

void draw_game_init(struct pong *p) {
  // 一旦画面をクリアする
  printf("\033[2J\033[1;1H");

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
    printf("\033[%d;%dH\033[34m|", i, p->bar1_y); // 青色
    printf("\033[%d;%dH\033[32m|", i, p->bar2_y);
  }

  // ボールを用意する
  printf("\033[%d;%dH\033[33mo", p->ball_x, p->ball_y);
}

// ユーザーからの入力を受け付け、バーの位置を更新する
void update_bars(struct pong *p) {
  int ch = checkchar();
  if (ch != -1) {
    // w が押された場合、左のバーを上にずらす
    if (ch == 'w') {
      if (p->bar1_x > 2) {
        p->bar1_x--;
        printf("\033[%d;%dH\033[34m|", p->bar1_x, p->bar1_y);
        printf("\033[%d;%dH ", p->bar1_x+p->bar_length, p->bar1_y);
      }
    }

    // s が押された場合、左のバーを下にずらす
    if (ch == 's') {
      if (p->bar1_x < p->height-6) {
        p->bar1_x++;
        printf("\033[%d;%dH ", p->bar1_x-1, p->bar1_y);
        printf("\033[%d;%dH\033[34m|", p->bar1_x+p->bar_length-1, p->bar1_y);
      }
    }

    // o が押された場合、右のバーを上にずらす
    if (ch == 'o') {
      if (p->bar2_x > 2) {
        p->bar2_x--;
        printf("\033[%d;%dH\033[32m|", p->bar2_x, p->bar2_y);
        printf("\033[%d;%dH ", p->bar2_x+p->bar_length, p->bar2_y);
      }
    }

    // l が押された場合、右のバーを下にずらす
    if (ch == 'l') {
      if (p->bar2_x < p->height-6) {
        p->bar2_x++;
        printf("\033[%d;%dH ", p->bar2_x-1, p->bar2_y);
        printf("\033[%d;%dH\033[32m|", p->bar2_x+p->bar_length-1, p->bar2_y);
      }
    }
  }
}

void update_ball(struct pong *p) {
  // ボールが壁に当たった場合、速度を反転する

  // 上の壁に当たった場合
  if(p->ball_x + p->velocity_x == 1) {
    p->velocity_x = -p->velocity_x;
  }

  // 下の壁に当たった場合
  if(p->ball_x + p->velocity_x == p->height) {
    p->velocity_x = -p->velocity_x;
  }

  // 左のバーに当たった場合
  if(p->ball_y + p->velocity_y == p->bar1_y) {
    if(p->ball_x >= p->bar1_x && p->ball_x <= p->bar1_x + p->bar_length) {
      p->velocity_y = -p->velocity_y;
    }
  }

  // 右のバーに当たった場合
  if(p->ball_y + p->velocity_y == p->bar2_y) {
    if(p->ball_x >= p->bar2_x && p->ball_x <= p->bar2_x + p->bar_length) {
      p->velocity_y = -p->velocity_y;
    }
  }

  // 左の壁に当たった場合
  if(p->ball_y + p->velocity_y == 1) {
    printf("\033[32;0H%s\n", "Game Over!");
    exit();
  }

  // 右の壁に当たった場合
  if(p->ball_y + p->velocity_y == p->width) {
    printf("\033[32;0H%s\n", "Game Over!");
    exit();
  }

  // ボールの描画の更新
  printf("\033[%d;%dH ", p->ball_x, p->ball_y);
  p->ball_x = p->ball_x + p->velocity_x;
  p->ball_y = p->ball_y + p->velocity_y;
  printf("\033[%d;%dH\033[33mo", p->ball_x, p->ball_y);
}

void main(void) {
  struct pong p;

  // ゲームの設定を初期化
  p = init();

  // ゲームの初期状態を描画
  draw_game_init(&p);

  // ゲームの状態を更新
  int cnt = 0;
  while(true) {
    update_bars(&p);
    // ボールの更新速度
    cnt++;
    __asm__ __volatile__("nop");
    if(cnt % 70000 == 0) {
      cnt %= 70000;
      update_ball(&p);
    }
  }
}