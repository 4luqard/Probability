# Problem Set 2: Ebola(Problem 10)

## Part (c)

Probability of each gene and the trait: [0.702, 0.301, 0.501, 0.801, 0.327, 0.301].
Conditional probability of the trait given each gene: [0.302, 0.302, 0.583, 0.371, 0.9].
Given these probabilities we can calculate to see if each gene is independent of the trait using the $P(A, B) = P(A) \times P(B)$:

- Gene 1: $P(Gene1, Trait) = P(Gene1) \times P(Trait) = 0.702 \times 0.301 = 0.211002$.
- Gene 2: $P(Gene2, Trait) = P(Gene2) \times P(Trait) = 0.301 \times 0.301 = 0.090601$.
- Gene 3: $P(Gene3, Trait) = P(Gene3) \times P(Trait) = 0.501 \times 0.301 = 0.150801$.
- Gene 4: $P(Gene4, Trait) = P(Gene4) \times P(Trait) = 0.801 \times 0.301 = 0.241101$.
- Gene 5: $P(Gene5, Trait) = P(Gene5) \times P(Trait) = 0.327 \times 0.301 = 0.098727$.

- Gene 1: $P(Gene1, Trait) = P(Trait|Gene1) \times P(Trait) = 0.302 \times 0.702 = 0.211404$.
- Gene 2: $P(Gene2, Trait) = P(Trait|Gene2) \times P(Trait) = 0.302 \times 0.301 = 0.090902$.
- Gene 3: $P(Gene3, Trait) = P(Trait|Gene3) \times P(Trait) = 0.583 \times 0.501 = 0.292083$.
- Gene 4: $P(Gene4, Trait) = P(Trait|Gene4) \times P(Trait) = 0.371 \times 0.801 = 0.297471$.
- Gene 5: $P(Gene5, Trait) = P(Trait|Gene5) \times P(Trait) = 0.9 \times 0.327 = 0.2943$.

According to the calculations above, we can see that the probability of each gene and the trait is not equal to the conditional probability of the trait given each gene except maybe for the gene 1. Therefore, we can conclude that the genes are not independent of the trait except for the gene 1.

## Part (d)

According to the conditional probabilities for each gene and the trait, we can see that gene 5 has the highest probability of being associated with the trait while gene 1 has the lowest probability of being associated wih the trait, which is consistent with the results from part (c).
