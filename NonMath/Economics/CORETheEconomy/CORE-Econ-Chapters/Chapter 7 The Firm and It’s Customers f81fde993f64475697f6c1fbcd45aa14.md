# Chapter 7: The Firm and It’s Customers

Most people in the modern day work for *large* firms. Firms grow because owners can gain more money if they expand. They prosper by many different strategies: some firms, like Tesco, prosper by *keeping the price low*, minimizing the profit on individual items with the hope that the lower prices enough customers to maximize profit. Apple, on the other hand, charges a *premium* for their products, rather than lowering prices to reach more customers.

- The classical analysis of price setting is in terms of a demand curve: we assume known that at a given price $P$, there is a given demand $D$ for a good. Firms will offer their goods at a price $P$ which maximizes $(P-C)D$, where $C$ is the cost for producing a good.
    - In practice, this is not necessarily how prices are set, e.g. by trial and error, or by past experience / market research. But we expect firms to act in this way over time, because they are forced to act optimally via competition with other firms.
- Firms are often large in order to take advantage of *economies of scale*, the lowered average cost of production that occurs in large firms by virtue of the technological advantages of large scale production, being able to take advantage of specialization, and cost advantages that occur, for instance, by having to pay less per unit on advertising or lobbying.
- On the other hand, there are also *diseconomies of scale*. For instance, the more workers a firm employs, the greater the level of bureaucracy required to maintain that firms increased level of production.
- If many users use a given product, it often becomes more useful (it is much more easy to use a Windows computer than a Linux computer partially because more people use Windows, and therefore have the skill set to continue using Windows computers). Thus we have a *network economy of scale*.
- There are also *economies of scope*: cost savings obtained by producing many products together. For instance, universities are more profitable by providing undergraduate education, graduate education, and research into one package.

Many products in the economy are *differentiated*, i.e. a series of products may be similar in use, but the products produced by each company may have small variations which make the product produced by each given company (Toyota, Ford, and so on) essentially unique. Let us now come up with a model to analyze economic transactions with differentiated products.

- We consider an economy consisting of a collection of individual customers. Each individual in an economy has a certain maximum amount they would be willing to pay for each product, which we call a *willingness to pay*. This induces a demand function: for any cost, there will be a certain number of customers who are willing to buy a product at that particular cost. Firms then produce a certain number of goods, and sell it at a fixed price to all customers who are willing to buy the product for that price.
- Each individual who buys the good then receives a *consumer surplus* from buying that item, i.e. the difference between the maximum amount they would be willing to pay for the product, and the amount they actually paid. The *producer surplus* is the price at which the good is sold, vs. the minimum amount the producer would be willing to sell the good at (a quantity closely related to profit, but not accounting for fixed costs which are independent of the number of goods sold). Thus individuals in this model make *economic rent* by virtue of their individual differences in preference. The surplus from trading is called the *gains from exchange*.
- Setting one price for all customers results in a loss of potential producer surplus, relative to setting prices individually for each customer (*perfect price discrimination*). Thus firms have grounds to gain by changing the rules of the gain to another feasible situation. By the same vein, individuals who are priced out of a single price, but are willing to pay above the production price for an item also lose out, because in the situation where goods are individually priced, they would also have the potential to gain some surplus. Thus the outcome of this game is *not necessarily Pareto optimal*. When a market results in a non Pareto optimal choice, we call it a *market failure*. Thus the decision incurs a *deadweight loss*, a loss in the product of surplus for individuals involved in a game which could be avoided by switching to a Pareto optimal rule set.
- Recall that the *price elasticity* *of demand* of a good is the percentage rate of *decrease* of the demand of a product, relative to a percentage increase in price. In math terms, given a demand $D$, which we view as a function of price $P$, the elasticity is equal to
    
    $$
    \varepsilon = - \lim_{\Delta P \to 0} \frac{\Delta D/ D}{\Delta P / P}
     = - \frac{dD}{dP} \frac{P}{D}
    $$
    
    The elasticity is normally positive, since increasing prices will likely mean less people are willing to buy a product (this is referred to as the *Law of Demand*). A good is *elastic* if it’s price elasticity exceeds one, and *inelastic* if it’s price elasticity is less than one.
    
    - For instance, the demand function $D = P^{-e}$ has a constant rate of elasticity $e$. A linear demand function is given by  $D = T - AP$, where $T$ is the total number of customers of a particular product. The elasticity is then $AP/(T - AP) = T/D - 1$, which is elastic for $P > T/2A$, and inelastic for  $P < T/2A$. As $A$ increases, the good is elastic for more prices $P$.
