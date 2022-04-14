import schemdraw
import schemdraw.elements as elm
from schemdraw import logic

with schemdraw.Drawing() as d:
    andGate = logic.And(inputs=2)
    logic.Or(inputs=2, xy=andGate.in1)