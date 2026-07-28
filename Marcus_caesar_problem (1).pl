%--------------------------
% Facts
%--------------------------

% 1. Marcus was a man.
man(marcus).

% 2. Marcus was a Pompeian.
pompeian(marcus).

% 4. Caesar was a ruler.
ruler(caesar).

% 8. Marcus tried to assassinate Caesar.
tried_to_assassinate(marcus, caesar).

%--------------------------
% Rules
%--------------------------

% 3. All Pompeians are Romans.
roman(X) :-
    pompeian(X).

% 9. All men are people.
person(X) :-
    man(X).

% 6. Everyone is loyal to someone.
loyal_to(X, someone) :-
    person(X).

% 7. People only try to assassinate rulers they are not loyal to.
not_loyal_to(X, Y) :-
    person(X),
    ruler(Y),
    tried_to_assassinate(X, Y).

% 5. All Romans were either loyal to Caesar or hated him.
% If a Roman is not loyal to Caesar, then he hates Caesar.
hates(X, caesar) :-
    roman(X),
    not_loyal_to(X, caesar).

% A Roman is loyal to Caesar only if he does not hate Caesar.
loyal_to(X, caesar) :-
    roman(X),
    \+ hates(X, caesar).