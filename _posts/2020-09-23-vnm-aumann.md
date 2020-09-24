---
title: "VON NEUMANN-MORGENSTERN SOLUTIONS TO COOPERATIVE GAMES WITHOUT SIDE PAYMENTS"
excerpt_separator: "<!--more-->"
categories:
  - journal articles
tags:
  - Aumann
  - Peleg
  - game theory
  - good writers
---

VON NEUMANN-MORGENSTERN SOLUTIONS TO COOPERATIVE GAMES WITHOUT SIDE PAYMENTS  
BY R. J. AUMANN AND B. PELEG  
Communicated by A. W. Tucker, January 7, 1960

# First Page

In VNM's treatment of n-person games with side payments, VNM requires that:

- there be a common medium of exchange
- the side payments must be physically and legally feasible
- utility is "unrestrictedly transferable," 
i.e. that each player's utility for money
is a linear function of the amount of money

The paper tries to take a different approach to avoid the avoid the use of these restrictive side payments.

In fact, here's the entire first page quoted:

> The use of side payments in the classical 1 theory of ^-person games
involves three restrictive assumptions. First, there must be a com-
mon medium of exchange (such as money) in which the side payments
may be effected; next, the side payments must be physically and
legally feasible; and finally, it is assumed that utility is "unre-
strictedly transferable," i.e. that each player's utility for money 2 is a
linear function of the amount of money. 3 These assumptions severely
limit the applicability of the classical theory; in particular, the last
assumption has been characterized by Luce and Raiffa [2, p. 233]
as being "exceedingly restrictive—for many purposes it renders n-
person theory next to useless." It is the purpose of this paper to pre-
sent the outline of a theory that parallels the classical theory, but
makes no use of side payments.* Our definitions are related to those
given in [2, p. 234] and in [3], but whereas the previous work went
no further than proposing definitions, the theory outlined here con-
tains results which generalize a considerable portion of the classical
theory. It thus demonstrates that the restrictive side payment as-
sumption is not necessary for the development of a theory based on
the ideas of von Neumann and Morgenstern. Only a general descrip-
tion of the theory and statements of the more important theorems will
be included here; details and proofs will be published elsewhere.

Here's what it accomplishes:

- It states a fact about existing literature in a clear and concise way.
- It quotes somebody else saying that this is a problem. (Shows that there's agreement about the need for a fix)
- States the paper it's building on top of.
- Says what's new in this paper.
- Describes what the paper contains.

All on just one page.



# The meat of the paper

## Definitions of effectiveness

&alpha;-effective
: A coalition B is said to be a-effective for the payoff vector x if there
is a strategy* for B, such that for each strategy used by N—B, each mem-
ber i of B receives at least x_i.
(aka maximin)

&beta;-effective
: A coalition B is said to be &beta;-effective for the payoff vector x, if
for each strategy used by N—B, there is a strategy for B such that each
member i of B receives at least X_i.
(aka minimax)



## axiomatic treatment
An n-person "characteristic function is a set N with n members together with a function v that carreis each subset B of N insto a subset v(B) of E^N so that 
$$
\begin{gather}
    v(B) \text{ is convex} \\
    v(B) \text{ is closed} \\
    v(\varnothing) = E^N \\
    x \in v(B), y \in E^N, y_i \leq x_i \forall i \in B \implies y\in v(B) \\
    B_1, B_2 disjoint \implies v( B_1 \cup B_2 ) \supset v(B_1) \cap v(B_2) \\
\end{gather}
$$


















