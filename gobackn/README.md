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
    Enter TRACE:5
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 0.000000
                INSERTEVENT: future time will be 1870.573975
    CCH> A_init> .
    CCH> B_init> .

    EVENT time: 1870.573975,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 1870.573975
                INSERTEVENT: future time will be 3512.483887
              MAINLOOP: data given to student: aaaaaaaaaaaaaaaaaaaa
    CCH> A_output> Got message from app layer, sending packet
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 1870.573975
                INSERTEVENT: future time will be 1876.039062
              START TIMER: starting timer at 1870.573975
                INSERTEVENT: time is 1870.573975
                INSERTEVENT: future time will be 2370.573975

    EVENT time: 1876.039062,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 1876.039062
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 2370.573975,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 2370.573975
                INSERTEVENT: future time will be 2375.805664
              START TIMER: starting timer at 2370.573975
                INSERTEVENT: time is 2370.573975
                INSERTEVENT: future time will be 2870.573975

    EVENT time: 2375.805664,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 2375.805664
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 2870.573975,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 2870.573975
                INSERTEVENT: future time will be 2872.723877
              START TIMER: starting timer at 2870.573975
                INSERTEVENT: time is 2870.573975
                INSERTEVENT: future time will be 3370.573975

    EVENT time: 2872.723877,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 2872.723877
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 3370.573975,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 3370.573975
                INSERTEVENT: future time will be 3379.818604
              START TIMER: starting timer at 3370.573975
                INSERTEVENT: time is 3370.573975
                INSERTEVENT: future time will be 3870.573975

    EVENT time: 3379.818604,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 3379.818604
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 3512.483887,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 3512.483887
                INSERTEVENT: future time will be 3578.976318
              MAINLOOP: data given to student: bbbbbbbbbbbbbbbbbbbb
    CCH> A_output> Got message from app layer, sending packet
              TOLAYER3: seq: 1, ack 0, check: 1961 bbbbbbbbbbbbbbbbbbbb
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 3512.483887
                INSERTEVENT: future time will be 3513.962402
              START TIMER: starting timer at 3512.483887
    Warning: attempt to start a timer that is already started

    EVENT time: 3513.962402,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 3513.962402
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: bbbbbbbbbbbbbbbbbbbb

    EVENT time: 3578.976318,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 3578.976318
                INSERTEVENT: future time will be 5451.959473
              MAINLOOP: data given to student: cccccccccccccccccccc
    CCH> A_output> Got message from app layer, sending packet
              TOLAYER3: seq: 2, ack 0, check: 1982 cccccccccccccccccccc
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 3578.976318
                INSERTEVENT: future time will be 3585.274658
              START TIMER: starting timer at 3578.976318
    Warning: attempt to start a timer that is already started

    EVENT time: 3585.274658,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 3585.274658
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: cccccccccccccccccccc

    EVENT time: 3870.573975,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 3870.573975
                INSERTEVENT: future time will be 3876.603516
              START TIMER: starting timer at 3870.573975
                INSERTEVENT: time is 3870.573975
                INSERTEVENT: future time will be 4370.574219
              TOLAYER3: seq: 1, ack 0, check: 1961 bbbbbbbbbbbbbbbbbbbb
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 3870.573975
                INSERTEVENT: future time will be 3884.258057
              START TIMER: starting timer at 3870.573975
    Warning: attempt to start a timer that is already started
              TOLAYER3: seq: 2, ack 0, check: 1982 cccccccccccccccccccc
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 3870.573975
                INSERTEVENT: future time will be 3887.670898
              START TIMER: starting timer at 3870.573975
    Warning: attempt to start a timer that is already started

    EVENT time: 3876.603516,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 3876.603516
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 3884.258057,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 3884.258057
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: bbbbbbbbbbbbbbbbbbbb

    EVENT time: 3887.670898,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 3887.670898
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: cccccccccccccccccccc

    EVENT time: 4370.574219,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 4370.574219
                INSERTEVENT: future time will be 4372.375488
              START TIMER: starting timer at 4370.574219
                INSERTEVENT: time is 4370.574219
                INSERTEVENT: future time will be 4870.574219
              TOLAYER3: seq: 1, ack 0, check: 1961 bbbbbbbbbbbbbbbbbbbb
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 4370.574219
                INSERTEVENT: future time will be 4376.534180
              START TIMER: starting timer at 4370.574219
    Warning: attempt to start a timer that is already started
              TOLAYER3: seq: 2, ack 0, check: 1982 cccccccccccccccccccc
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 4370.574219
                INSERTEVENT: future time will be 4381.874512
              START TIMER: starting timer at 4370.574219
    Warning: attempt to start a timer that is already started

    EVENT time: 4372.375488,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 4372.375488
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 4376.534180,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 4376.534180
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: bbbbbbbbbbbbbbbbbbbb

    EVENT time: 4381.874512,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 4381.874512
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: cccccccccccccccccccc

    EVENT time: 4870.574219,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 4870.574219
                INSERTEVENT: future time will be 4876.935059
              START TIMER: starting timer at 4870.574219
                INSERTEVENT: time is 4870.574219
                INSERTEVENT: future time will be 5370.574219
              TOLAYER3: seq: 1, ack 0, check: 1961 bbbbbbbbbbbbbbbbbbbb
              TOLAYER3: packet being corrupted
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 4870.574219
                INSERTEVENT: future time will be 4886.763184
              START TIMER: starting timer at 4870.574219
    Warning: attempt to start a timer that is already started
              TOLAYER3: packet being lost
              START TIMER: starting timer at 4870.574219
    Warning: attempt to start a timer that is already started

    EVENT time: 4876.935059,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 4876.935059
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 4886.763184,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Invalid checksum, sending a NACK
              TOLAYER3: seq: 1, ack 0, check: 286 NACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 4886.763184
                INSERTEVENT: future time will be 4892.037109
              STOP TIMER: stopping timer at 4886.763184
    Warning: unable to cancel your timer. It wasn't running.
              START TIMER: starting timer at 4886.763184
                INSERTEVENT: time is 4886.763184
                INSERTEVENT: future time will be 5386.763184

    EVENT time: 4892.037109,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Checksum is valid
    CCH> A_input> Received NACK, resending outstanding packets
              TOLAYER3: packet being lost
              START TIMER: starting timer at 4892.037109
    Warning: attempt to start a timer that is already started
              TOLAYER3: seq: 1, ack 0, check: 1961 bbbbbbbbbbbbbbbbbbbb
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 4892.037109
                INSERTEVENT: future time will be 4900.818359
              START TIMER: starting timer at 4892.037109
    Warning: attempt to start a timer that is already started
              TOLAYER3: seq: 2, ack 0, check: 1982 cccccccccccccccccccc
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 4892.037109
                INSERTEVENT: future time will be 4902.330078
              START TIMER: starting timer at 4892.037109
    Warning: attempt to start a timer that is already started

    EVENT time: 4900.818359,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 4900.818359
              TOLAYER5: data received: bbbbbbbbbbbbbbbbbbbb

    EVENT time: 4902.330078,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 4902.330078
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: cccccccccccccccccccc

    EVENT time: 5370.574219,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5370.574219
                INSERTEVENT: future time will be 5373.452148
              START TIMER: starting timer at 5370.574219
                INSERTEVENT: time is 5370.574219
                INSERTEVENT: future time will be 5870.574219
              TOLAYER3: seq: 1, ack 0, check: 1961 bbbbbbbbbbbbbbbbbbbb
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5370.574219
                INSERTEVENT: future time will be 5377.113770
              START TIMER: starting timer at 5370.574219
    Warning: attempt to start a timer that is already started
              TOLAYER3: seq: 2, ack 0, check: 1982 cccccccccccccccccccc
              TOLAYER3: packet being corrupted
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5370.574219
                INSERTEVENT: future time will be 5386.024414
              START TIMER: starting timer at 5370.574219
    Warning: attempt to start a timer that is already started

    EVENT time: 5373.452148,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 5373.452148
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 5377.113770,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 5377.113770
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: bbbbbbbbbbbbbbbbbbbb

    EVENT time: 5386.024414,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Invalid checksum, sending a NACK
              TOLAYER3: seq: 2, ack 0, check: 287 NACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5386.024414
                INSERTEVENT: future time will be 5391.642090
              STOP TIMER: stopping timer at 5386.024414
    Warning: unable to cancel your timer. It wasn't running.
              START TIMER: starting timer at 5386.024414
                INSERTEVENT: time is 5386.024414
                INSERTEVENT: future time will be 5886.024414

    EVENT time: 5391.642090,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Checksum is valid
    CCH> A_input> Received NACK, resending outstanding packets
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5391.642090
                INSERTEVENT: future time will be 5393.620605
              START TIMER: starting timer at 5391.642090
    Warning: attempt to start a timer that is already started
              TOLAYER3: seq: 1, ack 0, check: 1961 bbbbbbbbbbbbbbbbbbbb
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5391.642090
                INSERTEVENT: future time will be 5395.426758
              START TIMER: starting timer at 5391.642090
    Warning: attempt to start a timer that is already started
              TOLAYER3: seq: 2, ack 0, check: 1982 cccccccccccccccccccc
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5391.642090
                INSERTEVENT: future time will be 5397.539551
              START TIMER: starting timer at 5391.642090
    Warning: attempt to start a timer that is already started

    EVENT time: 5393.620605,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 5393.620605
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 5395.426758,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 5395.426758
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: bbbbbbbbbbbbbbbbbbbb

    EVENT time: 5397.539551,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 5397.539551
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: cccccccccccccccccccc

    EVENT time: 5451.959473,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 5451.959473
                INSERTEVENT: future time will be 5900.190430
              MAINLOOP: data given to student: dddddddddddddddddddd
    CCH> A_output> Got message from app layer, sending packet
              TOLAYER3: seq: 3, ack 0, check: 2003 dddddddddddddddddddd
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5451.959473
                INSERTEVENT: future time will be 5458.191895
              START TIMER: starting timer at 5451.959473
    Warning: attempt to start a timer that is already started

    EVENT time: 5458.191895,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 5458.191895
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: dddddddddddddddddddd

    EVENT time: 5870.574219,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending outstanding packets
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5870.574219
                INSERTEVENT: future time will be 5873.056641
              START TIMER: starting timer at 5870.574219
                INSERTEVENT: time is 5870.574219
                INSERTEVENT: future time will be 6370.574219
              TOLAYER3: seq: 1, ack 0, check: 1961 bbbbbbbbbbbbbbbbbbbb
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5870.574219
                INSERTEVENT: future time will be 5878.443359
              START TIMER: starting timer at 5870.574219
    Warning: attempt to start a timer that is already started
              TOLAYER3: seq: 2, ack 0, check: 1982 cccccccccccccccccccc
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5870.574219
                INSERTEVENT: future time will be 5880.147461
              START TIMER: starting timer at 5870.574219
    Warning: attempt to start a timer that is already started
              TOLAYER3: seq: 3, ack 0, check: 2003 dddddddddddddddddddd
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5870.574219
                INSERTEVENT: future time will be 5887.970703
              START TIMER: starting timer at 5870.574219
    Warning: attempt to start a timer that is already started

    EVENT time: 5873.056641,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 5873.056641
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 5878.443359,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 5878.443359
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: bbbbbbbbbbbbbbbbbbbb

    EVENT time: 5880.147461,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 5880.147461
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: cccccccccccccccccccc

    EVENT time: 5887.970703,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
    CCH> B_input> Checksum is valid
    CCH> B_input> Packet contains a message, passing to app
              STOP TIMER: stopping timer at 5887.970703
    Warning: unable to cancel your timer. It wasn't running.
              TOLAYER5: data received: dddddddddddddddddddd

    EVENT time: 5900.190430,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 5900.190430
                INSERTEVENT: future time will be 7774.521484
              MAINLOOP: data given to student: eeeeeeeeeeeeeeeeeeee
    CCH> A_output> Got message from app layer, sending packet
              TOLAYER3: seq: 4, ack 0, check: 2024 eeeeeeeeeeeeeeeeeeee
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5900.190430
                INSERTEVENT: future time will be 5904.583008
              START TIMER: starting timer at 5900.190430
    Warning: attempt to start a timer that is already started

    EVENT time: 5904.583008,  type: 2, fromlayer3  entity: 1
     Simulator terminated at time 5904.583008
     after sending 5 msgs from layer5


