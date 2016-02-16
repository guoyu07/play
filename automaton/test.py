#!/usr/bin/env python

from automaton import machines

m = machines.FiniteMachine()

m.add_state('up')
m.add_state('down')
m.add_transition('down', 'up', 'jump')
m.add_transition('up', 'down', 'fall')
m.default_start_state = 'down'

print m.pformat()

m.initialize()

m.process_event('jump')
print m.pformat()
print m.current_state
print m.terminated
m.process_event('fall')
print m.pformat()
print m.current_state
print m.terminated
