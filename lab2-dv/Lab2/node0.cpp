#include "stdafx.h"
#include "nodes.h"

void creatertpkt(struct rtpkt * initrtpkt,int srcid,int destid,int mincosts[]);
void tolayer2(struct rtpkt packet);

extern int TRACE;
extern int YES;
extern int NO;

const int ME =0;
int c_0_y[] ={LOOP_BACK,1,3,7};


struct distance_table dt0;


/* students to write the following two routines, and maybe some others */

void rtinit0() 
{
	// for all destinations: if y is not a neighbor then c(x,y) = inf
    for (int y=0;y<4;y++) dt0.costs[ME][y] = c_0_y[y];

	// for all neighbors...
    for (int  w = 0;w<4;w++)
		// ... for all destinations, initialize D_w(y) to unknown
		for (int y=0;y<4;y++)
			if(w!= ME) dt0.costs[w][y] = UNKNOWN;

	struct rtpkt my_rtpkt;

	// for each neighbor, end distance vector information
	for (int y=0;y<4;y++) 
		if ((y!=ME)&&(c_0_y[y] != NOT_CONNECTED))
		{
			creatertpkt(&my_rtpkt,ME,y,dt0.costs[ME]);
			tolayer2(my_rtpkt);
		}
}


void rtupdate0(struct rtpkt *rcvdpkt)
{
     // look at page 373 
	 // ME is x
	 // v is some other guy
	 
	 int v = rcvdpkt->sourceid;
     // On page 372, we should update my costs in dt for v
	 for(int y = 0;y<4;y++)
		 dt0.costs[v][y] = rcvdpkt->mincost[y];

	 // On page 373 this is the Bellman-Ford Equation
	 int min_Me_to_Y_through_v = 999;
	 bool changed = false;
	 for (int y = 0; y<4;y++)
	 {
		 int c_x_v = dt0.costs[ME][v];
		 int D_v_y = dt0.costs[v][y];
		 
		 if(y != ME)
		 {  // if there is a path and it is known (NOT_CONNECTED = -1) (UNKNOWN = -2)
		    if ((c_x_v>0) && (D_v_y >0))
				if(((c_x_v + D_v_y)<dt0.costs[ME][y])
					||(dt0.costs[ME][y]==NOT_CONNECTED))
				{
					dt0.costs[ME][y] = c_x_v + D_v_y;
					changed = true;
					printf("\n NODE %d found a better way to NODE %d,through NODE %d",ME,y,v);
				}
		 }

	 }

	 if(changed)
	 {
		 // Then I need to tell my neighbors, which is in c_0_y.
		  struct rtpkt my_rtpkt;

		  for (int y=0;y<4;y++) 
			if ((y!=ME)&&(c_0_y[y] != NOT_CONNECTED))
			{
				creatertpkt(&my_rtpkt,ME,y,dt0.costs[ME]);
				tolayer2(my_rtpkt);
			}
	 }
}


void printdt0(struct distance_table *dtptr)
  
{
  printf("                via     \n");
  printf("   D0 |    1     2    3 \n");
  printf("  ----|-----------------\n");
  printf("     1|  %3d   %3d   %3d\n",dtptr->costs[1][1],
	 dtptr->costs[1][2],dtptr->costs[1][3]);
  printf("dest 2|  %3d   %3d   %3d\n",dtptr->costs[2][1],
	 dtptr->costs[2][2],dtptr->costs[2][3]);
  printf("     3|  %3d   %3d   %3d\n",dtptr->costs[3][1],
	 dtptr->costs[3][2],dtptr->costs[3][3]);
}

void linkhandler0(int linkid, int newcost)   
/* called when cost from 0 to linkid changes from current value to newcost*/
/* You can leave this routine empty if you're an undergrad. If you want */
/* to use this routine, you'll need to change the value of the LINKCHANGE */
/* constant definition in prog3.c from 0 to 1 */
	
{
}
