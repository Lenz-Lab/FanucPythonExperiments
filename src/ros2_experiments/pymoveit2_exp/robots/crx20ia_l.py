from typing import List

class crx20ia:
    
    MOVE_GROUP_ARM: str = 'manipulator'
    PREFIX = 'crx20ia_l'
    
    def __init__(self):
        self._joint_names = [f'J{i}' for i in range(1, 7)]
        # self._joint_names.append('flange')
    
    @property
    def joint_names(self) -> List[str]:        
        return self._joint_names
    
    @property
    def base_link_name(self) -> str:
        return 'base_link'
    
    @property
    def end_effector_name(self) -> str:
        return 'tcp'
    