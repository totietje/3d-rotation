import numpy as np


# Generates a matrix that rotates a point |by| radians about the axis 'by'
# Black magic copy pasted from stackoverflow
def _rotation_matrix(by):
	"""
	Return the rotation matrix associated with counterclockwise rotation about
	the given unit vector axis by theta radians.
	"""

	theta = np.sqrt(np.dot(by, by))
	axis = np.asarray(by) / theta

	a = np.cos(theta / 2.0)
	b, c, d = -axis * np.sin(theta / 2.0)
	aa, bb, cc, dd = a * a, b * b, c * c, d * d
	bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
	return np.array([
		[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
		[2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
		[2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]
	])


def model_rotation(settings):
	moment_of_inertia = settings.moment_of_inertia
	total_time = settings.total_time
	delta_time = settings.delta_time
	angular_velocity = settings.initial_angular_velocity
	rotation = settings.initial_rotation
	angular_momentum = settings.angular_momentum

	rotations = {}

	for i in range(int(total_time / delta_time)):
		rotations[i] = (rotation, angular_velocity)

		# Rotate by angular velocity
		rotation = _rotation_matrix(angular_velocity * delta_time) @ rotation
		
		# Calculate new angular velocity based on new rotation & constant angular momentum
		# Rotating angular momentum by the box's rotation yields angular momentum from the box's perspective
		# Use H = I * omega, omega = I^-1 * H
		angular_velocity = np.linalg.inv(moment_of_inertia) @ rotation @ angular_momentum

	return rotations
