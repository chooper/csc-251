// LAB1.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <stdio.h>
#include <cstring>
#include "altbit.h"
//#include "stdafx.h"

// The following allows this to run on Linux
#ifdef linux
#define _TCHAR char
#define scanf_s scanf
#define _tmain main
#endif

/* ******************************************************************
 ALTERNATING BIT AND GO-BACK-N NETWORK EMULATOR: VERSION 1.1  J.F.Kurose

   This code should be used for PA2, unidirectional or bidirectional
   data transfer protocols (from A to B. Bidirectional transfer of data
   is for extra credit and is not required).  Network properties:
   - one way network delay averages five time units (longer if there
     are other messages in the channel for GBN), but can be larger
   - packets can be corrupted (either the header or the data portion)
     or lost, according to user-defined probabilities
   - packets will be delivered in the order in which they were sent
     (although some can be lost).
**********************************************************************/

#define BIDIRECTIONAL 0    /* change to 1 if you're doing extra credit */
                           /* and write a routine called B_output */


/* possible events: */
#define  TIMER_INTERRUPT 0  
#define  FROM_LAYER5     1
#define  FROM_LAYER3     2

#define  OFF             0
#define  ON              1
#define   A    0
#define   B    1

#define WINDOWSIZE 20
#define MSGSIZE 20
#define TIMEOUT 500
#define ACK "ACK"
#define NACK "NACK" 

/* a "msg" is the data unit passed from layer 5 (teachers code) to layer  */
/* 4 (students' code).  It contains the data (characters) to be delivered */
/* to layer 5 via the students transport level protocol entities.         */
struct msg {
  char data[MSGSIZE];
  };

/* a packet is the data unit passed from layer 4 (students code) to layer */
/* 3 (teachers code).  Note the pre-defined packet structure, which all   */
/* students must follow. */
struct pkt {
   int seqnum;
   int acknum;
   int checksum;
   char payload[MSGSIZE];
    };

/*** START Charles Hooper's Code ***/

struct pkt_hist {
    struct pkt *packet;
    struct pkt_hist *next;
    };

struct pkt_hist *windowBase;
struct pkt_hist *windowEnd;

// Let's store last packet sent so we can resend it later
//struct pkt *last_pkt;
struct pkt *last_ack;

int calc_checksum(struct pkt *tgt_pkt)
{
    int checksum = 0;
    checksum += tgt_pkt->seqnum;
    checksum += tgt_pkt->acknum;
    for(int i = 0; i < sizeof(tgt_pkt->payload) / sizeof(char); i++)
        checksum += tgt_pkt->payload[i];
    return checksum;
}

bool pkt_checksum_valid(struct pkt *tgt_pkt)
{
    int expectedChecksum = calc_checksum(tgt_pkt);
    return (expectedChecksum == tgt_pkt->checksum);
}

struct pkt *make_pkt(int seqnum, char data[MSGSIZE])
{
    // make_pkt: Returns a pointer to a newly initialized packet
    struct pkt *gen_pkt;
    gen_pkt = new struct pkt;
    gen_pkt->seqnum = seqnum;
    gen_pkt->acknum = 0;
    for(int i = 0; i < sizeof(gen_pkt->payload) / sizeof(char); i++) {
        gen_pkt->payload[i] = data[i];
    }
    gen_pkt->checksum = calc_checksum(gen_pkt);
    return gen_pkt;
}

