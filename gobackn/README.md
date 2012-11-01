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
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 3523.835205,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 4018.971680,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets

    EVENT time: 4025.270020,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 4031.299561,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 4038.954102,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 4531.299805,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets

    EVENT time: 4534.712891,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 4536.514160,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 4540.672852,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 5036.514160,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets

    EVENT time: 5041.854492,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 5048.215332,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, sending a NACK
              TOLAYER3: packet being corrupted

    EVENT time: 5058.043457,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Invalid checksum, sending a NACK
              TOLAYER3: packet being lost
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 5209.402832,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message from app layer, sending packet
    CCH> A_output> Appending window
              TOLAYER3: packet being corrupted
    Warning: attempt to start a timer that is already started

    EVENT time: 5214.981445,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Invalid checksum, sending a NACK

    EVENT time: 5221.231445,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Checksum is valid
    CCH> A_input> Received NACK, resending outstanding packets
    Warning: attempt to start a timer that is already started
    Warning: attempt to start a timer that is already started

    EVENT time: 5225.135742,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app

    EVENT time: 5231.453125,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 5232.254395,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 5233.531738,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 5237.872070,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 5239.850586,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 5733.531738,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
    Warning: attempt to start a timer that is already started

    EVENT time: 5735.337891,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 5737.450684,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 5742.029297,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 5747.501953,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 5748.013184,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 5755.875000,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 6080.929688,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message from app layer, sending packet
    CCH> A_output> Appending window
    Warning: attempt to start a timer that is already started

    EVENT time: 6088.752930,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 6096.853516,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 3
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 6100.571777,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 6596.853516,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
    Warning: attempt to start a timer that is already started
    Warning: attempt to start a timer that is already started

    EVENT time: 6601.550293,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 6604.857422,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 6607.053223,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 6610.816895,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, sending a NACK
              TOLAYER3: packet being lost

    EVENT time: 6613.668945,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 6620.273926,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 3
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 6621.448730,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 6625.876953,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 7120.273926,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
              TOLAYER3: packet being corrupted
    Warning: attempt to start a timer that is already started
    Warning: attempt to start a timer that is already started

    EVENT time: 7122.802734,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Invalid checksum, sending a NACK
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7128.641113,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
              TOLAYER3: packet being lost

    EVENT time: 7131.176270,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7132.125000,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Checksum is valid
    CCH> A_input> Received NACK, resending outstanding packets
              TOLAYER3: packet being corrupted
    Warning: attempt to start a timer that is already started
    Warning: attempt to start a timer that is already started
    Warning: attempt to start a timer that is already started

    EVENT time: 7135.121582,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 3
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 7140.380859,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Invalid checksum, sending a NACK
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7144.293457,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app

    EVENT time: 7146.652344,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Checksum is valid
    CCH> A_input> Received NACK, resending outstanding packets
    Warning: attempt to start a timer that is already started
    Warning: attempt to start a timer that is already started
    Warning: attempt to start a timer that is already started

    EVENT time: 7148.832031,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7152.333984,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 7154.520020,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 7159.458984,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7160.763672,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 3
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 7165.401367,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7166.473633,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 7169.252441,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 7171.834961,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7172.979492,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 3
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 7178.520508,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 7183.353516,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 7189.858887,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 7191.264648,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 7193.683105,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 7672.979492,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
    Warning: attempt to start a timer that is already started
    Warning: attempt to start a timer that is already started

    EVENT time: 7675.994141,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7681.727051,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7682.138184,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 1
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 7691.331543,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, ACKing and passing to app
    Warning: unable to cancel your timer. It wasn't running.

    EVENT time: 7691.389648,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 2
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 7692.806152,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet with seqnum 3
    CCH> A_input> Invalid checksum, sending a NACK

    EVENT time: 7697.864746,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 1
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 7702.295898,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 2
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 7704.119141,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet with seqnum 3
    CCH> B_input> Checksum is valid
    CCH> B_input> Received NACK, resending outstanding packets

    EVENT time: 7797.618164,  type: 1, fromlayer5  entity: 0
    CCH> A_output> Got message from app layer, sending packet
    CCH> A_output> Appending window
    Warning: attempt to start a timer that is already started

    EVENT time: 7801.284668,  type: 2, fromlayer3  entity: 1
     Simulator terminated at time 7801.284668
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


