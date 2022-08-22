---
title: Fatih Lecture 5 Optimization
categories: class
tags:
  - worskhop
  - computation
  - optimization
---

When you estimate parameters, there will be some free ones left over.

Howe do we calibrate these floating parameters?

Empirical estimates of risk aversion have a huge range. You can pick and choose whatever you want.

New approach:
- Choose list of moments you think are important.
- Now solve optimization to search over parameter space and minimize the distance between the model and the data given these parameters.

---


## Optimization

Needed for
- Solve dynamic programming
- Root-finding as minimization
    - solving for GE
- estimation or calibbration by matching moments


### Main Trade-offs

- Fast local methods vs slow global methods
- Whether to calculate derivatives (Jacobians/Hessians)


Never use Newton's method.
It's fast and beautiful. 
But it has horrible global properties, 
doesn't bracket a minimum (serach Newton's fractals),
and is extremely slow in high dimensions.
Used as part of other algorithms, but never used alone.

In general, numerical derivatives cause issues in high-dimensional problems.

### 1D Problems


You only need two points to bracket a zero.
You need three to bracket a minimum.


Don't write your own code if a physicist already wrote it for you.

`NR's mnbrak.f90`

#### Brent's Method

`NR's brent.f90`

Always brackets a minimum. Very fast.

`NR's dbrent.f90` uses derivatives. Faster but not as reliable with certain objectives.

GNU Scientific Library
: Large scientific library with lots of examples of code.


#### Handy tip

Fit three points to a quadratic. Find the minimum of the quadratic.
Taylor's theorem says smooth functions become quadraticish then linearish at small scales.


### Higher Dimensions

Unituitive features.
You cannot visualize or plot the object.
At best you can plot some slices. These are essential but never conclusive.

If there are multiple optima (often happens), you cannot garuntee that you find the global optimum.

**Proceed with maximum caution.**

#### Local Optimizers:

- Quasi-Newton Methods: Speedy but greedy. Will get you to the optima or get stuck in a ditch. Either way, it gets there fast.
    - BFGS optimizer is the best Fatih's seen.
    - DFP Min 
- Nelder-Mead's Downhill Simplex: Slow, patient, methodical. Good global properties despite being local optimizer.
    - Like an ameba. Pretty but slow.
- BOBYQA + Derivative-free Nonlinear Least Squares (DFNLS): Newer method. Ofterntimes very fast and pretty good at finding optimum. Intermediate quality global properties.
    - Designed for MSM-like objective functions
    - Fatih's go-to algorithm.

$$min \Phi (x) = \frac{1}{2} \sum_i ...$$


[NLOPT](https://nlopt.readthedocs.io/en/latest/)
: A website with documentation for nonlinear optimization


Don't use a package if you can't see the source code.


#### Performance Evaluation

More and Wild (2009)

Performance profiles are defined in terms of a performance measure $t_{p,s} > 0$ defined for each problem $p \in P$ and solver $s \in S$

Performance ratio:

$$r_{p,s} = \frac{t_{p,s} }{\min \{t_{p,s} : s \in S\} }$$

The best solver for a problem attains ratio of 1. A solver that takes 7 times as long as the best gets a ratio of 7. A solver that never finds the minimum gets a ratio of $\infty$.



### TikTak Global Optimization

- Set counter $j=0$ and start iteration.
- Start a local optimizer from initial guess $x_j$.
- Run local optimizer until it converges to a new point $z_j$.
- Draw a quasi-random intial guess $y_j$
    - Halton's or Sobol's sequence.
- Take new

TODO: Fill this in









In high dimensional space, drawing from cartesian product of uniform variables creates a set of points that isn't uniformly distributed in the space. Big gaps. Gaps become bigger in higher dimensions.




### A little parallel programming

... without knowing any parallel programming.

Ingredients:
- Dropbox
- Friends who will let you use their computer while they are sleeping.
- Text file called wisdom.txt

[Here's the github repo](https://github.com/serdarozkan/TikTak)


























