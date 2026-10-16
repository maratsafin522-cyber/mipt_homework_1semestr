"""Physics of a simple solar system."""

gravitational_constant = 6.67408e-11


class Star:
    """Star with mass, position and velocity."""

    type = "star"
    m = 0
    x = 0
    y = 0
    Vx = 0
    Vy = 0
    Fx = 0
    Fy = 0
    R = 5
    color = "red"
    image = None


class Planet:
    """Planet with mass, position and velocity."""

    type = "planet"
    m = 0
    x = 0
    y = 0
    Vx = 0
    Vy = 0
    Fx = 0
    Fy = 0
    R = 5
    color = "green"
    image = None


def calculate_force(body, space_objects):
    """Calculate the gravitational force on a body."""
    body.Fx = 0
    body.Fy = 0

    for obj in space_objects:
        if obj is body:
            continue

        dx = obj.x - body.x
        dy = obj.y - body.y
        r = (dx ** 2 + dy ** 2) ** 0.5

        if r == 0:
            continue

        force = gravitational_constant * body.m * obj.m / r ** 3
        body.Fx += force * dx
        body.Fy += force * dy


def move_space_object(body, dt):
    """Update velocity and position using Newton's second law."""
    if body.m == 0:
        return

    body.Vx += body.Fx / body.m * dt
    body.Vy += body.Fy / body.m * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt


def angular_speed(body, star):
    """Calculate the angular speed of a body relative to a star."""
    dx = body.x - star.x
    dy = body.y - star.y
    dvx = body.Vx - star.Vx
    dvy = body.Vy - star.Vy
    r2 = dx ** 2 + dy ** 2

    if r2 == 0:
        return 0

    return abs(dx * dvy - dy * dvx) / r2


def areal_speed(body, star):
    """Calculate the area swept per second around a star."""
    dx = body.x - star.x
    dy = body.y - star.y
    r2 = dx ** 2 + dy ** 2
    return r2 * angular_speed(body, star) / 2


def recalculate_space_objects_positions(space_objects, dt):
    """Update forces, then velocities and positions of all bodies."""
    for body in space_objects:
        calculate_force(body, space_objects)

    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
