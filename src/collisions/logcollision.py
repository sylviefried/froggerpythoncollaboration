'''
Created on June 28, 2009

@author: William Madison
'''

from src.collisions.basecollision import BaseCollision

class LogCollision(BaseCollision):

  def __init__(self, entLog, entFrog):
    self.frogCollidedWith = entFrog
    self.logCollidedWith  = entLog

  def handleCollision(self):
    '''
      This is the function responsible for providing the 
      means of handling a collision of between a Log and a Frog.
    '''
    print "I done bumped into a log..."

  @property
  def FrogCollidedWith(self):
    return self.frogCollidedWith

  @property
  def LogCollidedWith(self):
    return self.logCollidedWith