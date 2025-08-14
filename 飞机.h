#include<stdio.h>>
#include<graphics.h>
#include<time.h>
IMAGE bk;
IMAGE img_role[2];
IMAGE img_bullet[2];
IMAGE img_enemy[2][2];
enum my
{
	WIDTH=480,
	HEIGHT=850,
	BULLET_NUM=15,
	BIG,
	SMALL,
	ENEMY_NUM=10
};
struct plane
{
	int x;
	int y;
	bool alive;
	int width;
	int height;
	int hp;
	int type;
}player,bull[BULLET_NUM],enemy[ENEMY_NUM];
void enemyhp(int i)
{
	if(rand()%8)
	{
		enemy[i].type=BIG;
		enemy[i].hp=3;
		enemy[i].width=103;
		enemy[i].type=148;
	}
	else
	{
		enemy[i].type=SMALL;
		enemy[i].hp=1;
		enemy[i].width=52
		enemy[i].type=39;
	}
	
		
}
void gameinit()
{
	player.x=WIDTH/2;
	player.y=HEIGHT-120;
	player.alive=true;
	for(int i=0;i<BULLET_NUM;i++)
	{
		bull[i].x=0;
		bull[i].y=0;
		bull[i].alive=false;
	}
	for(int i=0;i<ENEMY_NUM;i++)
	{
		enemy[i].alive=false;
		bull[i].x=0;
		bull[i].y=0;
		bull[i].alive=false;
	}
	
}
void loadimg()
{
	loadimage(&bk,"C:\\Users\\Administrator\\Desktop\\飞机大战背景.png");
	loadimage(&img_role[0],"C:\\Users\\Administrator\\Desktop\\飞机一.png");
	loadimage(&img_role[1],"C:\\Users\\Administrator\Desktop\\飞机二.png");
	loadimage(&img_bullet[0],"C:\\Users\\Administrator\\Desktop\\bullet1.png");
	loadimage(&img_bullet[1],"C:\\Users\\Administrator\\Desktop\\bullet2.png");
	loadimage(&img_enemy[0][0],"C:\\Users\\Administrator\\Desktop\\小敌人1.png");
	loadimage(&img_enemy[0][1],"C:\\Users\\Administrator\\Desktop\\小敌人2.png");
	loadimage(&img_enemy[1][0],"C:\\Users\\Administrator\\Desktop\\大敌人1.png");
	loadimage(&img_enemy[1][0],"C:\\Users\\Administrator\\Desktop\\大敌人2.png");
}
void gamedraw()
{
	loadimg();
	putimage(player.x,player.y,&img_role[0],NOTSRCERASE);
	putimage(player.x,HEIGHT-120,&img_role[1],SRCINVERT);
	for(int i=0;i<BULLET_NUM;i++)
	{
		if(bull[i].alive)
		{
			putimage(bull[i].x,bull[i].y,&img_bullet[0],NOTSRCERASE);
	        putimage(bull[i].x,bull[i].y,&img_bullet[1],SRCINVERT);
		}
	}
	for(int i=0;i<ENEMY_NUM;i++)
	{
		if(enemy[i].alive)
		{
			if(enemy[i].type=BIG)
			{
				putimage(enemy[i].x,enemy[i].y,&img_enemy[1][0],NOTSRCERASE);
				putimage(enemy[i].x,enemy[i].y,&img_enemy[1][1],SRCINVERT);
			}
			else
			{
				putimage(enemy[i].x,enemy[i].y,&img_enemy[0][0],NOTSRCERASE);
				putimage(enemy[i].x,enemy[i].y,&img_enemy[0][1],SRCINVERT);
			}
		}
	}
	
}
void createbullet()
{
	for(int i=0;i<BULLET_NUM;i++)
	{
		if(!bull[i].alive)
		{
			bull[i].x=player.x+80;
	        bull[i].y=player.y;
			bull[i].alive=true;
			break;
		}
	}
	
}

void bullet_move()
{
	for(int i=0;i<BULLET_NUM;i++)
	{
		if(bull[i].alive)
		{
			bull[i].y-=1;
			if(bull[i].y<0)
			{
				bull[i].alive=false;
			}
		}
	}
}
void createenemy()
{
	for(int i=0;i<ENEMY_NUM;i++)
	{
		if(!enemy[i].alive)
		{
			enemy[i].alive=true;
			enemy[i].x=rand()%(WIDTH-60);
			enemy[i].y=0;
			break;
		}
	}
}
void enemymove(int speed)
{
	for(int i=0;i<ENEMY_NUM;i++)
	{
		if(enemy[i].alive)
		{
			enemy[i].y+=speed;
			if(enemy[i].y>HEIGHT)
			{
				enemy[i].alive=false;
			}
		}
	}
}
void move(int speed)
{
	if((GetAsyncKeyState(VK_UP)||GetAsyncKeyState('w'))&&player.y>0)
	{
		player.y-=speed;
	}
	if((GetAsyncKeyState(VK_DOWN)||GetAsyncKeyState('S'))&&player.y<HEIGHT)
	{
		player.y-=speed;
	}
	if((GetAsyncKeyState(VK_LEFT)||GetAsyncKeyState('A'))&&player.x>0)
	{
		player.x-=speed;
	}
	if((GetAsyncKeyState(VK_RIGHT)||GetAsyncKeyState('D'))&&player.x<WIDTH)
	{
		player.x+=speed;
	}
	static DWORD t1=0,t2=0;
	if(GetAsyncKeyState(VK_SPACE)&&t2-t1>50)
	{
		createbullet();
		t1=t2;
	}
	t2=GetTickCount();
}
void playplane()
{
	for(int i=0;i<ENEMY_NUM;i++)
	{
		if(!enemy[i].alive)
		{
			continue;
		}
		for(int k=0;i<ENEMY_NUM;k++)
		{
			if(bull[k].x>enemy[i].x&&bull[k].x<enemy[i]+enemy[i].width&&bull[k].y>enemy[i].y&&bull[k].y<enemy[i].y+enemy[i].height)
			{
				bull[i].alive=false;
				enemy[i].hp--;
			}		
		}
		if(enemy[i].hp<=0)
		{
			enemy[i].alive=false;
		}
		
	}
}
bool time(int ms,int id)
{
	static DWORD T[10];
	if(clock()-T[10]>ms)
	{
		T[10]=clock();
		return true;
	}
	return false;
}
int main()
{
	initgraphy(WIDTH,HEIGHT,1);
	gameinit();
	gamedraw();
	BeginBatchDraw();
	while(1)
	{
		gamedraw();
		FlushBatchDraw;
		move(3);
		bullet_move();
		if(time(500,0))
		{
			createenemy();
		}
		enemymove(1);
	}
	return 0;
}