void send_ack(int caller, struct pkt *pkt_to_ack)
{
    int seqnum = pkt_to_ack->seqnum;
    char msg[MSGSIZE] = {'A','C','K',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    struct pkt *ack_pkt = make_pkt(seqnum, msg);
    ack_pkt->acknum = pkt_to_ack->seqnum;
    tolayer3(caller, *ack_pkt);
}


void send_nack(int caller, struct pkt *pkt_to_nack)
{
    int seqnum = pkt_to_nack->seqnum;
    char msg[MSGSIZE] = {'N','A','C','K',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    struct pkt *nack_pkt = make_pkt(seqnum, msg);
    nack_pkt->acknum = 0;
    tolayer3(caller, *nack_pkt);
}

void send_pkt(int caller, struct pkt *pkt_to_send)
{
    tolayer3(caller, *pkt_to_send);
    starttimer(caller, TIMEOUT);
}
    
/* called from layer 5, passed the data to be sent to other side */
void A_output(struct msg message)
{
    printf("CCH> A_output> Got message from app layer, sending packet\n");
    struct pkt *out_pkt;
    struct pkt_hist *currentElement;
    int seqnum;

    seqnum = windowEnd ? (windowEnd->packet->seqnum + 1) : 0;
    out_pkt = make_pkt(seqnum, message.data);

    // Build current pkt_hist element
    currentElement = new struct pkt_hist;
    currentElement->packet = out_pkt;
    currentElement->next = NULL;

    // If this is our first packet, set it as the base of the window
    if (!windowBase)
        windowBase = currentElement;

    // Append current element onto end of window sequence
    if (windowEnd)
        windowEnd->next = currentElement;
    windowEnd = currentElement;

    send_pkt(A, out_pkt);
}

void B_output(struct msg message)  /* need be completed only for extra credit */
{
    printf("CCH> B_output> Got message (noop)\n");
}

/* called from layer 3, when a packet arrives for layer 4 */
void A_input(struct pkt packet)
{
    printf("CCH> A_input> Got packet\n");
    struct pkt_hist *currWindowElement;

    // isChecksumValid
    if(pkt_checksum_valid(&packet)) {
        printf("CCH> A_input> Checksum is valid\n");

        // isACK
        if(strncmp(packet.payload, ACK, strlen(ACK)) == 0) {
            if(packet.acknum <= windowEnd->packet->seqnum) {
                printf("CCH> A_input> Packet is an ACK and valid\n");
                last_ack = &packet;
                if (windowBase) {
                    // Update window sequence to drop acknowledged packets
                    currWindowElement = windowBase;
                    while (currWindowElement && currWindowElement->next && currWindowElement->packet->seqnum < packet.acknum) {
                        // TODO: Delete old history elements
                        currWindowElement = windowBase->next;
                        windowBase = windowBase->next;
                    }
                }
                stoptimer(A);
            } else {
                // We received an ACK we don't care about
                printf("CCH> A_input> Received invalid ACK (ignoring)\n");
            }
        // isNACK
        } else if (strncmp(packet.payload, NACK, strlen(ACK)) == 0) {
            printf("CCH> A_input> Received NACK, resending outstanding packets\n");
            currWindowElement = windowBase;
            while (currWindowElement) {
                send_pkt(A, currWindowElement->packet);
                currWindowElement = currWindowElement->next;
            }
        } else {
            // Message
            printf("CCH> A_input> Packet contains a message, passing to app\n");
            stoptimer(A);
            tolayer5(A, packet.payload);
        }
    } else {
        printf("CCH> A_input> Invalid checksum, sending a NACK\n");
        send_nack(A, &packet);
        stoptimer(A);
        starttimer(A, TIMEOUT);
        return;
    }
}

/* called when A's timer goes off */
void A_timerinterrupt(void)
{
    printf("CCH> A_timerinterrupt> Called\n");
    struct pkt_hist *currWindowElement;

    if(!last_ack || (last_ack->acknum < windowEnd->packet->seqnum)) {
        printf("CCH> A_timerinterrupt> Packet timed out, resending outstanding packets\n");
        currWindowElement = windowBase;
        while (currWindowElement) {
            send_pkt(A, currWindowElement->packet);
            currWindowElement = currWindowElement->next;
        }
    }
}  

/* the following routine will be called once (only) before any other */
/* entity A routines are called. You can use it to do any initialization */
void A_init(void)
{
    printf("CCH> A_init> .\n");
    windowBase = NULL;
    windowEnd = NULL;
    //last_pkt = NULL;
    last_ack = NULL;
}

/* Note that with simplex transfer from a-to-B, there is no B_output() */

/* called from layer 3, when a packet arrives for layer 4 at B*/
void B_input(struct pkt packet)
{
    printf("CCH> B_input> Got packet\n");

    if(pkt_checksum_valid(&packet)) {
        printf("CCH> B_input> Checksum valid, sending ACK and passing message to app\n");
        // Send ACK
        send_ack(B, &packet);

        // Pass message to layer 5
        tolayer5(B, packet.payload);
    } else {
        printf("CCH> B_input> Invalid checksum! Sending NACK\n");
        send_nack(B, &packet);
    }
}

/* called when B's timer goes off */
void B_timerinterrupt(void)
{
}

/* the following rouytine will be called once (only) before any other */
/* entity B routines are called. You can use it to do any initialization */
void B_init(void)
{
}


/*** END Charles Hooper's Code ***/


/*****************************************************************
***************** NETWORK EMULATION CODE STARTS BELOW ***********
The code below emulates the layer 3 and below network environment:
  - emulates the tranmission and delivery (possibly with bit-level corruption
    and packet loss) of packets across the layer 3/4 interface
  - handles the starting/stopping of a timer, and generates timer
    interrupts (resulting in calling students timer handler).
  - generates message to be sent (passed from later 5 to 4)

THERE IS NOT REASON THAT ANY STUDENT SHOULD HAVE TO READ OR UNDERSTAND
THE CODE BELOW.  YOU SHOLD NOT TOUCH, OR REFERENCE (in your code) ANY
OF THE DATA STRUCTURES BELOW.  If you're interested in how I designed
the emulator, you're welcome to look at the code - but again, you should have
to, and you defeinitely should not have to modify
******************************************************************/

struct event {
   float evtime;           /* event time */
   int evtype;             /* event type code */
   int eventity;           /* entity where event occurs */
   struct pkt *pktptr;     /* ptr to packet (if any) assoc w/ this event */
   struct event *prev;
   struct event *next;
 };
struct event *evlist = NULL;   /* the event list */

// my function prototypes for the simulator
/*
int init(void);  
float jimsrand(void);
void generate_next_arrival(void);
void insertevent( struct event *p);
void stoptimer(int AorB);
void starttimer(int AorB,float increment);
void tolayer3(int AorB,struct pkt packet);
void tolayer5(int AorB,char datasent[]);
*/

// initialize globals
int TRACE = 1;             /* for my debugging */
int nsim = 0;              /* number of messages from 5 to 4 so far */ 
int nsimmax = 0;           /* number of msgs to generate, then stop */
float time = 0.000;
float lossprob;            /* probability that a packet is dropped  */
float corruptprob;         /* probability that one bit is packet is flipped */
float lambda;              /* arrival rate of messages from layer 5 */   
int   ntolayer3;           /* number sent into layer 3 */
int   nlost;               /* number lost in media */
int ncorrupt;              /* number corrupted by media*/



int _tmain(int argc, _TCHAR* argv[])
{
   struct event *eventptr;
   struct msg  msg2give;
   struct pkt  pkt2give;
   
   int i,j;
//   char c; 
  
   init();
   A_init();
   B_init();
   
   while (1) {
        eventptr = evlist;            /* get next event to simulate */
        if (eventptr==NULL)
           goto terminate;
        evlist = evlist->next;        /* remove this event from event list */
        if (evlist!=NULL)
           evlist->prev=NULL;
        if (TRACE>=2) {
           printf("\nEVENT time: %f,",eventptr->evtime);
           printf("  type: %d",eventptr->evtype);
           if (eventptr->evtype==0)
	       printf(", timerinterrupt  ");
             else if (eventptr->evtype==1)
               printf(", fromlayer5 ");
             else
	     printf(", fromlayer3 ");
           printf(" entity: %d\n",eventptr->eventity);
           }
        time = eventptr->evtime;        /* update time to next event time */
        if (nsim==nsimmax)
	  break;                        /* all done with simulation */
        if (eventptr->evtype == FROM_LAYER5 ) {
            generate_next_arrival();   /* set up future arrival */
            /* fill in msg to give with string of same letter */    
            j = nsim % 26; 
            for (i=0; i<20; i++)  
               msg2give.data[i] = 97 + j;
            if (TRACE>2) {
               printf("          MAINLOOP: data given to student: ");
                 for (i=0; i<20; i++) 
                  printf("%c", msg2give.data[i]);
               printf("\n");
	     }
            nsim++;
            if (eventptr->eventity == A) 
               A_output(msg2give);  
             else
               B_output(msg2give);  
            }
          else if (eventptr->evtype ==  FROM_LAYER3) {
            pkt2give.seqnum = eventptr->pktptr->seqnum;
            pkt2give.acknum = eventptr->pktptr->acknum;
            pkt2give.checksum = eventptr->pktptr->checksum;
            for (i=0; i<20; i++)  
                pkt2give.payload[i] = eventptr->pktptr->payload[i];
	    if (eventptr->eventity ==A)      /* deliver packet by calling */
   	       A_input(pkt2give);            /* appropriate entity */
            else
   	       B_input(pkt2give);
	    delete(eventptr->pktptr);          /* free the memory for packet */
            }
          else if (eventptr->evtype ==  TIMER_INTERRUPT) {
            if (eventptr->eventity == A) 
	       A_timerinterrupt();
             else
	       B_timerinterrupt();
             }
          else  {
	     printf("INTERNAL PANIC: unknown event type \n");
             }
        delete(eventptr);
        }

terminate:
   printf(" Simulator terminated at time %f\n after sending %d msgs from layer5\n",time,nsim);
   return 0;
}



int init(void)                         /* initialize the simulator */
{
  int i;
  float sum, avg;
  float jimsrand();
  
  
   printf("-----  Stop and Wait Network Simulator Version 1.1 -------- \n\n");
   printf("Enter the number of messages to simulate: ");
   scanf_s("%d",&nsimmax);
   printf("Enter  packet loss probability [enter 0.0 for no loss]:");
   scanf_s("%f",&lossprob);
   printf("Enter packet corruption probability [0.0 for no corruption]:");
   scanf_s("%f",&corruptprob);
   printf("Enter average time between messages from sender's layer5 [ > 0.0]:");
   scanf_s("%f",&lambda);
   printf("Enter TRACE:");
   scanf_s("%d",&TRACE);

   srand(9999);              /* init random number generator */
   sum = 0.0;                /* test random number generator for students */
   for (i=0; i<1000; i++)
      sum=sum+jimsrand();    /* jimsrand() should be uniform in [0,1] */
   avg = (float)(sum/1000.0);
   if (avg < 0.25 || avg > 0.75) {
    printf("It is likely that random number generation on your machine\n" ); 
    printf("is different from what this emulator expects.  Please take\n");
    printf("a look at the routine jimsrand() in the emulator code. Sorry. \n");
    return -9;
    }

   ntolayer3 = 0;
   nlost = 0;
   ncorrupt = 0;

   time=0.0;                    /* initialize time to 0.0 */
   generate_next_arrival();     /* initialize event list */
   return 0;
}

/****************************************************************************/
/* jimsrand(): return a float in range [0,1].  The routine below is used to */
/* isolate all random number generation in one location.  We assume that the*/
/* system-supplied rand() function return an int in therange [0,mmm]        */
/****************************************************************************/
float jimsrand(void) 
{
  double mmm = 2147483647;   /* largest int  - MACHINE DEPENDENT!!!!!!!!   */
  float x;                   /* individual students may need to change mmm */ 
  x = (float)(rand()/mmm);            /* x should be uniform in [0,1] */
  return(x);
}  

/********************* EVENT HANDLINE ROUTINES *******/
/*  The next set of routines handle the event list   */
/*****************************************************/
 
void generate_next_arrival(void)
{
   double x,log(),ceil();
   struct event *evptr;
    char *malloc();
//   float ttime;
//   int tempint;

   if (TRACE>2)
       printf("          GENERATE NEXT ARRIVAL: creating new arrival\n");
 
   x = lambda*jimsrand()*2;  /* x is uniform on [0,2*lambda] */
                             /* having mean of lambda        */
  // evptr = (struct event *)malloc(sizeof(struct event));
   evptr = new struct event;
   evptr->evtime =  (float)(time + x);
   evptr->evtype =  FROM_LAYER5;
   if (BIDIRECTIONAL && (jimsrand()>0.5) )
      evptr->eventity = B;
    else
      evptr->eventity = A;
   insertevent(evptr);
} 


void insertevent( struct event *p)
{
   struct event *q,*qold;

   if (TRACE>2) {
      printf("            INSERTEVENT: time is %lf\n",time);
      printf("            INSERTEVENT: future time will be %lf\n",p->evtime); 
      }
   q = evlist;     /* q points to header of list in which p struct inserted */
   if (q==NULL) {   /* list is empty */
        evlist=p;
        p->next=NULL;
        p->prev=NULL;
        }
     else {
        for (qold = q; q !=NULL && p->evtime > q->evtime; q=q->next)
              qold=q; 
        if (q==NULL) {   /* end of list */
             qold->next = p;
             p->prev = qold;
             p->next = NULL;
             }
           else if (q==evlist) { /* front of list */
             p->next=evlist;
             p->prev=NULL;
             p->next->prev=p;
             evlist = p;
             }
           else {     /* middle of list */
             p->next=q;
             p->prev=q->prev;
             q->prev->next=p;
             q->prev=p;
             }
         }
}

void printevlist(void)
{
  struct event *q;
//  int i;
  printf("--------------\nEvent List Follows:\n");
  for(q = evlist; q!=NULL; q=q->next) {
    printf("Event time: %f, type: %d entity: %d\n",q->evtime,q->evtype,q->eventity);
    }
  printf("--------------\n");
}



/********************** Student-callable ROUTINES ***********************/

/* called by students routine to cancel a previously-started timer */
void stoptimer(int AorB)
   /* A or B is trying to stop timer */
{
 struct event *q;//,*qold;

 if (TRACE>2)
    printf("          STOP TIMER: stopping timer at %f\n",time);
/* for (q=evlist; q!=NULL && q->next!=NULL; q = q->next)  */
 for (q=evlist; q!=NULL ; q = q->next) 
    if ( (q->evtype==TIMER_INTERRUPT  && q->eventity==AorB) ) { 
       /* remove this event */
       if (q->next==NULL && q->prev==NULL)
             evlist=NULL;         /* remove first and only event on list */
          else if (q->next==NULL) /* end of list - there is one in front */
             q->prev->next = NULL;
          else if (q==evlist) { /* front of list - there must be event after */
             q->next->prev=NULL;
             evlist = q->next;
             }
           else {     /* middle of list */
             q->next->prev = q->prev;
             q->prev->next =  q->next;
             }
       delete(q);
       return;
     }
  printf("Warning: unable to cancel your timer. It wasn't running.\n");
}


void starttimer(int AorB,float increment)
  /* A or B is trying to stop timer */
 
{

 struct event *q;
 struct event *evptr;
 char *malloc();

 if (TRACE>2)
    printf("          START TIMER: starting timer at %f\n",time);
 /* be nice: check to see if timer is already started, if so, then  warn */
/* for (q=evlist; q!=NULL && q->next!=NULL; q = q->next)  */
   for (q=evlist; q!=NULL ; q = q->next)  
    if ( (q->evtype==TIMER_INTERRUPT  && q->eventity==AorB) ) { 
      printf("Warning: attempt to start a timer that is already started\n");
      return;
      }
 
/* create future event for when timer goes off */
 //  evptr = (struct event *)malloc(sizeof(struct event));
   evptr = new struct event;
   evptr->evtime =  time + increment;
   evptr->evtype =  TIMER_INTERRUPT;
   evptr->eventity = AorB;
   insertevent(evptr);
} 


/************************** TOLAYER3 ***************/
void tolayer3(int AorB,struct pkt packet)
   /* A or B is trying to stop timer */
 
{
 struct pkt *mypktptr;
 struct event *evptr,*q;
 char *malloc();
 float lastime, x, jimsrand();
 int i;


 ntolayer3++;

 /* simulate losses: */
 if (jimsrand() < lossprob)  {
      nlost++;
      if (TRACE>0)    
	printf("          TOLAYER3: packet being lost\n");
      return;
    }  

/* make a copy of the packet student just gave me since he/she may decide */
/* to do something with the packet after we return back to him/her */ 
 //mypktptr = (struct pkt *)malloc(sizeof(struct pkt));
 mypktptr = new struct pkt;
 mypktptr->seqnum = packet.seqnum;
 mypktptr->acknum = packet.acknum;
 mypktptr->checksum = packet.checksum;
 for (i=0; i<20; i++)
    mypktptr->payload[i] = packet.payload[i];
 if (TRACE>2)  {
   printf("          TOLAYER3: seq: %d, ack %d, check: %d ", mypktptr->seqnum,
	  mypktptr->acknum,  mypktptr->checksum);
    for (i=0; i<20; i++)
        printf("%c",mypktptr->payload[i]);
    printf("\n");
   }

/* create future event for arrival of packet at the other side */
 // evptr = (struct event *)malloc(sizeof(struct event));
  evptr = new struct event;
  evptr->evtype =  FROM_LAYER3;   /* packet will pop out from layer3 */
  evptr->eventity = (AorB+1) % 2; /* event occurs at other entity */
  evptr->pktptr = mypktptr;       /* save ptr to my copy of packet */
/* finally, compute the arrival time of packet at the other end.
   medium can not reorder, so make sure packet arrives between 1 and 10
   time units after the latest arrival time of packets
   currently in the medium on their way to the destination */
 lastime = time;
/* for (q=evlist; q!=NULL && q->next!=NULL; q = q->next) */
 for (q=evlist; q!=NULL ; q = q->next) 
    if ( (q->evtype==FROM_LAYER3  && q->eventity==evptr->eventity) ) 
      lastime = q->evtime;
 evptr->evtime =  lastime + 1 + 9*jimsrand();
 


 /* simulate corruption: */
 if (jimsrand() < corruptprob)  {
    ncorrupt++;
    if ( (x = jimsrand()) < .75)
       mypktptr->payload[0]='Z';   /* corrupt payload */
      else if (x < .875)
       mypktptr->seqnum = 999999;
      else
       mypktptr->acknum = 999999;
    if (TRACE>0)    
	printf("          TOLAYER3: packet being corrupted\n");
    }  

  if (TRACE>2)  
     printf("          TOLAYER3: scheduling arrival on other side\n");
  insertevent(evptr);
} 

void tolayer5(int AorB,char datasent[])
{
  int i;  
  if (TRACE>2) {
     printf("          TOLAYER5: data received: ");
     for (i=0; i<20; i++)  
        printf("%c",datasent[i]);
     printf("\n");
   }
  
}

