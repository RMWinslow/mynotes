---
title: Fatih Rene Leon Skewness
categories: class
tags:
  - macro workshop
  - learning
---

## project

Learn to apply lasso or something liek that

annual wage earnings of individual = some function of observables

Egor sent out training sample.

RHS has lots of observables.
We need to exclude some things like hourly wage or weeks worth; too closely related.

Ranking of ML methods can change depending on size of sample.
Ensemble methods. Will be discussed in Fatih's computation class.

"Bayesian model selection". More cumbersome. Developed before machine learning.

You can use matlab or python for now. Just get your hands dirty with the data.
Don't worry about cross validation for now.

**Assignment:**
Use Lasso on the data egor sent.
1 year, cross section

## Fatih's introduction

Macro can be thought of as growth and fluctuations.

1930s report: Burns and Mitchell documented business cycle properties. Coorelations between industries, between different aggregates, etc.

Theories:
- Prescott: country hit with aggregate productivity shocks. RBC model
  - Oil prices, demand shocks, regulations, etc can be interpreted as tfp shocks.
  - Can call it a "first moment shock". Mean value of $z$ goes down.
- Friedman, Lucas, etc.: Monetary policy shocks
- Government expenditure shocks.

These are aggregate shocks. But at the micro level, we can see some fall more than others.
Recent decades models assume there are idiosyncratic shocks with certain features.
Firm size with Pareto distribution. 
Then shocks to the fat tail has aggregate effects.
Nicolos 2009. All shocks are idiosyncratic. An increase in variance of shocks across firms causes recession.
Strange idea that we can have idiosyncratic "second moment shocks" that don't wash out.

TODO: read this paper

Volkswagon spent 50 billion to compete with tesla. ID3. Didn't work.

## Rene's presentation:

[Real-Time Forward-Looking Skewness over the Business Cycle](http://www.dew-becker.org/documents/skewness.pdf) by Ian Dew-Becker.

### Big idea:
- Measure *expectations*
    - measure skwness of expected stock returns through option prices
    - MEasure skewness from firms and S&P
- Relate skewness to business cycle indicators
    - They find procyclical at firm level, no relation at aggregate S&P level
    - Firm skewness is correlated with employment, industrial growth, capactiy, utilization, and measures of credit tightness like VIX
    - Boom: heavy right tail, bust heavy left tail.

### Data sources:
- Berkely option database 1980-1995
- Optionmetrics 1996-2019
- Agg skewnewss from CME S&P 500 1983-1994 and Optionmetrics

Options are one month in advance.
restric to just 200 largest firms by market cap.

### Skewness from Option Prices

scaled third moment:

$$skew_t(x_{t+1})\equiv   \frac{E_t [(x_{t+1}-E_t x_{t+1})^3]}{E_t [(x_{t+1}-E_t x_{t+1})^2]^{3/2}}$$

Option implied skewness, following [Kozhan, Neuberger, Schneider 2013]

$$SKEW_t = 3 \frac{\int_{0}^{\infty}\left[\frac{K-F_{t}}{K^{2}F_{t}}O_{t}(K)\right]\ dK}{\int_{0}^{\infty}\left[\frac{1}{K^{2}}O_{t}(K)\right]\ dK} $$

where $O_t(K)$ is the price of an out of the money option at strike $K$ on data $t$.

Note that estimating skewness of expectations has to deal with risk premium baked in.


#### Fatih's sidenote about stock options. 

Call options insures the downside. 
Any LLC faces a similar payoff function.
This kind of payoff structure encourages risk taking.

Elon Musk had billions in personal gains from his stock options
which let him buy millions of shares at something like 70 dollars.

Put option is the mirror image of call option.

The upfront payment is set in equilibrium so that doing both loses you money in expectation.

Options create stange nonlinearities in payoff structure.