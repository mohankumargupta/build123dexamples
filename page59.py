from build123d import *
from ocp_vscode import *

from dataclasses import dataclass, field

@dataclass
class Parameters:
	diameter_a: int = 90
	diameter_b: int = 65
	diameter_c: int = 50
	diameter_d: int = 38
	diameter_e: int = 30
	diameter_f: int = 40
	g: float = 14.2
	h: float = 44.2
	i: float = 6
	j: float = 24
	k: float = 12.5
	l: int = field(init=False)
	m: int = field(init=False)
	chamfer: float = 3.5

	def calculated_values(self):
		self.l = (self.diameter_c - self.diameter_f)/2
		self.m = (self.diameter_c - self.diameter_d)/2

	def __post_init__(self):
		self.calculated_values()

		for attr_name in dir(self):
			if attr_name.startswith("diameter_"):
				suffix = attr_name.split("_")[-1]
				radius_name = f"radius_{suffix}"
				setattr(self, radius_name, getattr(self, attr_name) / 2)



params = Parameters()
print(params)
print(params.radius_e)

pts = [
  (params.radius_e, 0),
  (params.radius_a, 0),
  (params.radius_a, params.g),
  (params.radius_f, params.g),
  (params.radius_f, params.g + params.h),
  (params.radius_f + params.l, params.g + params.h),
  (params.radius_f + params.l, params.g + params.h + params.i + params.j),
  (params.radius_f + params.l - params.m, params.g + params.h + params.i + params.j),
  (params.radius_f + params.l - params.m, params.g + params.h + params.i),
  (params.radius_e, params.g + params.h + params.i),
(params.radius_e, 0),  
]
#print(pts)
line = Plane.XZ * Polyline(pts)
face = make_face(line)
#show(face)
solid = revolve(face)
show(solid)
#show_all()
