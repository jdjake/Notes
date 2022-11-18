# Chapter 14: Unemployment and Fiscal Policy

Some periods of capitalist history are highly volatile (e.g. the Great Depression and the Great Recession), and others not so much (e.g. the post WW2 era, or the period of *great moderation* between the cold war and the great recession). Why is this so? In this unit, we determine to what extent *government investment* during the last century influenced the volatility of the economy.

As we discussed in the previous chapter, the investment of firms is purely motivated by post-tax profits, which leads to spending in clusters, because firms tends to adopt the same technologies at the same times, and tend to have the same beliefs about expected future demand of products. A useful tool to measure how the decisions of firms effect the economy as a whole is the concept of a **********multiplier**********. In particular, it will explain how initial investment in an economy can cause drastic effects relative to the quantity of the initial investment.

To explain this effect, we must combine the separate behavior of individual households, who smooth consumption, with the behavior of firms, who do not smooth consumption. A 1$ increase in the income of individual households will not directly cause a one-to-one increase in the consumption of these households, since some of this money might be put aside to save for future decreases in income. The **********multiplier********** is a quantity which represents representing the increase in total output in an economy, relative to a change of investment. If $Y$ is aggregate demand, and $I$ is the level of investment of firms in the future of the economy, then the multiplier gives the change in aggregate demand as a response to the change in the level of investment. It is greater than one if a temporary increase in expenditure results in a greater demand, and less than one if a temporary increase causes a decrease in consumption.

Let us begin with a model excluding the government, and foreign trade. There are therefore two ways individuals spend money: consumption, and investment. We break down consumption into a **autonomous consumption** $c_0$, that is independent of the amount of income recieved, and *****************variable consumption***************** depending on a parameter $c_1$, the **********************marginal propensity to consume**********************. Thus the total consumption in an income for a particular amount of income $Y$ is given by $c_0 + c_1 Y$. We will assume $0 < c_1 < 1$, i.e. so that an increase in income causes an increase in consumption, but at least some amount is saved. This average consumption hides a large number of variables: some houses might consume more (e.g. if they are credit constrained so cannot smooth consumption) and some less, but we treat this as a necessary simplification in order to get results.

As an aside, the consumption rate can be effected by other factors, like how optimistic individuals are about the future. Data collected during the great recession shows a correlation between the consumption of ************durable goods************ and the optimism about the future, and a slightly less, but still negative correlation between consumption of non durable goods. Perhaps the greater correlation with durable goods is because these are generally more expensive, and involve taking a loan in order to buy, and also because they can be bought later, vs. food that must be bought at the present moment. Thus the durable market is more volatile than the non-durable market. We are not taking this into account in the present model, i.e. since we do not separate the consumption of durable and non-durable goods.

Next, we assume that firms are able to meet any demand for goods, i.e. they are not at ********************capacity utilization********************. If firms are willing to invest a fixed amount $I$ into future production of resources, then at a given demand $Y_{n-1}$, the total demand in the economy, and thus the aggregate demand in the future, is given by the equation $Y_n = I + c_0 + c_1 Y_{n-1}$. This gives a dynamical system which converges as $n \to \infty$ to a level of demand $Y_\infty$ satisfying the equation

$$
Y_\infty = I + c_0 + c_1 Y_\infty
$$

i.e. a quantity satisfying

$$
Y_\infty = \frac{I + c_0}{1 - c_1}
$$

That convergence occurs happens because aggregate demand will decrease over time at levels of demand above $Y_\infty$, and increases over time below $Y_\infty$. We thus see the multiplier in this problem is precisely

$$
k = \frac{dY_\infty}{dI} = \frac{1}{1 - c_1}
$$

Thus the less individuals are willing to save, the greater the total demand of the economy can be made after an initial investment.

Let us go over our assumptions. First, we assumed that firms are not at capacity utilization. We also assume that wages are fixed (i.e. so that income is proportional to demand), an assumption we will remove in the next unit.

****Consumption Saving****

Consumption is a large part of the GDP of most economies relative to investment, so it is integral we work out models that determine how $c_0$ and $c_1$ change. For instance, a change in $c_0$ might result in a multiplicative effect analogous to the effect of a change in $I$. To model how these parameters change, we think about households as having a given *****target wealth***** they are trying to achieve relative to their ***************expected wealth***************, the households net worth, plus the expected earnings the health expects to achieve from employment: if their expected wealth is lower than a target wealth, they are motivated to save more. If their expected wealth is higher than target wealth, they might as well consume more at the present moment. (QUESTION IS THIS RELATION TO SMOOTHING?). During the great depression, news about factory closures, the collapse of the stock market, and bank failures lead people to believe their expected wealth had decreased, thus decreasing the values $c_0$  and $c_1$, and eventually leading to an overall decrease in aggregate demand, and thus income.

