class Coords:
    def __init__(self, coords):
        self.x, self.y = coords

    def by_delta(self, dx: float = 0, dy: float = 0):
        return self.__class__((self.x + dx, self.y + dy))


class State:
    CRAWL = 'crawl'
    FLYING = 'flying'
    FEET = 'feet'

    def __init__(self, state):
        self.state = state


class Direction:
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    UP = 'UP'
    DOWN = 'DOWN'

    def __init__(self, direction):
        self.direction = direction


class Field:
    def __init__(self):
        self.unit = None
        self.coords = None

    def set_unit(self, unit, coords):
        self.unit = unit
        self.coords = coords


class UnitMoveRequestDTO:
    def __init__(self, field: Field, direction: Direction, coords: Coords, state: State = State.FEET, speed: float = 1):
        self.field = field
        self.direction = direction
        self.coords = coords
        self.state = state
        self.speed = speed


class Unit:
    def move(self, request: UnitMoveRequestDTO):
        delta = self._get_speed_by_state(request.speed, request.state)
        new_coords = self._get_new_coords(request.coords, delta, request.direction)
        request.field.set_unit(self, new_coords)

    @staticmethod
    def _get_speed_by_state(original_speed, state):
        if state == State.CRAWL:
            return original_speed * 0.5
        if state == State.FLYING:
            return original_speed * 1.2
        if state == State.FEET:
            return original_speed
        raise ValueError(f'Unsupported state {state}')

    @staticmethod
    def _get_new_coords(old_coords: Coords, delta: float, direction: Direction) -> Coords:
        if direction == Direction.DOWN:
            return old_coords.by_delta(dy=-delta)
        if direction == Direction.RIGHT:
            return old_coords.by_delta(dx=delta)
        if direction == Direction.UP:
            return old_coords.by_delta(dy=delta)
        if direction == Direction.LEFT:
            return old_coords.by_delta(dx=-delta)
        raise ValueError(f'Unsupported direction {direction}')
