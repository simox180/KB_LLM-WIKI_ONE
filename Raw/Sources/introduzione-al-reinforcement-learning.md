---
Title: Introduzione al Reinforcement Learning
Reference: Raw/Files/RL_4h_2025.pdf
Created: 2026-10-05
Processed: true
tags:
  - source
---

# Introduzione al Reinforcement Learning

Trascrizione automatica dal PDF originale; la struttura delle pagine e conservata nei marcatori.

===== PAGE 1

Reinforcement Learning
A Gentle Introduction
May 18th, 2025
Marcello Restelli                                     marcello.restelli@polimi.it


## Pagina 2

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Who am I?
• Associate Professor @Politecnico di Milano
• Courses
– Machine Learning
– Reinforcement Learning
– Information Retrieval and Data Mining
– Robotics
• Research interests
– Reinforcement learning
– Multi-agent learning
– Online learning
• Industrial collaborations
– Finance
– E-commerce
– Automotive
– Industry 4.0
– Health
• Spin-off
– ML cube (since 2021)
– AD cube (since 2023)
– TradeRL (since 2024)
• Co-Director of Artificial Intelligence Research & Innovation Center - AIRIC (since 2022)


## Pagina 3

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Outline
• Overview of Reinforcement Learning
– Sequential Decision Making 
– Policies and Value Functions
– Algorithms
• Applications

## Pagina 4

Overview of RL

## Pagina 5

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Machine Learning
• Supervised Learning
• Learn the model
• Unsupervised Learning
• Learn the representation
• Reinforcement Learning
• Learn to control

## Pagina 6

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
What is Reinforcement Lerning (RL)?
• A set of techniques for solving Sequential 
Decision Making problems
• RL is learning form interaction, by trial-and-error


## Pagina 7

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Reinforcement Learning
observations
reward
new observations

## Pagina 8

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
But who’s counting?


## Pagina 9

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
But who’s counting?
• First game
– Best possible value : 75421
– Value following the optimal policy: 75142
• Second game
– Best possible value: 76530
– Value following the optimal policy: 75630

## Pagina 10

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
History of Reinforcement Learning


## Pagina 11

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Deep Reinforcement Learning


## Pagina 12

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Deep RL to Play Atari’s Games


## Pagina 13

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Learning to Run
13


## Pagina 14

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Deep RL for Playing Go
10170 configurations
According to AI experts, computers would have beaten humans no sooner than 2100
2016
4 - 1

## Pagina 15

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
AlphaStar wins at StarCraft II
• Strategic game
• Real-time
• Partial information
• Huge decision space

## Pagina 16

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
ChatGPT: RL with Human Feedback
Source: https://huyenchip.com/2023/05/02/rlhf.html

## Pagina 17

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
ChatGPT: RL with Human Feedback
Source: https://huyenchip.com/2023/05/02/rlhf.html


## Pagina 18

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
ChatGPT: RL with Human Feedback
Source: https://huyenchip.com/2023/05/02/rlhf.html


## Pagina 19

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
RL in DeepSeek-R1


## Pagina 20

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Where RL comes from?


## Pagina 21

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
How Large is RL?
21
NeurIPS 2018 Submissions per area

## Pagina 22

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
RL Research Trend
0
10000
20000
30000
40000
50000
60000
70000
80000
90000
100000
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
No. of papers
Year
Number of RL papers per year

## Pagina 23

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
What is the Trend for RL?
Gartner, 2019

## Pagina 24

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
What is the Trend for RL?
Gartner, 2023


## Pagina 25

Sequential Decision Making

## Pagina 26

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Markov Decision Process (MDP)
• State space 𝑆𝑆
• Action space 𝐴𝐴
• Transition model 𝑃𝑃(𝑠𝑠𝑠|𝑠𝑠, 𝑎𝑎)
• Reward function 𝑅𝑅(𝑠𝑠, 𝑎𝑎, 𝑠𝑠𝑠)
• Discount factor 𝛾𝛾
• Initial state distribution 𝜇𝜇(𝑠𝑠)