*******************Investment Spending*******************

How might a firm decide how much it wants to invest in an economy? Given a particular profit, a firm can choose to pay dividends, save money (by paying off debt, or buying bonds), invest in foreign economies, or invest in domestic economies. 

The desirability to save money depends on the discount rate of the firm, as we saw in Chapter 10. The interest rate on saving money is one of the prime factors determining whether investment occurs, and this can be effected by government policy; the lower the interest rate, the more the chance that investment occurs. The function that associates a given interest rate with a given amount of investment is called the **********************************aggregate investment function.********************************** There is a limit to how much interest rate can effect investment; for instance, interest rates do not seem to effect the amount of money firms invest in machinery, which seems to depend much more on market side factors like aggregate demand.

***********************Stabilizing the Economy***********************

To understand how government intervention can stabilize the economy, let’s add government spending into the mix. Household spending depends on ***************post tax income***************. Let us assume the government takes a percentage $t$ of all income recieved by individuals. Consumption of individuals is therefore given by the equation $c_0 + c_1 (1 - t) Y$. We assume that expected wealth level will *****only***** effect the parameter $c_0$, and not the parameter $c_1$ (TODO: IS THIS REALLY A GOOD MODEL ISN’T $c_1$ the value we should expect to shift, i.e. b/c it contains the durable goods). Government spending $G$ does not necessarily change with changes in relative income, since the government can create money. Individuals also have a ************marginal propensity to import************, so we have an associated aggregate statistic $m$ representing the percentage of all income spent on foreign goods. If $X$  is the amount of demand of exported goods, then the net export level will be $X - mY$. Thus we obtain an equation for aggregate demand of the form

$$
c_0 + c_1(1 - t)Y + G + I + (X - mY)
$$

which now takes into account individual spending, government spending, investment by firms, and imports and exports. For a fixed set of quantities $c_0, c_1, t, G, I, X, m$, we conclude that the aggregate demand of the economy will settle at a value $Y_\infty$ satisfying the equation

$$
Y_\infty = \frac{c_0 + G + I + X}{1 - c_1(1-t) + m}
$$

The multiplier thus increases as individuals are willing to save less, as taxation is decreased, and as the propensity to import decreases. Note also that as $X$ increases, so too does the aggregate demand. Thus if one country experiences a recession, countries that are closely connected to them in the export market will also suffer. Similarily, if $m$ is relatively high, the effects of investment by the private sector or government on net demand is also reduced. This was the effect in France in 1981, when tax cuts and an increase in public spending was not met with an increase in aggregate demand because of a large spending on foreign items. The result was a contraction in the french economy; the Franc had to be devalued three times between 1981 and 1983 to compensate for the budget deficit.

The government can stabilize the economy by spending a fixed amount on public services, an amount that does not change as the economy changes. It can also pay unemployment benefits, which stabilizes the values $c_0$ and $c_1$. And it can increase the value $G$ relative to the value $I$ in order to stabilize the level of investment into the economy. In general, it is a good idea for ***********governments*********** to pay out unemployment insurance, rather than to have private firms pay this money. The reason is that people tend to become unemployed in waves, which may mean an insurance provider is unable to make payments.

*********************The Paradox of Thrift*********************

Faced with a budget deficit, a family is motivated to cut spending. In 1929, Keynes argued this phenomenon should ***not*** be followed by government. If individuals are more thrifty, the total demand in the economy falls, and so too does individual income. The *paradox of thrift* is thus that saving money leads to losing money, an instance of the **********************fallacy of composition**********************, i.e. that the effect of a decision on an individual should be the same as the effect on the economy as a whole.

Sometimes a government chooses to raise taxes or cut spending during a recession with a policy of *********austerity*********, in order to *****************balance the books,***************** as might be motivated by an increase in unemployment benefits during a recession, which increases the budget deficit. But as we saw about, this will lead to an economic contraction, which is precisely not what is needed during a period of recession. That does not mean austerity should never be pursued, but rather that it should not be pursued during a recession. A 2012 study by Alan Auerbach and Yuriy Gorodnichenko suggests that the multiplier for government investment seems to be about 1.5-2 in periods of recession, whereas closer to 0.5 in periods of expansion. Of course, some goverments are forced into a period of austerity because they have lost the ability to borrow, as we will see in the next section, but in general, balancing books should not be done during recessionary periods.

