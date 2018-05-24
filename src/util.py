import numpy as np


def _angular_momentum(rotation, angular_velocity, moment_of_inertia):
	return rotation @ moment_of_inertia @ rotation.T @ angular_velocity


class Settings:
	def __init__(self, initial_angular_velocity, moment_of_inertia, delta_time=0.0001, total_time=20, initial_rotation=np.identity(3)):
		self.initial_angular_velocity = initial_angular_velocity
		self.total_time = total_time
		self.delta_time = delta_time
		self.initial_rotation = initial_rotation
		self.moment_of_inertia = moment_of_inertia

		self.angular_momentum = _angular_momentum(self.initial_rotation, self.initial_angular_velocity, self.moment_of_inertia)
