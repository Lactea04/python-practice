import random
import math

class WeightLayer():
    def __init__(self):
        self.w1 = 0
        self.w2 = 0
        self.w3 = 0

    def set_data(self, w1, w2, w3):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

    def forward(self):
        self.w1 += 0.7
        self.w2 += 0.7
        self.w3 += 0.7

    def get_data(self):
        return (self.w1, self.w2, self.w3)

class NormWeightLayer(WeightLayer):
    def norm(self):
        exp_w = []
        exp_w.append(math.exp(self.w1))
        exp_w.append(math.exp(self.w2))
        exp_w.append(math.exp(self.w3))
        self.w1 = exp_w[0]/sum(exp_w)
        self.w2 = exp_w[1]/sum(exp_w)
        self.w3 = exp_w[2]/sum(exp_w)

def run(model, w1, w2, w3):
 model.set_data(w1, w2, w3)
 model.forward()
def driver():
 v1 = random.random()
 v2 = random.random()
 v3 = random.random()
 print("WeightLayer: ")
 base_layer = WeightLayer()
 run(base_layer, v1, v2, v3)
 (w1, w2, w3) = base_layer.get_data()
 print(f"After forward : {w1:0.3f}, {w2:0.3f}, {w3:0.3f}")
 print("-" * 40)
 print("NormWeightLayer: ")
 norm_layer = NormWeightLayer()
 run(norm_layer, v1, v2, v3)
 norm_layer.norm()
 (w1, w2, w3) = norm_layer.get_data()
 print(f"After forward + norm : {w1:0.3f}, {w2:0.3f}, {w3:0.3f}")
driver()