********************John Maynard Keynes********************

The Great Depression completely changed economic thought. Before, economists thought that unemployment was an imperfection of the labor market; if the market worked optimally, supply would balance demand. Persistent unemployment during the 1930s lead Keynes to reanalyze this situation. A student of Marshall, Keynes began his career as an expert on the quantity theory of money, and the gold standard, and pushed for a limited role of the government in society, but his views would soon change.

Keynes celebrity status began when he published “The Economic Consequences of the Peace”, in which he argued that the aggressive reparations Germany would have to pay were impossible to fulfill, and would lead to dire economic repercussion for the world at large.

In response to the Great Depression, Keynes changed his mind about the gold standard, arguing that limiting money supply would lead to the contraction of the economy. In 1936, he published “The General Theory of Employment, Interest, and Money”, in which he argued that, if interest rates were low, then fiscal expansion is necessary to alleviate a depression.

During WWII, Keynes lead the effort to avoid the mistakes that were made after WWI. In 1944, with Harry Dexter, he organized the Bretton Woods conference that resulted in the creation of the International Monetary Fund, or IMF. The fund was designed to ensure countries in recessions would not need to follow contractive measures as required by the gold standard.

***************************Limitations of the Analysis***************************

To calculate the multipliers in the analysis above, we greatly simplified the number of variables we were considering. But the multiplier can depend on many many more factors. If employment is lower, an increase in government spending might crowd out private investment, so that the multiplier of government spending might be close to one, or even below one if it reduces future investment in the economy by firms. The size also depends on how firms react to the choices of government. An economic stimulus might not shift individuals consumption habits if individuals perceive that the stimulus will lead to higher taxes in the future.

By 2008, the Keynesian multiplier model was seen by most economists as irrelevant for modeling the economy, and that they were skeptical the multiplier was greater than one, even while the recession was occurring. But the Great Recession brought back interest as the desire to determine the multiplier for the economy, and government investment was largely seen as responsible for staving off another great depression (so that the consensus that the multiplier was greater than one after all).

An interesting natural experiment for measuring the multiplier arose in Italy. In 1991, legal changes lead to a dismissal of mafia-associated politicians across Italy. New politicians cut spending by about 20% on average. Because there is no causal link between links to the mafia to the variation of output in a country, one can directly see based on how many politicans were replaced how the aggregate demand was affected.

**Government Debt**

In our model above, the net deficit of the government is equal to $G - tY$. When there is a budget deficit, the government must borrow to cover it’s deficit by selling bonds, normally purchased indirectly by individuals through pension funds. Foreigners can also purchase domestic bonds, and will likely do that if they are perceived to be a safe investment. A *sovereign debt crisis* occurs when government bonds begin to be considered as risky investments. Such crises are uncommon in advanced economies, but can occur in developing economies. But in 2010, the interest rate on Irish, Greek, Spanish, and Portuguese bonds increased, which lead to them being perceived as riskier. This sparked the Eurozone crisis.

TODO: WHY DID INTEREST RATES INCREASE?

A large debt can be a problem for a government, since it will have to pay it’s interest rate. However, there is no point at which a government needs to pay off it’s debt, and governments will often continue to sell new bonds as previous bonds mature in order to pay off currently issued coupons, so that they are constantly in deficit. In economies perceived as safe (i.e. with higher growth relative to a rate of inflation), this is not a problem since there is normally a demand for these bonds from private investors. But if governments print off more money, the rate of inflation increases, which means bonds might be seen as more risky.

TODO: UK BOND CRISIS.

**************Unemployment Rate**************

Finally, let’s analyze how our model determines the unemployment rate of a society. Let us suppose a constant rate of productivity of labor $\lambda$, so that if $N$ is the total number of people employed, then the aggregate demand $Y$ is equal to $N \lambda$. We choose a unit of demand so that $\lambda$ is equal to one. It then follows that the unemployment rate is directly related to $Y$, and so the previous model determines the number of people employed in an economy.

This model is a ***************short run model***************. It assumes prices, wages, the capital stock, technology, institutions are fixed. The labor market model we analyze previously was a ****************medium run model,**************** where Capital stock, technology, and institutions were fixed. In the next unit, we will continue to analyze the short run model, and in the unit after that, we come up with a **************long run model**************, where only technology and an economy’s institutions are fixed.