## Pagina 27

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Markov Assumption
The future is independent of the past given the present
• Definition: a stochastic process 𝑋𝑋𝑡𝑡 is said to be Markovian if and only if 
 𝑃𝑃 𝑋𝑋𝑡𝑡+1 = 𝑗𝑗 𝑋𝑋𝑡𝑡 = 𝑖𝑖, 𝑋𝑋𝑡𝑡−1 = 𝑘𝑘𝑡𝑡−1, … , 𝑋𝑋0 = 𝑘𝑘0 = 𝑃𝑃(𝑋𝑋𝑡𝑡+1 = 𝑗𝑗|𝑋𝑋𝑡𝑡 = 𝑖𝑖)
– The state captures all the information from history
– Once the state is known, the history may be thrown away
– The state is a sufficient statistic for the future
– The conditional probabilities are tranistion probabilities
– If the probabilities are stationary (time invariant), we can write:
𝑝𝑝𝑖𝑖𝑖𝑖 = 𝑃𝑃 𝑋𝑋𝑡𝑡+1 = 𝑗𝑗 𝑋𝑋𝑡𝑡 = 𝑖𝑖 = 𝑃𝑃(𝑋𝑋1 = 𝑗𝑗|𝑋𝑋0 = 𝑖𝑖)

## Pagina 28

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Classification of Environments
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 29

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 1: Rubik’s Cube
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 30

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 1: Rubik’s Cube
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 31

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 2: Blackjack
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 32

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 2: Blackjack
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 33

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 3: Pole Balancing
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 34

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 3: Pole Balancing
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent

## Pagina 35

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 4: Robot Navigation
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 36

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 4: Robot Navigation
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 37

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 5: Web Banner Advertising
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 38

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 5: Web Banner Advertising
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 39

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 6: Chess
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 40

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 6: Chess
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 41

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 7: Texas Hold’em
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 42

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Example 7: Texas Hold’em
• Discrete vs Continuous State
• Discrete vs Continuous Action
• Deterministic vs Stochastic
• Fully vs Partially Observable
• Stationary vs Nonstationary
• Single Agent vs Multi Agent


## Pagina 43

Policies and Value Functions

## Pagina 44

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Policies
• A policy, at any given point in time, decides which action the 
agent selects
• A policy fully defines the behavior of an agent
• Policies can be:
– Markovian ⊆ History-dependent
– Deterministic ⊆ Stochastic
– Stationary ⊆ Non-stationary

## Pagina 45

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Policies
• A policy, at any given point in time, decides which action the 
agent selects
• A policy fully defines the behavior of an agent
• Policies can be:
– Markovian ⊆ History-dependent
– Deterministic ⊆ Stochastic
– Stationary ⊆ Non-stationary

## Pagina 46

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Value functions
• Given a policy 𝜋𝜋, it is possible to define the utility of each 
state: Policy Evaluation
• Value function 
– 𝑉𝑉𝜋𝜋 𝑠𝑠 = 𝐸𝐸𝜋𝜋[∑𝑡𝑡=0
∞ 𝛾𝛾𝑡𝑡𝑟𝑟𝑡𝑡+1|𝑠𝑠𝑡𝑡 = 𝑠𝑠]
• For control purposes, rather than the value of each state, it is 
easier to consider the value of each action in each state
– 𝑄𝑄𝜋𝜋 𝑠𝑠, 𝑎𝑎 = 𝐸𝐸𝜋𝜋[∑𝑡𝑡=0
∞ 𝛾𝛾𝑡𝑡𝑟𝑟𝑡𝑡+1|𝑠𝑠𝑡𝑡 = 𝑠𝑠 , 𝑎𝑎𝑡𝑡 = 𝑎𝑎]

## Pagina 47

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Bellman Expectation Equation
• The value function can again be decomposed into immediate 
reward plus discounted value of successor state
𝑉𝑉𝜋𝜋 𝑠𝑠 = 𝐸𝐸𝜋𝜋 𝑟𝑟𝑡𝑡+1 + 𝛾𝛾𝑉𝑉𝜋𝜋 𝑠𝑠𝑡𝑡+1 𝑠𝑠𝑡𝑡 = 𝑠𝑠
= �
𝑎𝑎
�
𝑠𝑠𝑠
𝜋𝜋 𝑎𝑎 𝑠𝑠 ∗ 𝑃𝑃 𝑠𝑠𝑠 𝑠𝑠, 𝑎𝑎 ∗ 𝑅𝑅 𝑠𝑠, 𝑎𝑎, 𝑠𝑠𝑠 + 𝛾𝛾𝑉𝑉𝜋𝜋(𝑠𝑠𝑠)
• The action-value function can similarly be decomposed:
      𝑄𝑄𝜋𝜋 𝑠𝑠, 𝑎𝑎 = 𝐸𝐸𝜋𝜋 𝑟𝑟𝑡𝑡+1 + 𝛾𝛾𝑄𝑄𝜋𝜋 𝑠𝑠𝑡𝑡+1 𝑠𝑠𝑡𝑡 = 𝑠𝑠, 𝑎𝑎𝑡𝑡 = 𝑎𝑎 =
