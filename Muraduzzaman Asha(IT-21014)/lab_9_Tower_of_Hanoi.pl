% Base Case: If there is only 1 disk, move it directly.
move(1, Source, Dest, _) :-
 write('Move top disk from '), write(Source),
 write(' to '), write(Dest), nl.
% Recursive Step:
% N: Number of disks
% S: Source, D: Destination, A: Auxiliary
move(N, S, D, A) :-
 N > 1,
 M is N - 1,
 move(M, S, A, D), % Step 1: Move N-1 from Source to Aux
 move(1, S, D, _), % Step 2: Move largest from Source to Dest
 move(M, A, D, S). % Step 3: Move N-1 from Aux to Dest
