---
title: Cristian ELS estimators
categories: class
tags:
  - workshop
  - els
  - stats
---

- Least squares estimates have low bias but large variance.
- Mean squared error of estimator $\hat{\beta}$ is

    $$MSE(\hat{\beta}) = E(\hat{\beta}-\beta)^2$$
- Tradeoff between bias and variance.
- Our goal is to make model that has best out of sample prediction.

## Lasso shrinkage

$$\hat\beta^{lasso} = \argmin_\beta \sum_{i=1}^N (y_i - \beta_0 - \sum_{j=1}^p x_{ik}\beta_j)$$

subject to the constraint

$$\sum_{j=1}^p |\beta_j | \leq t$$

- Making t small will cause some cooefficients to be zero.
- We can tune t to minimize MSE. Helps avoid over-fitting.
- Special case: if 
  $$t_0=\sum_j^p|\hat\beta_j^{ls}|$$ 
  then lasso estimate is also least squares coefficients.


### Example prostate

Trying to predict prostate specific antigen levels.

Lowering the shrinkage factor makes variables dissapear at different times. First glesaon, than age, then lcp, etc. Cancer volume is last to dissapear.

Shrinkage sets least informative to zero, but not the smallest coefficient.

Look at fig 15.7 in Kevin Murphy book.

### Example netflix

Netflix has way more variables than data points. So OLS doesn't give meaningful results.
they need to trim the potential variables.

### Example inflation forecast

Rene Leon noticed while working for gov
that coefficients would go wild as variables grew.
Highly coorelated regressors becomes more likely as regressors goes up.


## Cross validation

When you have a free parameter, and are trying to pin it down to maximize out of sample prediciton.

Take actual sample and preten 10% of doesn't exist.

Don't quite understand the rest of the process.


When doing Lasso, you rerun at every step, get some non-zero coef, and rerun OLS using just those variables.
The Lasso process itself givs you biased estimates.

## Lasso vs Ridge

Ridge is same process but with constraint
$$\sum_j^p (\beta_j)^2$$
instead of  
$$\sum_j^p |\beta_j|$$

This leads to differences near the corner cases.

Only way to learn these data techniques is to actually use it.
Fortan, R, Python, all good choices.
R or Python can call the Fortran code.
Use it as the frontend, but code the time consuming stuff in Fortran.

Data software recomendations: 
- Split between Stata and R.

When you are on market, you want to be expert in two kinds of software.
1. Computation tool like Fortran
2. Something to manipulate data like Stata or R or Python

Anecdote: stata percentile written to be robust to ties.
Involves convoluted partitioning algorithm.
If you have data that never ties, need to write your own percentile.
Sped up code 100 times.

You can know ten different things and it won't take you anywhere.
Know one thing very well...

[Tibshirani has some examples to build off of.](https://statweb.stanford.edu/~tibs/software.html).
He has some fortran code that solves something something 173k regressors in just a few seconds.

Don't wait. **Learn Fortran now.**

