import time

from vpython import vector, box, arrow, color
import numpy as np
import rotation
import util

ARROW_LENGTH = 0.2

SETTINGS = util.Settings(initial_angular_velocity=np.array([.1, 3, .1]), total_time=20)


def to_vec(arr):
	return vector(arr[0], arr[1], arr[2])


box = box(size=to_vec(SETTINGS.dimensions))
angular_velocity_arrow = arrow(shaftwidth=0.01, color=color.green)

angular_momentum = SETTINGS.angular_momentum
angular_momentum_direction = angular_momentum / np.sqrt(np.dot(angular_momentum, angular_momentum))

angular_momentum_arrow = arrow(axis=to_vec(angular_momentum_direction * ARROW_LENGTH), shaftwidth=0.01, color=color.red)


def set_box_rotation(rot):
	box.axis = to_vec(rot[:, 0]) * SETTINGS.dimensions[0]
	box.up = to_vec(rot[:, 1]) * SETTINGS.dimensions[1]


def set_angular_velocity_arrow(omega):
	angular_velocity_arrow.axis = to_vec(omega * 0.1)


set_box_rotation(SETTINGS.initial_rotation)
set_angular_velocity_arrow(SETTINGS.initial_angular_velocity)


states = rotation.model_rotation(SETTINGS)

t0 = time.time()

while (time.time() - t0) < SETTINGS.total_time:
	rot, omega = states[(time.time() - t0) // SETTINGS.delta_time]

	set_box_rotation(rot)
	set_angular_velocity_arrow(omega)
