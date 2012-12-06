//constants

#define LOOP_BACK		 0
#define NOT_CONNECTED	-1
#define UNKNOWN			-2



// Function Prototypes
void linkhandler0(int linkid, int newcost);  
void linkhandler1(int linkid, int newcost);
void linkhandler2(int linkid, int newcost);  
void linkhandler3(int linkid, int newcost);  


void rtupdate0(struct rtpkt *rcvdpkt);
void rtupdate1(struct rtpkt *rcvdpkt);
void rtupdate2(struct rtpkt *rcvdpkt);
void rtupdate3(struct rtpkt *rcvdpkt);


void rtinit0() ;
void rtinit1() ;
void rtinit2() ;
void rtinit3() ;
// Data structures

struct rtpkt {
  int sourceid;       /* id of sending router sending this pkt */
  int destid;         /* id of router to which pkt being sent 
                         (must be an immediate neighbor) */
  int mincost[4];    /* min cost to node 0 ... 3 */
  };


struct distance_table 
{
  int costs[4][4];
};


