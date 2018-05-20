import numpy as np


def _angular_momentum(rotation, angular_velocity, moment_of_inertia):
	return np.linalg.inv(rotation) @ moment_of_inertia @ angular_velocity


def _moment_of_inertia(mass, dimensions):
	def _inertia(i, j):
		a = dimensions[i]
		b = dimensions[j]

		return (mass * (a * a + b * b)) / 12

	return np.array([
		[_inertia(1, 2), 0, 0],
		[0, _inertia(0, 2), 0],
		[0, 0, _inertia(0, 1)],
	])


class Settings:
	def __init__(self, initial_angular_velocity, delta_time=0.0001, total_time=20, dimensions=None, mass=1, initial_rotation=np.identity(3)):
		self.initial_angular_velocity = initial_angular_velocity
		self.mass = mass
		self.total_time = total_time
		self.delta_time = delta_time
		self.initial_rotation = initial_rotation

		if dimensions is None:
			self.dimensions = [20, 50, 100]
		else:
			self.dimensions = dimensions

		self.moment_of_inertia = _moment_of_inertia(self.mass, self.dimensions)
		print(self.moment_of_inertia)
		self.angular_momentum = _angular_momentum(self.initial_rotation, self.initial_angular_velocity, self.moment_of_inertia)
		print(self.initial_angular_velocity)
		print(self.angular_momentum)