from midpointCircle import drawCircle
from midpointLine import drawLine

class Container:
    def __init__(self, padding=0, corner_radius=0, color=(0, 0, 0), border_width=0, border_color=(0, 0, 0),offset=(0,0)):
        self.padding = padding
        self.corner_radius = corner_radius
        self.color = color
        self.border_width = border_width
        self.border_color = border_color
        self.x = offset[0]
        self.y = offset[1]
        
    
    def render(self):
        
        
        