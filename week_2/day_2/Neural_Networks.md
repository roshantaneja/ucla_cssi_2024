---
tags:
  - lecture
  - notes
  - summer
  - CS
---
## Lecture Notes on Neural Networks Presentation

### Key Concepts
- **Neural Network (NN)**
- **Connection to Shallow Machine Learning Algorithms**
- **Multi-Layer Feed-Forward Neural Network**
- **Neural Network Design in General**
- **Training A Neural Network**
- **Practical Issues**
- **Deep Learning**

### Historical Context
- **AlphaGo (2015)**
- **AlphaZero (2017)**
- **Alpha Fold (2020)**
- **iOS Speech Synthesis (2016-)**
- **GPT-4**
- **DALLE-2**
- **ArXiv papers on deep learning (2012-2017)**

---

## Artificial Neural Networks (ANN)

### Human vs. Artificial Neurons
- **Humans:**
  - Number of neurons: ~
  - Connections per neuron: ~
  - Neuron switching time: ~0.001 second
  - Scene recognition time: ~0.1 second

- **Artificial Neural Networks:**
  - Many neuron-like threshold switching units
  - Many weighted interconnections among units
  - Highly parallel distributed process
  - Emphasis on tuning weights automatically

---

## Single Unit: Perceptron

### Structure
$$
o = f(\sum_{i=1}^{p} w_i x_i + b)
$$
- **Input vector**: $\mathbf{x}$
- **Weight vector**: $\mathbf{w}$
- **Activation function**: $f$
- **Output**: $o$
- **Bias**: $b$

### Parameters
- Number of parameters: $p + 1$ (weights + bias)

---

## General Neural Networks

### Multi-Layer Feed-Forward Neural Network
- **Layers**:
  - Input Layer
  - Hidden Layers
  - Output Layer

### Example Calculations
- **Number of parameters**:
  - Between two layers $t$ and $t+1$:
   $$
    \text{Parameters} = (m \times n) + n \quad \text{(including bias)}
   $$
    - If layer $t$ has $m$ neurons and layer $t+1$ has $n$ neurons.
  
---

## Important Concepts in NN

### Architecture
- Network topology
  - Number of units in input layer
  - Number of hidden layers
  - Units per hidden layer
  - Connection types between layers
  - Number of units in output layer

### Activation Functions
- **Sigmoid**: $\sigma(x) = \frac{1}{1 + e^{-x}}$
- **Tanh**: $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$
- **ReLU**: $\text{ReLU}(x) = \max(0, x)$
- **Leaky ReLU**: $\text{Leaky ReLU}(x) = \max(0.01x, x)$
- **Softplus**: $\text{softplus}(x) = \log(1 + e^x)$
- **Swish**: $\text{Swish}(x) = x \cdot \sigma(x)$

### Loss Functions
- **Squared error**: $L(y, \hat{y}) = \frac{1}{2} (y - \hat{y})^2$
- **Cross-entropy**: $L(y, \hat{y}) = -y \log(\hat{y}) - (1 - y) \log(1 - \hat{y})$
- **Hinge loss**: $L(y, \hat{y}) = \max(0, 1 - y \hat{y})$

### Optimization
- **Stochastic Gradient Descent (SGD)**
- **Backpropagation**
  - **Gradient descent step**: $w = w - \eta \frac{\partial L}{\partial w}$
  - **Learning rate**: $\eta$

### Regularization
- **L2 Regularization (Ridge)**: $L = L + \lambda \sum w_i^2$
- **L1 Regularization (Lasso)**: $L = L + \lambda \sum |w_i|$
- **Dropout**
- **Early Stopping**

---

## Training A Neural Network

### Learning Process
- **Initialization**: Start with random weights
- **Forward Pass**: Compute outputs
- **Loss Calculation**: Compare predicted and actual values
- **Backward Pass (Backpropagation)**: Adjust weights to minimize loss
  - **Gradient Calculation**
  - **Weight Update Rule**: $w = w - \eta \frac{\partial L}{\partial w}$

### Example
- **Heart Data Example**:
  - Assume a step function as activation, with initial weights and biases.
  - Evaluate output for given inputs and adjust weights iteratively using the loss function and gradient descent.

---

## Summary

### Key Takeaways
- Neural networks consist of multiple layers of perceptrons.
- They can approximate complex, non-linear functions.
- Essential components include:
  - Architecture design
  - Choice of activation function
  - Loss function selection
  - Optimization and regularization techniques

### Further References
- **3Blue1Brown NN series**: [YouTube Series](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- **Deep Learning Books**:
  - [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)
  - [Deep Learning Book](http://www.deeplearningbook.org/)
  - [Charu Aggarwal's Book](http://www.charuaggarwal.net/neural.htm)
  - [Dive into Deep Learning](http://d2l.ai/index.html)