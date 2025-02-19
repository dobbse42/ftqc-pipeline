import qualtran
from qualtran._infra.gate_with_registers import get_named_qubits
from representations.Qualtran_Representation import Qualtran_Representation
from representations.Cirq_Representation import Cirq_Representation
import abstract_layer
from Algorithm import Algorithm

class Qualtran_Layer(abstract_layer.AbstractLayer):

  def __init__(self):
#    self.output_reps = [Qualtran_Representation, Cirq_Representation]
    pass

  def output_reps(self):
    return [Qualtran_Representation, Cirq_Representation]

  def translate(self, algorithm, output_representation):
    assert(output_representation in self.output_reps())
    assert(isinstance(algorithm.representation, Qualtran_Representation))
    if output_representation == Cirq_Representation:
      return self.translate_to_cirq(algorithm)
    else:
      print("invalid output representation.")
      return 1

  def translate_to_cirq(self, algorithm):
    quregs = get_named_qubits(algorithm.data.signature.lefts())
    circuit, _ = algorithm.data.to_cirq_circuit(**quregs)
    return Algorithm(circuit, Cirq_Representation)
