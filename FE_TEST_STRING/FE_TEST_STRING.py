docs = [
    f"""Operating Principles""",

    f"""The RSTi-EP PACSystem controls the system and can be programmed with Proficy Machine Edition (PME). The EDGE controller collects and processes data, making it easy to access. """,

    f"""PACSystem connects to the distributor's inputs/outputs and sends data to the EDGE controller. Valves regulate the air flow, while sensors detect the piston position. """,

    f"""The AF2 IO-Link measures pressure/flow, filters air, and sends data to the BUS coupler. A cable connects the PACSystem to the BUS coupler.""",

    f"""Pneumatic Stand""",

    f"""Contents of the diagram""",

    f"""Compressor - AtlasCopco G2FF""",

    f"""Air preparation unit with a safety system""",
    f"""Valve 1 - Aventics 5/2 double solenoid valve, no detent""",
    f"""Valve 2 - Aventics 2x3/2 normally closed valve, no detent""",
    f"""Valve 3 - Aventics 5/3 double solenoid valve , closed center, no detent""",
    f"""Valve 4 - Aventics 5/2 single solenoid valve, spring return, no detent""",
    f"""Valve 5 - Airtac 5/2 air actuated valve""",
    f"""Cylinder 1 - Aventics Ø63, Stroke: 500""",
    f"""Cylinder 2 - Aventics Ø32, Stroke: 500""",
    f"""Cylinder 3 - Aventics Ø63, Stroke: 300""",
    f"""Cylinder 4 - Aventics Ø50, Stroke: 300""",

    f"""The compressor adds pressurized air into the system. The air must be filtered and monitored for any irregularities in airflow.""",

    f"""Electronically controlled valves (valve 1 to valve 4) are used to control the air distribution to the cylinders. """,

    f"""An electric signal from the PACSystem to the BUS coupler tells the distributors on what position to be. The purpose of Valve 1 is to control the bigger Valve 5 which allows higher air flow to cylinder 1 for high speed tests, while the other valves (numbers 2 to 4) control the other cylinders directly, allowing for normal speed tests. """,

    f"""A BUS coupler gets information from the PACSystem and actuates the distributors.""",

    f"""Sensor System""",

    f"""A pair of magnetic sensors are placed at each end of the cylinder to monitor the position of the rod. Being a digital sensor it only detects if the rod is extended or retracted. """,

    f"""The airflow sensor is analog and transmits the current airflow and pressure going through it. """,

    f"""Compute Area""",
    
    f"""Rxi2-LP Edge Controller""",

    f"""Edge computing is a distributed computing framework that brings computation and data storage closer to the sources of data.""",

    f"""Using the Rxi2-LP industrial PC we can use the data forwarded from the BUS coupler to store, process, graph and analyze information.""",

    f"""RSTi-EP PACSystem""",

    f"""A Programmable Automation Controller (PAC) is an industrial computer control system that continuously monitors the state of input devices and makes decisions based upon a custom program to control the state of output devices.""",

    f"""In our case, the PACSystems* RSTi-EP CPE115 PAC, takes inputs from sensors and based on programmed logic it switches the solenoid valves (outputs) in the system to allow air to flow, actuating the pistons. It can be programmed using Ladder Logic, Structured Text, C or Function Block Diagram.""",

    f"""PACs are digital computers that hold and execute embedded programs. The PAC, compared to the PLC, is better suited for more complex automation solutions dealing with advanced process control, motion control, visualization and much more.""",

    f"""The software used for programming is Proficy Machine Edition""",

    f"""Connections""",

    f"""The EDGE controller is used to gather data, process it, graph it and make it easily accessible.""",

    f"""The BUS coupler is used to connect the PACSystem to the outputs and inputs of the system as well as transmitting the data to the EDGE controller.""",

    f"""The valves control the flow of air, moving the pistons. """,
    
    f"""Connection between PACSystem and the BUS coupler is done via a M12-D to ethernet adaptor cable, from a LAN2 interface of he pac to the X7E1 port of the BUS and it makes connection between the programed logic and the inputs/outputs (sensors/valves).""",

    f"""Connection between AF2 is done via a M12-A splitter cable connected to the 2AI2M12-E I/O module for flow and pressure measurements. """,
    

    f"""Connection between the BUS coupler and the EDGE controller for analysis is done via a M12-A to USB cable.""",
    
    f"""Connection between a computer and the PACSystem is done by ETHERNET. After connection and addition of present IO-devices the project is ready for upload/download of any programmed  logic.""",
    
    f"""Inputs/Outputs""",
    
    f"""PACs have an open architecture and incorporate modular design, due to this the PAC cannot take inputs or outputs directly, it needs to have connected an I/O module. For this we are using the RSTi-EP PROFINET Network Adapter on the kart for its compact build and the more advanced AES bus coupler on the experimental stand.""",
    
    f"""HALL effect sensors are used to detect when the piston is at the extremities of the cylinder, so we know when to change the flow of air using the valves so that the piston keeps moving.""",
    
    f"""The AF2 flow sensor, IO-Link, is the first element in the circuit right after the FRL unit, it measures the flow and pressure in the system and returns the results as analog signals between 4 and 20 mA.""",
    
    f"""PC and user functions""",
    
    f"""The user can program the whole system using the software Proficy Machine Edition. """,
    
    f"""Node-RED is node-based used to gather and process data then send it to the InfluxDB database. Graphs are made in Grafana using SQL. """
    

]