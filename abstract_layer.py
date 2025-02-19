import abc

class AbstractLayer(abc.ABC):

  @property
  @abc.abstractmethod
  def output_reps(self):
    """A list of names of Representations which the layer can return as output.
    """

  @abc.abstractmethod
  def translate(self, algorithm, output_representation) -> 'abstract_algorithm.AbstractAlgorithm':
#    assert(tuple(algorithm.representation.name, output_representation) in self.input_output_reps)
    """Translates the algorithm from its current representation to output_representation.

    Params:
      algorithm: An Algorithm object to be translated
      output_representation: The name of the output representation desired.

    Returns:
      Algorithm object with representation output_representation which implements the same functionality as algorithm.
    """
