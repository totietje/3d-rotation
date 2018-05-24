import numpy as np


def cuboid_inertia(dimensions, mass=1):
	def _inertia(i, j):
		a = dimensions[i]
		b = dimensions[j]

		return (mass * (a * a + b * b)) / 12

	return np.array([
		[_inertia(1, 2), 0, 0],
		[0, _inertia(0, 2), 0],
		[0, 0, _inertia(0, 1)],
	])
