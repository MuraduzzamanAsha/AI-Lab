% --- Facts: Parent/Child Relationships ---
parent(john, mary).
parent(john, tom).
parent(mary, ann).
parent(mary, fred).
% --- Rules: Logic ---
% Sibling Rule: X and Y are siblings if they share the same parent Z,
% and X is distinct from Y.
sibling(X, Y) :-
 parent(Z, X),
 parent(Z, Y),
 X \= Y.
