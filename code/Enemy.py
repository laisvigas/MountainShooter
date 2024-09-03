#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_HEIGHT, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # initialize vertical movement for Enemy3
        if self.name == 'Enemy3':
            self.vertical_speed = ENTITY_SPEED['Enemy3Vertical']
            self.direction = 1  # 1 for moving down, -1 for moving up

    def move(self):
        if self.name == 'Enemy3':
            # move left horizontally
            self.rect.centerx -= ENTITY_SPEED['Enemy3']

            # move vertically
            self.rect.centery += self.vertical_speed * self.direction

            # check for window collisions and change direction if needed
            if self.rect.bottom >= WIN_HEIGHT:
                self.direction = -1  # start moving up
                self.vertical_speed = ENTITY_SPEED['Enemy3Vertical']  # reset speed to normal when moving up
            elif self.rect.top <= 0:
                self.direction = 1  # start moving down
                self.vertical_speed = ENTITY_SPEED['Enemy3Vertical'] * 2  # double speed when moving down
        else:
            # default movement for Enemy1 and Enemy2
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery))
