import cirq
from representations.Qualtran_Representation import Qualtran_Representation
from representations.Cirq_Representation import Cirq_Representation
import abstract_layer
from Algorithm import Algorithm


class Cirq_Layer(abstract_layer.AbstractLayer):

  def __init__(self):
    pass

  def output_reps(self):
    return [Qualtran_Representation, Cirq_Representation]

  def translate(self, algorithm, output_representation):
    assert(output_representation in self.output_reps())
    assert(isinstance(algorithm.representation, Cirq_Representation))
    if output_representation == Cirq_Representation:
      return self.optimize(algorithm)
    elif output_representation == Qualtran_Representation:
      return self.translate_to_qualtran(algorithm)
    else:
      print("invalid output representation")
      return 1

#This goes from cirq->cirq, and by default optimizes gate-count as much as possible without changing the number of
#qubits in the circuit. This is the most complicated function in this class by far, and should be continuously
#improved.

  def optimize(self, algorithm, criteria='conservative speed'):
    circuit = algorithm.data
    if criteria == 'conservative speed': #reduce gatecount as much as possible without introducing extra qubits.
      circuit = cirq.eject_phased_paulis(circuit)
      circuit = cirq.eject_z(circuit)
    return Algorithm(circuit, Cirq_Representation)

# TODO
  def transalte_to_qualtran(self, algorithm):
    pass
