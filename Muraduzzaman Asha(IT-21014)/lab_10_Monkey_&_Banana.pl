% --- Definitions ---
% state(MonkeyLocation, onFloor/onBox, BoxLocation, hasNot/has)
% 1. GRASP: If monkey is on box, at banana location, and doesn't have it.
move(state(middle, onBox, middle, hasNot), grasp, state(middle, onBox,
middle, has)).
% 2. CLIMB: If monkey is at box location on the floor.
move(state(P, onFloor, P, H), climb, state(P, onBox, P, H)).
% 3. PUSH: If monkey is at box location on floor, push to new location P2.
move(state(P1, onFloor, P1, H), push(P1, P2), state(P2, onFloor, P2, H)).
% 4. WALK: Move from P1 to P2 on the floor.
move(state(P1, onFloor, B, H), walk(P1, P2), state(P2, onFloor, B, H)).
% --- Recursive Search ---
% Goal State: The monkey has the banana.
canget(state(_, _, _, has)).
% Recursive Step: Perform a move and check if the new state leads to the
goal.
canget(State1) :-
 move(State1, _Action, State2),
 canget(State2).
