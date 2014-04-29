<<<<<<< HEAD
=======
# file containing the ingredients for the network class in network.py:
#   - Node
#   - Edge
#   - Input_Node and Output_Node subclasses 

>>>>>>> FETCH_HEAD
class Node:
    def __init__(self):
        self.EdgesIn = []
        self.EdgesOut = []
        self.LastOutputs = []
        self.Error = 0.0

         
    def Evaluate(self, input):
        sum = 0
        
<<<<<<< HEAD
        #sum the outputs of each incoming edge
        for e in self.EdgesIn
            sum += sum + (e.in.Evaluate(input) * e.weight)
         
        self.LastOutputs.append(sum)    
=======
        # store the outputs of each edge in an array
        for i, e in enumerate(self.EdgesIn):
            self.LastInput[i] = (e.in.Evaluate(input) * e.weight)
        
        # sum the elements of the input array
        output = sum(self.LastInput)
        
        # store the value to be outputted in the output array
        self.LastOutputs.append(output)    
>>>>>>> FETCH_HEAD
        return sum

    def evaluate(self, inputVector):
      self.lastInput = []
      weightedSum = 0
 
      for e in self.incomingEdges:
         theInput = e.source.evaluate(inputVector)
         self.lastInput.append(theInput)
         weightedSum += e.weight * theInput
 
      self.lastOutput = activationFunction(weightedSum)
      return self.lastOutput
    
<<<<<<< HEAD

       
=======
    def EvalError(self, truth):
        
        # if for some reason we haven't learned from our last error
        if self.Error != None
            return self.Error
        
        # if current node is an output node calculate error and return it
        # else if self.EdgesOut == []
            # self.Error = truth - self.LastOutputs[0]
            # return self.Error
        
        # else sum errors of output edges and eventually return error
        else
            for e in self.EdgesOut:
                self.Error += (e.weight * e.out.EvalError(truth))
                
            return self.Error
        
    def Learn(self, LearnRate):
        if not_(self.LastOutputs = [] or self.Error = None or self.LastInput = None)
            for i, e in enumerate(self.EdgesIn):
                e.weight += (LearnRate * self.LastOutputs[0] * (1 - self.LastOutputs[0]) *
                             self.Error * self.LastInput[i]
>>>>>>> FETCH_HEAD
            
        
class Output_Node(Node):
    def __init__(self, index)
        Node.__init__(self, index)
        
        # add index of the output of this node for the creation of the single output vector
        self.index = index
        
    def EvalError(self, truth)
        self.Error = truth[self.index] - self.LastOutputs[0]
        return self.Error
        
        
class Input_Node(Node): 
    def __init__(self, index):
        Node.__init__(self)
        
        # add index of the input to be assigned to this node
        self.index = index; 
<<<<<<< HEAD

   
    def evaluate(self, inputVector):
      self.lastOutput = inputVector[self.index]
      return self.lastOutput


class Edge
    def __init__(self, in, out):
=======
        
    def Evaluate(self, input):
        # should just return the correct value identified by index from the input
        output = input[self.index]
        self.LastOutputs.append(output)
        return output

class Edge:
    def __init__(self, in, out)
>>>>>>> FETCH_HEAD
        self.weight = random.uniform(0,1)
        self.in = in
        self.out = out
        
        # add self to input and output nodes
        in.EdgesOut.append(self)
        out.EdgesIn.append(self)

class BiasNode(InputNode):
   def __init__(self):
      Node.__init__(self)
 
   def evaluate(self, inputVector):
      return 1.0

class NeuralNetwork
    def __init__(self):
      self.inputNodes = []
      self.outputNode = None

    def evaluate(self, inputVector):
      return self.outputNode.evaluate(inputVector)

    def propagateError(self, label):
      for node in self.inputNodes:
         node.getError(label)
 
   def updateWeights(self, learningRate):
      for node in self.inputNodes:
         node.updateWeights(learningRate)
 
   def train(self, labeledExamples, learningRate=0.9, maxIterations=10000):
      while maxIterations > 0:
         for example, label in labeledExamples:
            output = self.evaluate(example)
            self.propagateError(label)
            self.updateWeights(learningRate)
 
            maxIterations -= 1
        
        