Alternating Bit
---------------

    -----  Stop and Wait Network Simulator Version 1.1 -------- 

    Enter the number of messages to simulate: 10
    Enter  packet loss probability [enter 0.0 for no loss]:0.1
    Enter packet corruption probability [0.0 for no corruption]:0.1
    Enter average time between messages from sender's layer5 [ > 0.0]:1000
    Enter TRACE:5
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 0.000000
                INSERTEVENT: future time will be 1870.573975
    CCH> A_init> .

    EVENT time: 1870.573975,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 1870.573975
                INSERTEVENT: future time will be 3512.483887
              MAINLOOP: data given to student: aaaaaaaaaaaaaaaaaaaa
    CCH> A_output> Got message
              TOLAYER3: seq: 0, ack 0, check: 1940 aaaaaaaaaaaaaaaaaaaa
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 1870.573975
                INSERTEVENT: future time will be 1876.039062
              START TIMER: starting timer at 1870.573975
                INSERTEVENT: time is 1870.573975
                INSERTEVENT: future time will be 2370.573975

    EVENT time: 1876.039062,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 0, ack 0, check: 207 ACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 1876.039062
                INSERTEVENT: future time will be 1881.270630
              TOLAYER5: data received: aaaaaaaaaaaaaaaaaaaa

    EVENT time: 1881.270630,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Valid checksum
    CCH> A_input> Received valid ACK
              STOP TIMER: stopping timer at 1881.270630

    EVENT time: 3512.483887,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 3512.483887
                INSERTEVENT: future time will be 5209.402832
              MAINLOOP: data given to student: bbbbbbbbbbbbbbbbbbbb
    CCH> A_output> Got message
              TOLAYER3: seq: 1, ack 0, check: 1961 bbbbbbbbbbbbbbbbbbbb
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 3512.483887
                INSERTEVENT: future time will be 3514.504395
              START TIMER: starting timer at 3512.483887
                INSERTEVENT: time is 3512.483887
                INSERTEVENT: future time will be 4012.483887

    EVENT time: 3514.504395,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 1, ack 1, check: 208 ACK
              TOLAYER3: packet being corrupted
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 3514.504395
                INSERTEVENT: future time will be 3518.971680
              TOLAYER5: data received: bbbbbbbbbbbbbbbbbbbb

    EVENT time: 3518.971680,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum
              TOLAYER3: packet being lost
              STOP TIMER: stopping timer at 3518.971680
              START TIMER: starting timer at 3518.971680
                INSERTEVENT: time is 3518.971680
                INSERTEVENT: future time will be 4018.971680

    EVENT time: 4018.971680,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called

    EVENT time: 5209.402832,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 5209.402832
                INSERTEVENT: future time will be 6067.937500
              MAINLOOP: data given to student: cccccccccccccccccccc
    CCH> A_output> Got message
              TOLAYER3: seq: 0, ack 0, check: 1980 cccccccccccccccccccc
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5209.402832
                INSERTEVENT: future time will be 5214.675293
              START TIMER: starting timer at 5209.402832
                INSERTEVENT: time is 5209.402832
                INSERTEVENT: future time will be 5709.402832

    EVENT time: 5214.675293,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 0, ack 0, check: 207 ACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 5214.675293
                INSERTEVENT: future time will be 5218.877930
              TOLAYER5: data received: cccccccccccccccccccc

    EVENT time: 5218.877930,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Valid checksum
    CCH> A_input> Received valid ACK
              STOP TIMER: stopping timer at 5218.877930

    EVENT time: 6067.937500,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 6067.937500
                INSERTEVENT: future time will be 7849.862793
              MAINLOOP: data given to student: dddddddddddddddddddd
    CCH> A_output> Got message
              TOLAYER3: seq: 1, ack 0, check: 2001 dddddddddddddddddddd
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 6067.937500
                INSERTEVENT: future time will be 6075.592285
              START TIMER: starting timer at 6067.937500
                INSERTEVENT: time is 6067.937500
                INSERTEVENT: future time will be 6567.937500

    EVENT time: 6075.592285,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 1, ack 1, check: 208 ACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 6075.592285
                INSERTEVENT: future time will be 6079.005371
              TOLAYER5: data received: dddddddddddddddddddd

    EVENT time: 6079.005371,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum
              TOLAYER3: packet being lost
              STOP TIMER: stopping timer at 6079.005371
              START TIMER: starting timer at 6079.005371
                INSERTEVENT: time is 6079.005371
                INSERTEVENT: future time will be 6579.005371

    EVENT time: 6579.005371,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called

    EVENT time: 7849.862793,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 7849.862793
                INSERTEVENT: future time will be 8027.973145
              MAINLOOP: data given to student: eeeeeeeeeeeeeeeeeeee
    CCH> A_output> Got message
              TOLAYER3: seq: 0, ack 0, check: 2020 eeeeeeeeeeeeeeeeeeee
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 7849.862793
                INSERTEVENT: future time will be 7856.111816
              START TIMER: starting timer at 7849.862793
                INSERTEVENT: time is 7849.862793
                INSERTEVENT: future time will be 8349.863281

    EVENT time: 7856.111816,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 0, ack 0, check: 207 ACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 7856.111816
                INSERTEVENT: future time will be 7857.592285
              TOLAYER5: data received: eeeeeeeeeeeeeeeeeeee

    EVENT time: 7857.592285,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Valid checksum
    CCH> A_input> Received valid ACK
              STOP TIMER: stopping timer at 7857.592285

    EVENT time: 8027.973145,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 8027.973145
                INSERTEVENT: future time will be 9103.078125
              MAINLOOP: data given to student: ffffffffffffffffffff
    CCH> A_output> Got message
              TOLAYER3: seq: 1, ack 0, check: 2041 ffffffffffffffffffff
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 8027.973145
                INSERTEVENT: future time will be 8034.333984
              START TIMER: starting timer at 8027.973145
                INSERTEVENT: time is 8027.973145
                INSERTEVENT: future time will be 8527.972656

    EVENT time: 8034.333984,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: packet being lost
              TOLAYER5: data received: ffffffffffffffffffff

    EVENT time: 8527.972656,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending
              TOLAYER3: seq: 1, ack 0, check: 2041 ffffffffffffffffffff
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 8527.972656
                INSERTEVENT: future time will be 8529.031250
              START TIMER: starting timer at 8527.972656
                INSERTEVENT: time is 8527.972656
                INSERTEVENT: future time will be 9027.972656

    EVENT time: 8529.031250,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: packet being lost
              TOLAYER5: data received: ffffffffffffffffffff

    EVENT time: 9027.972656,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called
    CCH> A_timerinterrupt> Packet timed out, resending
              TOLAYER3: seq: 1, ack 0, check: 2041 ffffffffffffffffffff
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9027.972656
                INSERTEVENT: future time will be 9033.247070
              START TIMER: starting timer at 9027.972656
                INSERTEVENT: time is 9027.972656
                INSERTEVENT: future time will be 9527.972656

    EVENT time: 9033.247070,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: packet being lost
              TOLAYER5: data received: ffffffffffffffffffff

    EVENT time: 9103.078125,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 9103.078125
                INSERTEVENT: future time will be 9489.081055
              MAINLOOP: data given to student: gggggggggggggggggggg
    CCH> A_output> Got message
              TOLAYER3: seq: 0, ack 0, check: 2060 gggggggggggggggggggg
              TOLAYER3: packet being corrupted
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9103.078125
                INSERTEVENT: future time will be 9109.328125
              START TIMER: starting timer at 9103.078125
    Warning: attempt to start a timer that is already started

    EVENT time: 9109.328125,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 0, ack 0, check: 207 ACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9109.328125
                INSERTEVENT: future time will be 9114.147461
              TOLAYER5: data received: Zggggggggggggggggggg

    EVENT time: 9114.147461,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Valid checksum
    CCH> A_input> Received valid ACK
              STOP TIMER: stopping timer at 9114.147461

    EVENT time: 9489.081055,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 9489.081055
                INSERTEVENT: future time will be 10670.721680
              MAINLOOP: data given to student: hhhhhhhhhhhhhhhhhhhh
    CCH> A_output> Got message
              TOLAYER3: seq: 1, ack 0, check: 2081 hhhhhhhhhhhhhhhhhhhh
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9489.081055
                INSERTEVENT: future time will be 9492.743164
              START TIMER: starting timer at 9489.081055
                INSERTEVENT: time is 9489.081055
                INSERTEVENT: future time will be 9989.081055

    EVENT time: 9492.743164,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 1, ack 1, check: 208 ACK
              TOLAYER3: packet being corrupted
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9492.743164
                INSERTEVENT: future time will be 9501.654297
              TOLAYER5: data received: hhhhhhhhhhhhhhhhhhhh

    EVENT time: 9501.654297,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum
              TOLAYER3: seq: 1, ack 0, check: 286 NACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9501.654297
                INSERTEVENT: future time will be 9507.271484
              STOP TIMER: stopping timer at 9501.654297
              START TIMER: starting timer at 9501.654297
                INSERTEVENT: time is 9501.654297
                INSERTEVENT: future time will be 10001.654297

    EVENT time: 9507.271484,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 1, ack 1, check: 208 ACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9507.271484
                INSERTEVENT: future time will be 9509.250000
              TOLAYER5: data received: NACK

    EVENT time: 9509.250000,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum
              TOLAYER3: seq: 1, ack 0, check: 286 NACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9509.250000
                INSERTEVENT: future time will be 9511.056641
              STOP TIMER: stopping timer at 9509.250000
              START TIMER: starting timer at 9509.250000
                INSERTEVENT: time is 9509.250000
                INSERTEVENT: future time will be 10009.250000

    EVENT time: 9511.056641,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 1, ack 1, check: 208 ACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9511.056641
                INSERTEVENT: future time will be 9513.168945
              TOLAYER5: data received: NACK

    EVENT time: 9513.168945,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum
              TOLAYER3: seq: 1, ack 0, check: 286 NACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9513.168945
                INSERTEVENT: future time will be 9519.860352
              STOP TIMER: stopping timer at 9513.168945
              START TIMER: starting timer at 9513.168945
                INSERTEVENT: time is 9513.168945
                INSERTEVENT: future time will be 10013.168945

    EVENT time: 9519.860352,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 1, ack 1, check: 208 ACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9519.860352
                INSERTEVENT: future time will be 9525.333008
              TOLAYER5: data received: NACK

    EVENT time: 9525.333008,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum
              TOLAYER3: seq: 1, ack 0, check: 286 NACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9525.333008
                INSERTEVENT: future time will be 9531.317383
              STOP TIMER: stopping timer at 9525.333008
              START TIMER: starting timer at 9525.333008
                INSERTEVENT: time is 9525.333008
                INSERTEVENT: future time will be 10025.333008

    EVENT time: 9531.317383,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 1, ack 1, check: 208 ACK
              TOLAYER3: packet being corrupted
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 9531.317383
                INSERTEVENT: future time will be 9539.179688
              TOLAYER5: data received: NACK

    EVENT time: 9539.179688,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Invalid checksum
              TOLAYER3: packet being lost
              STOP TIMER: stopping timer at 9539.179688
              START TIMER: starting timer at 9539.179688
                INSERTEVENT: time is 9539.179688
                INSERTEVENT: future time will be 10039.179688

    EVENT time: 10039.179688,  type: 0, timerinterrupt   entity: 0
    CCH> A_timerinterrupt> Called

    EVENT time: 10670.721680,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 10670.721680
                INSERTEVENT: future time will be 12186.969727
              MAINLOOP: data given to student: iiiiiiiiiiiiiiiiiiii
    CCH> A_output> Got message
              TOLAYER3: seq: 0, ack 0, check: 2100 iiiiiiiiiiiiiiiiiiii
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 10670.721680
                INSERTEVENT: future time will be 10680.156250
              START TIMER: starting timer at 10670.721680
                INSERTEVENT: time is 10670.721680
                INSERTEVENT: future time will be 11170.721680

    EVENT time: 10680.156250,  type: 2, fromlayer3  entity: 1
    CCH> B_input> Got packet
              TOLAYER3: seq: 0, ack 0, check: 207 ACK
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 10680.156250
                INSERTEVENT: future time will be 10688.982422
              TOLAYER5: data received: iiiiiiiiiiiiiiiiiiii

    EVENT time: 10688.982422,  type: 2, fromlayer3  entity: 0
    CCH> A_input> Got packet
    CCH> A_input> Valid checksum
    CCH> A_input> Received valid ACK
              STOP TIMER: stopping timer at 10688.982422

    EVENT time: 12186.969727,  type: 1, fromlayer5  entity: 0
              GENERATE NEXT ARRIVAL: creating new arrival
                INSERTEVENT: time is 12186.969727
                INSERTEVENT: future time will be 13223.642578
              MAINLOOP: data given to student: jjjjjjjjjjjjjjjjjjjj
    CCH> A_output> Got message
              TOLAYER3: seq: 1, ack 0, check: 2121 jjjjjjjjjjjjjjjjjjjj
              TOLAYER3: scheduling arrival on other side
                INSERTEVENT: time is 12186.969727
                INSERTEVENT: future time will be 12191.666016
              START TIMER: starting timer at 12186.969727
                INSERTEVENT: time is 12186.969727
                INSERTEVENT: future time will be 12686.969727

    EVENT time: 12191.666016,  type: 2, fromlayer3  entity: 1
     Simulator terminated at time 12191.666016
     after sending 10 msgs from layer5

