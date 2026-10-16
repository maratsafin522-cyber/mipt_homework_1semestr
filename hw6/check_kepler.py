from solar_physics import (
    Star, Planet, recalculate_space_objects_positions,
    angular_speed, areal_speed
)

sun = Star()
sun.m = 1.989e30

earth = Planet()
earth.m = 5.972e24
earth.x = 1.496e11
earth.Vy = 24000

objects = [sun, earth]

print("Day | Distance | Angular speed | Areal speed")

for day in range(361):
    if day % 30 == 0:
        dx = earth.x - sun.x
        dy = earth.y - sun.y
        r = (dx ** 2 + dy ** 2) ** 0.5

        omega = angular_speed(earth, sun)
        s = areal_speed(earth, sun)

        print(day, f"{r:.3e}", f"{omega:.3e}", f"{s:.6e}")

    recalculate_space_objects_positions(objects, 86400)
