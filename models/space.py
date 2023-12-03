class Space:
    def __init__(self, x: [], y: [], z: []):
        self.x = x
        self.y = y
        self.z = z
        
    def get_bounding_box(self):
        bounding_box = [
            (min(self.x), min(self.y), min(self.z)),
            (max(self.x), min(self.y), min(self.z)),
            (max(self.x), max(self.y), min(self.z)),
            (max(self.x), max(self.y), max(self.z)),
            (min(self.x), max(self.y), min(self.z)),
            (min(self.x), min(self.y), max(self.z)),
            (max(self.x), min(self.y), max(self.z)),
            (min(self.x), max(self.y), max(self.z)),
        ]
        return bounding_box
