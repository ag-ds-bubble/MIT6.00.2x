# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: /home/john/Moocs/MITx6.00.2x V2 2020 1T/ps3b_precompiled.py
# Compiled at: 2020-05-24 03:07:34
# Size of source mod 2**32: 18085 bytes
import random, pylab

class NoChildException(Exception):
    """NoChildException"""
    pass


class SimpleVirus(object):
    """SimpleVirus"""

    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        prob = random.random()
        return prob < self.clearProb

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        prob = random.random()
        if prob < self.maxBirthProb * (1 - popDensity):
            child = SimpleVirus(self.maxBirthProb, self.clearProb)
            return child
        raise NoChildException()


class Patient(object):
    """Patient"""

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.getViruses())

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        survivedViruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                survivedViruses.append(virus)
            popDensity = float(len(survivedViruses)) / self.maxPop
            self.viruses = survivedViruses
            childViruses = []
            for virus in self.viruses:
                childViruses.append(virus)
                try:
                    child = virus.reproduce(popDensity)
                    childViruses.append(child)
                except NoChildException:
                    pass

            else:
                self.viruses = childViruses
                return self.getTotalPop()


def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    finalResults = None
    for i in range(0, numTrials):
        results = runSimulation(numViruses, maxPop, maxBirthProb, clearProb)
        if finalResults == None:
            finalResults = results
        else:
            for j in range(0, len(results)):
                finalResults[j] += results[j]
            else:
                for i in range(0, len(finalResults)):
                    finalResults[i] /= numTrials
                else:
                    pylab.plot(finalResults, label='SimpleVirus')
                    pylab.title('SimpleVirus simulation')
                    pylab.xlabel('Time Steps')
                    pylab.ylabel('Average Virus Population')
                    pylab.legend(loc='best')
                    pylab.show()


def runSimulation(numViruses, maxPop, maxBirthProb, clearProb):
    """ helper function for doing one simulation run """
    viruses = []
    for i in range(0, numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    else:
        patient = Patient(viruses, maxPop)
        numSteps = 300
        numVirusesEachStep = []
        for i in range(0, numSteps):
            numVirusesEachStep.append(patient.update())
        else:
            return numVirusesEachStep


class ResistantVirus(SimpleVirus):
    """ResistantVirus"""

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if drug in self.resistances:
            return self.resistances[drug]
        return False

    def isResistantToAll(self, drugList):
        for drug in drugList:
            if not self.isResistantTo(drug):
                return False
            return True

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                raise NoChildException()
        else:
            prob = random.random()
            if prob < self.maxBirthProb * (1 - popDensity):
                childResistances = {}
                for drug in self.resistances.keys():
                    resistanceProb = random.random()
                    if resistanceProb < self.mutProb:
                        childResistances[drug] = not self.resistances[drug]
                    else:
                        childResistances[drug] = self.resistances[drug]
                else:
                    child = ResistantVirus(self.maxBirthProb, self.clearProb, childResistances, self.mutProb)
                    return child

            raise NoChildException()


class TreatedPatient(Patient):
    """TreatedPatient"""

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.activeDrugs = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.activeDrugs:
            self.activeDrugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.activeDrugs

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        numResistantViruses = 0
        for virus in self.viruses:
            if virus.isResistantToAll(drugResist):
                numResistantViruses += 1
            return numResistantViruses

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        survivedViruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                survivedViruses.append(virus)
            popDensity = len(survivedViruses) / self.maxPop
            self.viruses = survivedViruses
            childViruses = []
            for virus in self.viruses:
                childViruses.append(virus)
                try:
                    child = virus.reproduce(popDensity, self.activeDrugs)
                    childViruses.append(child)
                except NoChildException:
                    pass

            else:
                self.viruses = childViruses
                return self.getTotalPop()


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    totalViruses = None
    resistantViruses = None
    for i in range(numTrials):
        total, resistant = runDrugSimulation(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, 150, 300)
        if totalViruses == None:
            totalViruses = total
            resistantViruses = resistant
        else:
            for j in range(0, len(total)):
                totalViruses[j] += total[j]
                resistantViruses[j] += resistant[j]
            else:
                for i in range(len(totalViruses)):
                    totalViruses[i] /= numTrials
                    resistantViruses[i] /= numTrials
                else:
                    pylab.plot((range(len(totalViruses))), totalViruses, label='Total')
                    pylab.plot((range(len(totalViruses))), resistantViruses, label='ResistantVirus')
                    pylab.title('ResistantVirus simulation')
                    pylab.xlabel('time step')
                    pylab.ylabel('# viruses')
                    pylab.legend(loc='best')
                    pylab.show()


def runDrugSimulation(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numStepsBeforeDrugApplied, totalNumSteps):
    """ Helper function for doing one actual simulation run with drug applied """
    assert numStepsBeforeDrugApplied <= totalNumSteps
    viruses = []
    for i in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    else:
        patient = TreatedPatient(viruses, maxPop)
        numVirusesEachStep = []
        numResistantVirusesEachStep = []
        for i in range(totalNumSteps):
            if i == numStepsBeforeDrugApplied:
                patient.addPrescription('guttagonol')
            numVirusesEachStep.append(patient.update())
            numResistantVirusesEachStep.append(patient.getResistPop(['guttagonol']))
        else:
            return (
             numVirusesEachStep, numResistantVirusesEachStep)
# okay decompiling ps3b_precompiled_38.pyc
