import numpy as np


def _rotation_matrix(omega, delta_time):
	theta = omega * delta_time
	x, y, z = theta[0], theta[1], theta[2]

	return np.array([
		[ 1, -z,  y],
		[ z,  1, -x],
		[-y,  x,  1],
	])


def model_rotation(settings):
	moment_of_inertia = settings.moment_of_inertia
	total_time = settings.total_time
	delta_time = settings.delta_time
	angular_velocity = settings.initial_angular_velocity
	rotation = settings.initial_rotation
	angular_momentum = settings.angular_momentum

	inverse_moment_of_inertia = np.linalg.inv(moment_of_inertia)

	rotations = {}

	for i in range(int(total_time / delta_time)):
		rotations[i] = (rotation, angular_velocity)

		# Rotate by angular velocity
		rotation = _rotation_matrix(angular_velocity, delta_time) @ rotation
		
		# Based on new rotation and conservation of linear momentum, calculate new angular velocity
		angular_velocity = rotation @ inverse_moment_of_inertia @ rotation.T @ angular_momentum

	return rotations