- A producer would *always* set the price at a point where the elasticity is greater than one, since they choose a price point $P$ which maximizes the profit $PD - C$, where $C$ is the cost of producing $D$ goods, and so the marginal rate of profit is

$$
\begin{aligned} \frac{d(PD - C)}{dP} &= D + P \frac{dD}{dP} - \frac{dC}{dP}\\ &= D + P \frac{dD}{dP} - \frac{dC}{dD} \frac{dD}{dP}\\ &= D \left( 1 - \varepsilon \left( 1 - \frac{dC}{dD} \frac{1}{P} \right) \right)
 \end{aligned}
$$

       This quantity must vanish, which leads to the equation

$$
1 = \varepsilon \left( 1 - \frac{dC}{dD} \frac{1}{P} \right)
$$

      Except in degenerate situations where no products are sold, we must have

$$
0 < 1 - \frac{dC}{dD} \frac{1}{P} < 1
$$

       because $0 < dC/dD < P$. But this implies that $\varepsilon > 1$, i.e. the price will *always* be set at a price point at which the good is elastic.

- We see from the above that the larger $\varepsilon$ is, the closer $dC/dP$ is to $P$, i.e. the *profit margin (*the left hand side of the equation) is smaller the more elastic the good is. On the other hand, as $\varepsilon$ tends to one, the profit margin is allowed to become arbitrarily large. Thus in situations where a good is inelastic (e.g. if the good is not easily replaceable with another, a producer can earn a huge profit margin). In this case we say the producer earns *monopoly rents*, and is said to have *market power*.
- Let us suppose we add *taxes* to the model, i.e. we add a sales tax $T$ to the sale of each individual item. The government will then earn a profit of $DT$ from the tax. However, the price a producer will set will now change to take into account the increased costs. Namely, our elasticity equation becomes
    
    $$
    1 = \varepsilon \left( 1 - \left( \frac{dC}{dD} + T \right) \frac{1}{P} \right)
    $$
    

       If the government now chooses a tax to maximize the profit from taxes, then we find that

$$
0 = \frac{d(DT)}{dT} = D + T \frac{dD}{dT} = D + T \frac{dD}{dP} \frac{dP}{dT} = D \left( 1 - \varepsilon \cdot \frac{T}{P} \right)
$$

      A government aiming to optimize tax revenue should therefore set $\varepsilon = P / T$, i.e. the elasticity will be equal to the percentage of the price that is given in taxes to the government. Thus if elasticity is high, the tax should be a low percentage of the good, and if the elasticity is low, then a larger percentage of the good should be given in taxes.

- *However*, a government may not necessarily want to optimize tax revenue. For instance, they may wish to tax an elastic good, like cigarettes, in order to discourage individuals from buying cigarettes, since society might decide that smoking is not healthy for society. Thus they make a trade off between tax revenue, and the public good that comes from less people smoking.
- Often policymakers are concerned with firms establishing market power via monopoly, since it enables them to obtain most of the trade surplus in a transaction, as well as a deadweight loss. Thus governments often intervene in trade actions via *competition,* or *antitrust* policy in order to ensure monopolies don’t form. In 2000, the European commission prevented Volvo from merging with Scania, since the two firms would then have a near monopoly on the heavy truck market. The US Department of Justice accused Microsoft of behaving anti competitively by making Internet Explorer the default web browser on its operating system. Having few firms in a market can also increase the potential for a *cartel:* where firms collude to keep the price high.
- In the production of some goods, such as utilities like gas and electricity, the fixed costs of an industry are high, irrespective of demand. Thus utilities possess a huge potential for economies of scale. A *natural monopoly* is a situation where a single firm can supply the entire market of a certain good at a lower cost of two firms provided the same quantity of these goods. In such a situation, increasing competition will not necessarily lower prices, since the cost to produce an individual good will increase the more competition that exists in a market. One way to ensure low costs in this situation is to fix prices, or to take public ownership of a good. A similar situation emerges in the production of media, e.g. since the cost to produce a single video game is virtually the same as the cost to produce one million copies of a video game. Thus the marginal cost of a cost is much lower than the average cost.
    - Question: Electricity is usually not a differentiated product, so buyers of electricity may be strongly price-sensitive. What does this mean?
    
    Discuss Exercise 7.8