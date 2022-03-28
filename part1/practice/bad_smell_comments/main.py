class Unit:

    def move(self, field, x: int, y: int, d, is_flying: bool, is_crawling: bool, speed: int = 1):
        if is_flying and is_crawling:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_flying:
            speed *= 1.2
            if d == 'UP':
                new_y = y + speed
                new_x = x
            elif d == 'DOWN':
                new_y = y - speed
                new_x = x
            elif d == 'LEFT':
                new_y = y
                new_x = x - speed
            elif d == 'RIGHT':
                new_y = y
                new_x = x + speed
        if is_crawling:
            speed *= 0.5
            if d == 'UP':
                new_y = y + speed
                new_x = x
            elif d == 'DOWN':
                new_y = y - speed
                new_x = x
            elif d == 'LEFT':
                new_y = y
                new_x = x - speed
            elif d == 'RIGHT':
                new_y = y
                new_x = x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)