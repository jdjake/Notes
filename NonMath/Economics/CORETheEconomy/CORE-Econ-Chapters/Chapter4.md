# Chapter 4: Social Interactions

- A *social dilemma* is a situation in which individuals acting independently, in pursuit of their own private objectives, result in an outcome that is inferior to some other feasible outcome that could have occurred differently if individuals acted collectively.
    - e.g. the Stern review, a report on the economic outcomes of climate change, predicts that the benefits of early action to slow climate change will vastly outweigh the economic cost of ‘pursuing business as usual', i.e. individuals pursuing their own pleasures, politics, and profits without taking account of their action on future generations.
    - Traffic jams occur when our individual desire to get around fast does not take into account the congestion that will cause.
    - Overusing antibiotics may help individuals recover more quickly, but may lead to the response of antibiotic resistant bacteria, which cause have much more harmful effects in the future.
    - The *Tragedy of the Commons* is a concept that resources not privately held by individuals (e.g. Fish) are easily exploited unless access to those resources are controlled in some way.
- How do we resolve social dilemmas?
    - Individuals may be willing to bear a cost in order to benefit someone else. These actions are called *altruistic*.
    - Government policies may control access to certain actions / add economic disincentives to encourage certain behaviour.
    - In this chapter, we use game theory to model social interactions.
- *Games* are models of *strategic interactions*, i.e. interactions between individuals who are aware of the ways that their actions affect others. Thus a game details *the players (*the individuals interacting), *the feasible strategies* (the actions open to players), *the information available to each player*, and *the payoffs* (the results of a given action).
    - The *best response* of a player is the action that will give that player the highest payoff, relative to the strategies of other players. A strategy is *dominant* if it yields the highest payoff, regardless of the actions of other players.
    - Suppose that two farmers both have the option of producing two crops, but can each only decide to produce one crop at a time. If both farmers produce the same resource, then there will be a large supply of that crop in the market, lowering prices. We might model the situation in a matrix as follows, with the rows representing the first farmer’s choice, and the columns the farmer’s second choice:
        
        
        |  | Crop A | Crop B |
        | --- | --- | --- |
        | Crop A | Farmer 1 gets $1
        Farmer 2 gets $3 | Farmer 1 gets $2
        Farmer 2 gets $2 |
        | Crop B | Farmer 1 gets $4
        Farmer 2 gets $4 | Farmer 1 gets $3
        Farmer 2 gets $1 |
        
        Regardless of whether Farmer 2 chooses crop A or crop B, Farmer 1’s best response is to choose to grow Crop B. Thus choosing to grow Crop B is Farmer 1’s dominant strategy. Similarly, the dominant strategy of Farmer 2 is to crow Crop A. We might predict therefore that the two farmer’s will choose to grow each of these resources; the situation is called a *dominant strategy equilibrium*, i.e. both players have dominant strategies, and they play those strategies. It is not always the case that dominant strategy equilibriums exist, but if they do, we expect self interested players to pursue these strategies. More generally, a *Nash equilibrium* is reached if all players is a game simultaneously choose the actions that result in the best outcome from themselves, given all other player’s actions. In such a case, self interested individuals should not regret the actions they took.
        
        Each individual acted in their own interest, which lead to the best possible result for each individual. Although they acted independently, they were guided by *an invisible hand* to an outcome that was beneficial for both parties. The pursuit of self interest is sometimes considered to be morally bad, but economics had identified situations in which it can lead to socially desirable outcomes. But there are situations in which the pursuit of self interest leads to suboptimal outcomes.
        
    - Now suppose that the farmers have to decide between using a chemical pesticide to kill crop eating pests, or to introduce beneficial insects which eat the pests. If just one of the farmers choose the pesticide, the damage will be limited, but if both farmers choose to use pesticides, water contamination will become bad enough they will both need to buy expensive filters.
        
        
        |  | Insects | Chemical |
        | --- | --- | --- |
        | Insects | Farmer 1 gets $3
        Farmer 2 gets $3 | Farmer 1 gets $1
        Farmer 2 gets $4 |
        | Chemical | Farmer 1 gets $4
        Farmer 2 gets $1 | Farmer 1 gets $2
        Farmer 2 gets $2 |
        
        Both farmer’s dominant strategy is to choose to use chemicals. But this leads to a strategy that it less optimal for either farmer. This game is an example of a type of game known as the *prisoner’s dilemma,* a game where the payoffs for the dominant equilibrium are lower for each player than if neither player played a dominant strategy. Let us analyze why a suboptimal action was taken by these players:
        
        - Neither farmer accounted for the payoffs of the other person, and so did not internalize the *costs* of taking an action on others. Preferences which do not just take account of individual benefit are called *social preferences,* either through altruism, or through spite and envy.
        
        One way we could model having social preferences my altering the utility for each action to account for social preference, and then running the same model as before. For instance, if we adjust the reward of an action by increasing the reward by 75% of other farmer’s reward, then we get a matrix of the form
            
            
            |  | Insects | Chemical |
            | --- | --- | --- |
            | Insects | Farmer 1 gets $5.25
            Farmer 2 gets $5.25 | Farmer 1 gets $4
            Farmer 2 gets $4.75 |
            | Chemical | Farmer 1 gets $4.75
            Farmer 2 gets $4 | Farmer 1 gets $3.5
            Farmer 2 gets $3.5 |
            
            The dominant strategy for both farmers is now to choose to use insects, which results in a better outcome for everyone. We thus see that social dilemmas are easier to resolve if people care for one another.
            
        - They were not able to make an agreement together on what actions to take together, and so could could not both agree to use insects on their farms.
    - Now imagine that, instead of making a single choice on what pesticide to use, farmer’s have a choice of switching between each pesticide each year.  Thus we have a *repeated game*. There is now incentive to cooperate given that, if an individual is screwed over in a previous year, they may change their actions the following year, which might result in a worse outcome over time for everyone.
    - A *conflict of interest* occurs when there is no single Nash equilibrium which is universally preferable to all players of a game.
