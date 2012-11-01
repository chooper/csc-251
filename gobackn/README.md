Alternating Bit and Go-Back-N Simulations
=========================================

Work-in-progress that's supposed to impement to Go-Back-N protocol via a
simulator. I lost alot of time trying to figure out how to get this to
compile in Linux (and also my last C++ class was 7 years ago). As a
result, some things are not as nice and straight-forward as they should
be, but I plan on continuing to improve this over time.


Go-Back-N
---------

    -----  Stop and Wait Network Simulator Version 1.1 -------- 

    Enter the number of messages to simulate: 5
    Enter  packet loss probability [enter 0.0 for no loss]:0.05
    Enter packet corruption probability [0.0 for no corruption]:0.05
    Enter average time between messages from sender's layer5 [ > 0.0]:1000
    Enter TRACE:2
    CCH> A_init> .
    CCH> B_init> .

    EVENT time: 1870.573975,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message from app layer, sending packet
    CCH> A_output> Setting A_windowbase

    EVENT time: 1876.039062,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 0
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 1881.270630,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 0
    CCH> A_input> Checksum is valid
    CCH> A_input> Packet is an ACK and valid

    EVENT time: 3512.483887,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message from app layer, sending packet
    CCH> A_output> Setting A_windowbase
    CCH> A_output> Appending window

    EVENT time: 3514.504395,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER3: packet being corrupted

    EVENT time: 3518.971680,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 4012.483887,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets

    EVENT time: 4017.347412,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 4023.645752,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 4512.483887,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets

    EVENT time: 4518.513672,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 4526.168457,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 5012.483887,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets

    EVENT time: 5015.896973,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 5017.698242,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 5209.402832,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message from app layer, sending packet
    CCH> A_output> Appending window
    Warning: attempt to start a timer that is already started

    EVENT time: 5216.604492,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 5222.442383,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 5512.483887,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
    Warning: attempt to start a timer that is already started

    EVENT time: 5522.243164,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER3: packet being lost

    EVENT time: 5523.301758,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 5528.575684,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 6012.483887,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
              TOLAYER3: packet being lost
    Warning: attempt to start a timer that is already started

    EVENT time: 6021.265137,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 6022.776855,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 6375.851562,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message from app layer, sending packet
    CCH> A_output> Appending window
    Warning: attempt to start a timer that is already started

    EVENT time: 6382.168945,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 6389.287598,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 3
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 6512.483887,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
    Warning: attempt to start a timer that is already started
    Warning: attempt to start a timer that is already started

    EVENT time: 6513.761230,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 6515.567383,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 6519.378906,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 6521.357422,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 6521.491699,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 6528.183105,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 3
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 7012.483887,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
    Warning: attempt to start a timer that is already started
    Warning: attempt to start a timer that is already started

    EVENT time: 7017.956543,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7019.480469,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 7023.940430,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7031.802246,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7033.375000,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 7042.200684,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 3
    CCH> A_input> Invalid checksum, refusing data

    EVENT time: 7224.581055,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message from app layer, sending packet
    CCH> A_output> Appending window
    Warning: attempt to start a timer that is already started

    EVENT time: 7229.277832,  type: 2, fromlayer3  entity: 1
     Simulator terminated at time 7229.277832
     after sending 5 msgs from layer5


Alternating Bit
---------------

    -----  Stop and Wait Network Simulator Version 1.1 -------- 

    Enter the number of messages to simulate: 5
    Enter  packet loss probability [enter 0.0 for no loss]:0.05
    Enter packet corruption probability [0.0 for no corruption]:0.05
    Enter average time between messages from sender's layer5 [ > 0.0]:1000 
    Enter TRACE:2
    CCH> A_init> .

    EVENT time: 1870.573975,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message

    EVENT time: 1876.039062,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet

    EVENT time: 1881.270630,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Valid checksum
    CCH> A_input> Received valid ACK

    EVENT time: 3512.483887,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message

    EVENT time: 3514.504395,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: packet being corrupted

    EVENT time: 3518.971680,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum

    EVENT time: 3523.835205,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet

    EVENT time: 3530.133545,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum

    EVENT time: 3536.163086,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet

    EVENT time: 3543.817627,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum

    EVENT time: 3547.230469,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet

    EVENT time: 3549.031982,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum

    EVENT time: 3553.190674,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet

    EVENT time: 3558.530762,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum

    EVENT time: 3564.891357,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: packet being corrupted

    EVENT time: 3574.719238,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum
              TOLAYER3: packet being lost

    EVENT time: 4074.719238,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called

    EVENT time: 5209.402832,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message
              TOLAYER3: packet being corrupted

    EVENT time: 5214.981445,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet

    EVENT time: 5221.231445,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Valid checksum
    CCH> A_input> Received valid ACK

    EVENT time: 6080.929688,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message

    EVENT time: 6085.749023,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet

    EVENT time: 6095.145020,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum

    EVENT time: 6104.377930,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: packet being lost

    EVENT time: 6194.596191,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message
    Warning: attempt to start a timer that is already started

    EVENT time: 6200.213867,  type: 2, fromlayer3  entity: 1
     Simulator terminated at time 6200.213867
     after sending 5 msgs from layer5


