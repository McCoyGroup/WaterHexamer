"""
Goal: The goal of this is to write a basic Discrete-weighted DMC code for an OH-stretch
Fundamentals: ... (Comma-separated list)
Related Exercises: ... (Comma-separated list)
"""

## Imports: put all import statments here
import numpy as np
import matplotlib.pyplot as plt

## Exports: put all the names of things we might want to use in other scripts here

__all__ = [
]

## Objects: put all the classes we're defining here
class Walker:
    def __init__(self,initialCoords):
        '''
        :param initialCoords: initial coordinates for each of our walkers
        '''
        self.coords=np.array([initialCoords])
        #Give the walkers coords, weights, and a potential energy value.
        #This is done by self.parameterICareAbout=WhatIWantItToBe
        #Coords should be a number of atoms x dimensions of the system matrix.


## Functions: put all the functions we're defining here
def getPotential(prefactor):
    """ Here we will get the potential for each walker.
    :param prefactor: 1/2*m*w^2
    :return: potArray
    """
    ### In the case of the OH stretch, we want to loop through our walkers and update the potential based on it's coords.
    ### we want to use 1/2*k*x^2 or prefactor*x^2 for our OH stretch

def birthOrDeath(Vref,prob):
    """
    :param Vref: Vref for the system, generated by getVref()
    :param prob: exp(-1*(curentV - Vref)*deltaTau)
    :return: nothing
    """
    ###This is the most complex part of our DMC. We're going to want to loop through
    ###our walkers. For each, we'll use a random number between 0 and 1 [see np.random.random()]
    ###used to determine if a walker is killed or replicated.
    ###We can begin by looping over out walkers and generating a probability. For each walker,
    ###we are going to compare the current potential energy to the Vref from the prior step.
    ###Using this difference and the timestep to generate our probability, we will use the
    ###random number generated above to determine what to do. First, we'll use the integer part
    ###to generate that many new copies of the walker and put them in a birth list. Then we compare the fractional part to
    ###our random number and use that to determine if we duplicate the walker one more time.
    ###EX: If we had 0.8, the walker would have a 0.8 probability of sticking around.
    ###If we have 1.8, we would replicate the walker and then it would still have a 0.8 probability
    ###of sticking around (though sticking around would mean we now had 2 copies of it)
    ###We should end up with a fresh list of walkers in our birthlist, which is our new myWalkers.

def moveRandomly(sigma):
    """ Here we will displace our walkers
    :param sigma: np.sqrt(deltaTau / m)
    :return: nothing
    """
    ###For each walker, we want to move their coordinate by an amount determined
    ###by a gaussian (np.random.normal might be useful here). Where should the gaussian be centered? Use sigma
    ###for width scaling.
def getVref(alpha,initialWalkers):
    """ Used to get Vref for your walkers.
    :param alpha: 1/(2*deltaTau)
    :param initialWalkers: the number of walkers at the start of the simulation
    :return: Vref
    """
    ### Here we want to start by calculating Vbar, the average potential of all walkers.
    ### We need to correct by a term in order to keep our number of walkers relatively consistant.
    ### this term takes the form alpha/initialWalkers*(currentWalkers-initialWalkers). Why are we using number of walkers
    ### here? They're a convineient stand-in, but for what? This will matter when you implement continuous weighting.


def run(initialWalkers,deltaTau,numTimeSteps,omega,mass,dimensions):
    """
    :param initialWalkers: The number of walkers you start with
    :param deltaTau: the size of the time step
    :param numTimeSteps: how many steps you want to complete
    :param omega: parameter for O-H stretch
    :param mass: reduced mass of OH
    :param dimensions: number of dimensions for the walkers, likely 1 here.
    :return:
    """
    ### We want to calculate simulation parameters such as sigma, then run
    ### Start by looping over numTimeSteps.
    ### We want to move our walkers, get their new potential, and to then birth and kill
    ### walkers based on Vref from the previous step (what happens on step 1?)
    ### After this we will again update the potential for our walkers, and then calculate/
    ### record Vref.
## Run Script: put the script we'd want to run from the command line here

if __name__ == '__main__':
    ...

# Useful Simulation Parameters/Functions:
wvnmbr = 4.55634e-6
omega = 3000.0000*wvnmbr #in atomic units
dimensions = 1
amutoelectron = 1.000000000000000000 / 6.02213670000e23 / 9.10938970000e-28
massH = 1.008 * amutoelectron
massO = 16 * amutoelectron
mass = (massH * massO) / (massH + massO)
initialWalkers=1000
deltaTau=1
numTimeSteps=1000
myWalkers = [Walker(0) for r in range(initialWalkers)]
run(initialWalkers,deltaTau,numTimeSteps,)
moveRandomly(sigma)
print()