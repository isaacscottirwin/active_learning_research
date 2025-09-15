class LabeledPoint:
    def __init__(self, x_pos, y_pos, label=None):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.label = label

    def getPoint(self):
        return self.x_pos, self.y_pos
    
    def getXpos(self):
        return self.x_pos
    
    def getYpos(self):
        return self.y_pos
    
    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label    

    def __str__(self):
        return f"LabeledPoint(x={float(self.x_pos):.4f}, y={float(self.y_pos):.4f}, label={self.label})"

    def __repr__(self):
        # repr is usually meant to be unambiguous
        return f"LabeledPoint(x={float(self.x_pos)}, y={float(self.y_pos)}, label={self.label})"