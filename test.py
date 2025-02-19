#Testing the most basic and limited pipeline.

from representations.Qualtran_Representation import Qualtran_Representation
from representations.Cirq_Representation import Cirq_Representation
from layers.Qualtran_Layer import Qualtran_Layer
from layers.Cirq_Layer import Cirq_Layer
from Algorithm import Algorithm
import qualtran
import cirq

#import some basic example circuit from qualtran
import attrs
from typing import *

from qualtran.cirq_interop import CirqQuregT

@attrs.frozen
class SwapTwoBits(qualtran.Bloq):
    @property
    def signature(self):
        return qualtran.Signature.build(x=1, y=1)

    def as_cirq_op(
            self, qubit_manager, x: CirqQuregT, y: CirqQuregT
    ) -> Tuple[cirq.Operation, Dict[str, CirqQuregT]]:
        x, = x  # each is an array of length one
        y, = y
        op = cirq.SWAP(x, y)
        out_quregs = {'x': [x], 'y': [y]}
        return op, out_quregs

bb = qualtran.BloqBuilder()
x = bb.add_register('x', 1)
y = bb.add_register('y', 1)
x, y = bb.add(SwapTwoBits(), x=x, y=y)
x, y = bb.add(SwapTwoBits(), x=x, y=y)
cbloq = bb.finalize(x=x, y=y)

#instantiate an Algorithm object beginning in the qualtran representation
qual_algo = Algorithm(cbloq, Qualtran_Representation)

#call the qualtran->cirq layer
tran = Qualtran_Layer()
cirq_algo = tran.translate(qual_algo, Cirq_Representation)

#call the cirq->optimized layer
tran = Cirq_Layer()
opt_cirq_algo = tran.translate(cirq_algo, Cirq_Representation)

#call the optimized->qasm layer
#call the qasm->lsc layer
#call the lsc->tiscc layer

#the above should be accomplishable via a single Algorithm.transform(target_representation, path) call, where the
#  path is by default set to my basic pipeline. Algorithm.transform() should consult a known graph of representations
#  and find the possible paths from Algorithm.representation to target_representation, then choose one based on path
#  (with some default setting). This path is then retrieved and executed (maybe path is an object, or maybe
#  execute_path() is just some global function which calls the transformations on the algorithm in the right order.
