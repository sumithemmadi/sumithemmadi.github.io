xor(0,0,0).
xor(0,1,1).
xor(1,1,0).
xor(1,0,1).

or(0,0,0).
or(0,1,1).
or(1,1,1).
or(1,0,1).

and(0,0,0).
and(0,1,0).
and(1,1,1).
and(1,0,0).

half_adder(X,Y,S,C):-
    xor(X,Y,S),
    and(X,Y,C).

full_adder(X,Y,S,C,CIN):-
    xor(X,Y,A),
    xor(A,CIN,S),
    and(CIN,A,B),
    and(X,Y,D),
    or(B,D,C)

