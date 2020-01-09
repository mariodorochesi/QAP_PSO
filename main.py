from srflp.reader import SRFLP
from pso.enjambre import Enjambre

''''
    @author : Mario Dorochesi Ollino
    @date   : 09-01-2019
    e537c28ce659274c37335cc911d089f2
'''

if __name__ == '__main__':
    enjambre = Enjambre(SRFLP('data/QAP_sko56_04_n')).ejecutar_pso()