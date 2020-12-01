# petri-project

## Installation

First, install the petri-project following:
- [NodeJS](https://nodejs.org/en/) (LTS recommended)
- [MongoDB](https://www.mongodb.com/)

Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).

Then, run `webgme start` from the project root to start . Finally, navigate to `http://localhost:8888` to start using petri-project!

## Domain Background

The goal of this design studio is to allow for the visualization an implementation of petri net models. The underlying domain is fairly straight-forward:
Every system is a Petri Net which is made up of 3 main components:
Places: indicated by circles in the implementation, contain a marking that indicates a non-zero integer status of each place.
Transitions: indicated by rectangles, when fired allow the transfer of one marking at a time from one place to another.
Arcs: indicated by directed lines, connect places to transitions and vice versa, forming the path via which markings are transferred.
The Petri Net is a very powerful visualization tool that can be generalizable to many different use cases:
	i. When every Transition has only one arc in and one arc out, it can be used to simulate a finite state machine.
	ii. When every Place has only one arc in and one arc out, it can be used to simulate a marked graph.
	iii. It is very useful for modeling communication networks, where markings may represent packages of information.
	iv. Generally, Petri Nets are very useful for many scientific domains as a very intuitive and often robust modeling domain.

## Implementation Details

The underlying basis of the implementation is the metamodel that describes the Petri Net domain. It is constructed in the Meta visualizer, and is the basis of
the Seed PetriNet. To put it to use, simply create a new project using the PetriNet seed. The seed also contains an Example PetriNet called Example.
Note: the 'projects' folder contains a few metamodels that were used in different iterations of forming the seed.
With the metamodel formed, the user is also able to create implementations in the Composition visualizer (similar to the Example).

The last visualizer that is available to the user is the PetriNetViz visualizer where models formed in the Composition view can be executed which a
petri net graphical visualizer. The background code for the formation of the visualizer uuses the JointJS library and is stored in the 'visualizers' section
within the 'src' folder. The Widget file is the file that primarily executes the actual look of the visualization. With this in mind, alterations to this
code could be made if one wished to change the style, look, and format of the visualizer. The control file connects the visualizer to the actual functionality
and thus has more influence on what the visualizer actually does.

The final functionality of the design studio is in the model interpreter. Stored in the 'plugins' section within the 'src' folder is the PetriNetCodeGenerator.
This plugin is available to every PetriNet implementation, and utilizes Formula to check and verify the domain to ensure it meets standards of Petri Nets.
In order to utilize the plugin, simply find the Plugin button in the top of the visualizer (within your model implementation), and run the PetriNetCodeGenerator.
In theory, the interpreter should be able to also identify if your model falls into one of several categories of special petri nets.