- There is debate on how much man is a *homo economicus*: a selfish and calculating individual pursuing self interest described in classical economics. Most classical economists believe so. Even great acts of kindness can be viewed as attempts to gain a favorable reputation, or have some other hidden benefit for the individual.
    - Since the 1990s, economists have performed hundreds of experiments to determine how individuals (e.g. students, farmers, whale hunters, warehouse workers, CEOS, etc) share various outcomes. The results seem to indicate that some behaviour is motivated by self interest, but also motivated by principles of altruism, reciprocity, aversion to inequality, even if following these principles leads to heavy losses, including several day’s wages. Thus we must be careful in applying the assumption of self interest to economic models. It can be appropriate in some economic calculations, but not in others, such as how we pay taxes, or why we work hard at our jobs.
- Though people seem to be generally altruistic, it does not seem altruism is a sustainable way to solve social dilemmas given large numbers of people:
    - Consider a game with ten rounds, in each round players contribute a given amount of money to a common pool: for each $1 contribution to the pool, everyone will recieved $0.40. Experiments show that in large groups, people are initially altruistic, though the degree to which this is to differs depending on the community. But over time, most people become less altruistic.
        - One explanation is that players noticed other players being less altruistic, and so were no longer willing to act as altruistically. We thus witness a tragedy of the commons.
    - On the other hand, if we add an additional option to punish players, e.g. paying $1 to take $3 of a particular individuals cash fund anonymously, then the contributions to the public pool remained high over time. Thus being able to punish those who violate societal expectations or norms leads to a sustainable solution of a social dilemma.
        - This phenomenon was brought forward by political scientist Elinor Ostrom, among other researchers, in the study of irrigation projects in India, Nepal, and other countries. In such countries, farmers rely on a shared irrigation facility to produce crops. These facilities require constant investment to maintain over time. Each individual could *free ride*, making a profit by not investing into the facility, and relying on the contributions of others. Ostrom was one of the first to provided economic explanations for how property could be owned by a community, rather than by private individuals or an organized government. In particular, Ostrom brought forward the idea that a tragedy of commons is not a necessary outcome of such a situation:
            - First, Ostrom distinguished between *Common Property* (property which a community can act in ways to prevent outsiders from exploiting resources, such as inshore fisheries, grazing lands, or forests), and *Open-Access Resources,* which can be exploited without restrictions.
            - Economists believed that one could explain these situations by the theory of self interest in *repeated games*. Ostrom showed that sustainable use was enforced by actions that deviated from an assumption of self interest. For instance, not only a preference for helping others, but also punishing those who violate rules or societal norms, even if it does not directly benefit you for doing so.
- Let us discuss some other factors that affect cooperation:
    - In some communities, *collective trust* built over time encourages cooperation. However, it seems that communities with more inequality have a harder time building up this collective trust and cooperation.
    - External regulations also sometimes erode the willingness of individuals to cooperate. For instance, in 1998, after some day cares in Israel introduced fines for late pickups of children, the number of late pickups doubled, and remained this way even after the fines were dropped. One explanation might be that, before the fine, parents came on time because they thought it was the right thing to do, whereas when the fine was introduced, it put a monetary value, and not a moral value, on being late. Thus it seems that introducing a fine lead individuals to think in a new *framework* about their decisions.
    - People often resort to *negotiation* in order to resolve social dilemmas. For instance, negotiation lead to the Montreal Protocol, in which countries agreed to eliminate the use of CFCs to avoid the destruction of the ozone layer. Negotiations on climate change have been less successful.
- Consider the *ultimatum game*. This is a *sequential game*, i.e. decisions are not made simultaneously. Player 1 is given $100, and instructed to offer a given amount to a Player 2. Player 2 can either accept the money, in which case Player 1 walks away with the remainder, or deny the offer, in which case neither player walks away with any money.
    - If the game was not repeated, and Player 2 was purely operating under self interest, then it would never be a good choice to deny the offer: it results in a worse outcome for both players. But in practice real players do accept or deny such offers. For instance, Kenyan farmers seemed to expect at least 30% or more before they began to accept an offer, US students were much more willing to accept an offer at say, 10% of the overall amount, and Missouri farmers were almost entirely unwilling to accept any offer below 50%. But no one was willing to accept an offer of 0%, even though they would receive the same amount by denying it. Correspondingly, Missouri farmers almost always offered 50%, and Kenyan farmers a higher percentage on average than US students.
    - We can model this situation through a theory in which players have preferences to punish their opponent if they receive an unequal amount of cash: Suppose Player 1 offers an amount of money X to Player 2. Assume Player 2 receives X units of satisfaction for accepting the money. Alternatively, suppose Player 2 also receives an amount of satisfaction from denying an offer below some expected amount of money T. If we let R denote the strength of the expectation that an amount T will be offered, then Player 2 will receive R max(T-X,0) units of satisfaction for denying an offer of X dollars from Player 1. The *minimum acceptable offer* for player two will be obtained by setting R max(T-X,0) = X, which occurs when X = T/(1+1/R).
    - What happens if there are two Player 2s, each of which has the option of accepting a given amount of money, splitting the cash if they both accept the offer. In this case, Player 2s cannot be sure that Player 1 will be punished if they do not accept an offer. Thus even fair minded individuals may accept lower offers to avoid having the worst of both worlds. And because of this, Player 1s are lead to offer lower prices.