∑𝑠𝑠𝑠 𝑃𝑃 𝑠𝑠𝑠 𝑠𝑠, 𝑎𝑎 ∗ (𝑅𝑅 𝑠𝑠, 𝑎𝑎, 𝑠𝑠𝑠 + 𝛾𝛾 ∑𝑎𝑎𝑠 𝜋𝜋 𝑎𝑎𝑠 𝑠𝑠𝑠 𝑄𝑄𝜋𝜋(𝑠𝑠𝑠, 𝑎𝑎𝑠) 

## Pagina 48

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Matrix Form
• The Bellman expectatio equation can be expressed concisely 
using the induced MRP
𝑉𝑉𝜋𝜋 = 𝑅𝑅𝜋𝜋 + 𝛾𝛾𝑃𝑃𝜋𝜋𝑉𝑉𝜋𝜋
• with direct solution
      𝑉𝑉𝜋𝜋 = 𝐼𝐼 − 𝛾𝛾𝑃𝑃𝜋𝜋 −1𝑅𝑅𝜋𝜋 

## Pagina 49

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Bellman Operators
• The Bellman operator 𝑇𝑇𝜋𝜋 maps value functions to value 
functions:
– 𝑇𝑇𝜋𝜋𝑉𝑉𝜋𝜋 𝑠𝑠 = ∑𝑎𝑎 𝜋𝜋 𝑎𝑎 𝑠𝑠 ∑𝑠𝑠𝑠 𝑃𝑃(𝑠𝑠𝑠|𝑠𝑠, 𝑎𝑎) 𝑅𝑅 𝑠𝑠, 𝑎𝑎, 𝑠𝑠𝑠 + 𝛾𝛾𝑉𝑉𝜋𝜋(𝑠𝑠𝑠)
– Using Bellman operator, Bellman expectation equation can be 
compactly written as:
𝑇𝑇𝜋𝜋𝑉𝑉𝜋𝜋 = 𝑉𝑉𝜋𝜋
– 𝑉𝑉𝜋𝜋 is a fixed point of the Bellman operator 𝑇𝑇𝜋𝜋
– This is a linear equation in 𝑉𝑉𝜋𝜋 and 𝑇𝑇𝜋𝜋
– If 0 < 𝛾𝛾 < 1 then 𝑇𝑇𝜋𝜋 is a contraction w.r.t. the maximum norm

## Pagina 50

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Policy performance
• The performance of a policy 𝜋𝜋 is the expected discounted sum 
of the rewards collected by 𝜋𝜋
𝐽𝐽𝜋𝜋 = 𝔼𝔼 �
𝑡𝑡=0
𝐻𝐻
𝛾𝛾𝑡𝑡𝑅𝑅𝑡𝑡 𝑠𝑠𝑡𝑡, 𝑎𝑎𝑡𝑡, 𝑠𝑠𝑡𝑡+1 |𝜋𝜋
= �
𝑠𝑠
𝜇𝜇 𝑠𝑠 𝑉𝑉𝜋𝜋 𝑠𝑠

## Pagina 51

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Stationary Distribution
• Given a policy 𝜋𝜋, the sequence of states comes from a Markov chain
• 𝑃𝑃𝜋𝜋 is the state transition probability matrix
• If 𝑃𝑃𝜋𝜋 is regular, then the chain converges to the stationary distribution
𝑑𝑑𝜇𝜇𝜋𝜋 𝑠𝑠𝑠 = �
𝑠𝑠
𝛾𝛾𝑑𝑑𝜇𝜇𝜋𝜋 𝑠𝑠 𝑃𝑃𝜋𝜋(𝑠𝑠𝑠|𝑠𝑠) , ∀𝑠𝑠𝑠 ∈ 𝑆𝑆
• Policy performance:
𝐽𝐽𝜋𝜋 = �
𝑠𝑠
𝜇𝜇 𝑠𝑠 𝑉𝑉𝜋𝜋 𝑠𝑠 = �
𝑠𝑠
𝑑𝑑𝜇𝜇𝜋𝜋 𝑠𝑠 𝑅𝑅𝜋𝜋(𝑠𝑠)

## Pagina 52

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Optimal Value Function
• The optimal state-value function 𝑉𝑉∗(𝑠𝑠) is the maximum value 
function over all policies
𝑉𝑉∗(𝑠𝑠) = max
𝜋𝜋
 𝑉𝑉𝜋𝜋(𝑠𝑠)
– The optimal value function specifies the best possible performance 
in the MDP
– An MDP is «solved» when we know the optimal value function

## Pagina 53

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Optimal Policy
• Value functions define a pratial ordering over policies
𝜋𝜋 ≥ 𝜋𝜋𝑠 if 𝑉𝑉𝜋𝜋 𝑠𝑠 ≥ 𝑉𝑉𝜋𝜋′
𝑠𝑠 , ∀𝑠𝑠 ∈ 𝑆𝑆
• For any MDP
– There exists an optimal policy 𝜋𝜋∗ that is better than or equal to all 
the other policies: 𝜋𝜋∗ ≥ 𝜋𝜋, ∀𝜋𝜋
– All optimal policies achieve the optimal value function
– There is always a deterministic optimal policy for any MDP

## Pagina 54

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Bellman Optimality Equation
• Bellman optimality equation for 𝑉𝑉∗
𝑉𝑉∗ 𝑠𝑠 = max
a
�
𝑠𝑠𝑠
𝑃𝑃 𝑠𝑠𝑠 𝑠𝑠, 𝑎𝑎 𝑅𝑅 𝑠𝑠, 𝑎𝑎, 𝑠𝑠𝑠 + 𝛾𝛾𝑉𝑉∗(𝑠𝑠𝑠)
• Bellman optimality equation for 𝑄𝑄∗
𝑄𝑄∗ 𝑠𝑠, 𝑎𝑎 = �
𝑠𝑠𝑠
𝑃𝑃(𝑠𝑠𝑠|𝑠𝑠, 𝑎𝑎) 𝑅𝑅 𝑠𝑠, 𝑎𝑎, 𝑠𝑠𝑠 + 𝛾𝛾 max
𝑎𝑎𝑠
𝑄𝑄∗(𝑠𝑠𝑠, 𝑎𝑎𝑠)  
• Bellman optimality equation is non-linear
• No closed-form solution for the general case

## Pagina 55

Algorithms

## Pagina 56

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Solving MDPs
• Brute force
– Unfeasible even for simple problems
• Dynamic Programming
– Requires knowledge of the transition model
• Linear Programming
– Better worst-case complexity, but worse in average
• Reinforcement Learning
– Without knowledge of the model

## Pagina 57

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
When is RL useful?
• When the dynamics of the environment are unknown or 
difficult to be modeled
– E.g., trading, betting
• When the model of the environment is too complex to be 
solved exactly, so that approximate solutions are searched for
– E.g., humanoid robot control, group elevator dispatching

## Pagina 58

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Classification of RL Techniques
• Model-free vs Model-based
• On-policy vs Off-policy
• Online vs Offline
• Tabular vs Function Approximation
• Value-based vs Policy-based vs Actor-Critic

## Pagina 59

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Reinforcement Learning Approaches
• Value-based
– Estimate the utility of state-action pairs
• Policy-based
– Search for the best parametric policy
• Actor-critic
– Combine the two previous approaches


## Pagina 60

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Value-Based Techniques
• Learn value function and implicit policy
• Monte Carlo vs Temporal Difference
• Some algorithms
– SARSA (on-policy)
𝑄𝑄 𝑠𝑠, 𝑎𝑎 ← 𝑄𝑄 𝑠𝑠, 𝑎𝑎 + 𝛼𝛼 𝑟𝑟 + 𝛾𝛾𝑄𝑄 𝑠𝑠𝑠, 𝑎𝑎𝑠 − 𝑄𝑄(𝑠𝑠, 𝑎𝑎)  
– Q-learning (off-policy)
𝑄𝑄 𝑠𝑠, 𝑎𝑎 ← 𝑄𝑄 𝑠𝑠, 𝑎𝑎 + 𝛼𝛼 𝑟𝑟 + 𝛾𝛾 max
𝑎𝑎′ 𝑄𝑄 𝑠𝑠𝑠, 𝑎𝑎𝑠 − 𝑄𝑄(𝑠𝑠, 𝑎𝑎)
• Continuous states => Function approximation, but no supervised learning
• When to use them
– Discrete actions
– Full Observability
https://cs.stanford.edu/people/karpathy/reinforcejs/gridworld_dp.html

## Pagina 61

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Policy-Based Techniques
• No value function and learn policy
• Some algorithms
– Policy gradient: REINFORCE, NPG, DDPG
– Trust region: REPS, TRPO, PPO, POIS
– Parameter-based: PGPE, NES, CEM
• Advantages
– Continuous actions
– Partial Observability
– Can benefit from demonstrations
– Stochastic policies
• Disadvantages
– May converge to local optima
– Sample inefficient
𝛻𝛻𝜃𝜃𝐽𝐽 𝜃𝜃 = 𝐸𝐸𝜋𝜋𝜃𝜃 �
𝑡𝑡=1
𝑇𝑇
𝐺𝐺𝑡𝑡𝛻𝛻𝜃𝜃 log 𝜋𝜋𝜃𝜃 𝑎𝑎𝑡𝑡|𝑠𝑠𝑡𝑡
𝐺𝐺𝑡𝑡 = 𝑟𝑟𝑡𝑡+1 + 𝛾𝛾𝑟𝑟𝑡𝑡+2 + 𝛾𝛾2𝑟𝑟𝑡𝑡+3

## Pagina 62

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Actor-Critic Techniques
• Exploit the best of the previous approaches
• Algorithms
– A2C, A3C, SAC, …
• When to use them
– Continuous actions
– Full observability
𝑄𝑄𝑤𝑤 𝑠𝑠, 𝑎𝑎 ≈ 𝑄𝑄𝑤𝑤
𝜋𝜋𝜃𝜃 (s, a)
𝛻𝛻𝜃𝜃𝐽𝐽(𝜃𝜃) ≈ 𝐸𝐸𝜋𝜋𝜃𝜃 𝛻𝛻𝜃𝜃 log 𝜋𝜋𝜃𝜃 𝑎𝑎 𝑠𝑠 𝑄𝑄𝑤𝑤(𝑠𝑠, 𝑎𝑎)

## Pagina 63

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Other RL Techniques
• Multi-Objective RL
• Inverse RL
• Transfer RL
• Safe RL
• Multi-Agent RL


## Pagina 64

Applications

## Pagina 65

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Reinforcement Learning Applications
• Robotic Control
• Water Resource Management
• Internet Commerce
• Gaming
• Finance
• Power Systems
• Autonomous Vehicles
• Dialogue Management


## Pagina 66

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Forex Trading €/$: the problem
• State
– Position (long/flat/short)
– Time
– Trades per minute
– Price history (60)
• Actions
– Long/flat/short (100K€)
• Reward
– P&L – fees (2€)
• Dataset
– 1-minute data from 2014 to 2018


## Pagina 67

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Forex Trading €/$: the performance


## Pagina 68

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Forex Trading €/$: the performance


## Pagina 69

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Autonomous Driving: Highway
• State (25 variables)
– Ego lane occupancy
– Ego speed
– Distance front / Distance back
– Speed front / Speed back
– Occupancy front / Occupancy back
– Free left / Free right
– During lane change
• Actions
– Car follower
– Lane change left
– Lane change right
• Rewards: multi-objective
– Target speed
– Safety violation
– Occupy the rightmost lane
– Avoid useless lane changes
• Issues
– Delay (1s)
– Partial observability


## Pagina 70

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Autonomous Driving: algorithms
• Several deep algorithms
– DQN
– TRPO
• They are not interpretable!
– PGPE + parametric rules (6 parameters)


## Pagina 71

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Autonomous Driving: performance


## Pagina 72

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Car Racing: the problem
• Understand the potential of a new car
• Fast learning to drive a new car
– Demonstrations from drivers
– Different cars
• Learning from demonstrations
– Stay close to the best trajectories
• Transfer learning
– Reuse of samples
– Importance weighting


## Pagina 73

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Car Racing: the performance


## Pagina 74

Marcello Restelli, Dipartimento di Elettronica, Informazione e Bioingegneria
Questions?

