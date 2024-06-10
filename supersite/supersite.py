"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
from supersite.functions import *
import pynecone as pc

class State(pc.State):
    selected_log: str = ""
    
    def select(log_name):
        #print("Selected log: " + log_name)
        selected_log = log_name

class ButtonState(pc.State):
    pass

        
log_dict = get_log_info()
names = list(log_dict.keys())
ids = list(log_dict.values())
        
def index():
    return pc.fragment(
        # menu
        pc.hstack(
            # home button
            pc.link(
                pc.button("Home"),
                href="/",
                button=True
            ),
            # devlog button
            pc.link(
                pc.button("Devlog"),
                href="/devlog",
                button=True
            ),
            # about button
            pc.link(
                pc.button("About"),
                href="/about",
                button=True
            ),

            pc.color_mode_button(pc.color_mode_icon(), float="right"),
            
            spacing="10%",
            justify="center",
            padding="3%"
        ),
        # project description
        pc.vstack(
            pc.heading("Research Experience Edge-Connected Technologies", font_size="xl"),
            pc.text("Principle Investigator:", size="sm", as_="b"),
            pc.text("Kartik V. Bulusu", size="sm", as_="i"),
            pc.text("Research Assistants:", size="sm", as_="b"),
            pc.text("Nathan Dixon (SUPER), Gustavo Londono, Rutvik Solanki, Boomika Karuppaiah", size="sm", as_="i"),

            pc.text("The research work encapsulating one of the National Academy of Engineering’s grand challenges engineering the Tools of Scientific Discovery is one of the overarching thematic areas of research under by supervision. The SUPER 2024 funding is being sought particularly in the areas of Internet of Things (IoT) and low-power, low-cost technologies toward developing portable, remote, or wearable devices. A wide spectrum of technologies such as single board computers (SBCs) like the Raspberry Pi and the Nvidia Jetson Nano and low-power microcontrollers such as ESP32 and the Raspberry Pi Pico along with a variety of sensors and actuators are integrated into these devices. The SBC-sensor/actuator units programmed to take on the role of either an edge-server or edge-node customized to the application being conceived.", 
                size="sm",
                padding="3%"
            ),
            # image 
            pc.image(src="assets/figure-1.jpg"),
            pc.box(
                pc.span("The objective of this highly cross-disciplinary research program is to develop technologies that implement an internet-of-things (IoT) framework with robust edge compute methodologies. ", font_weight="bold"), "The edge compute will not only involve standard algorithms for data analytics but also extend to deep learning methods with the potential of distributing the compute to connected devices within a spatio-temporal landscape with multiple sensors and actuators located in proximity to the data source. The research program builds on this idea of edge compute particularly on low-cost and low-powered devices wherein, the edge-server-node configurations will optimize the use of on-board computing resources to efficiently analyze data and transfer them to and from the end-user. A variety of communication protocols such as Zigbee, Lorawan, WiFi, Bluetooth, MQTT etc will be implemented on these customized laboratory-scale devices.",
                size="sm",
                padding="3%"
            ),
            pc.text("The most recent example of such as a system was developed by undergraduate students in the Department of Computer Science, GWU under the supervision of Prof. Kartik Bulusu (See Prior Faculty Experience with Supervision of Undergraduate Students for details in the students and their affiliations). The device shown in Figure 1 (A-C) is a lowcost, wireless data acquisitions system designed for the following applications: (i) Pump and sensor control in a temperature and humidity-controlled incubator for cell culture studies and (ii) Remote data acquisition and system diagnostics in refrigeration and air conditioning units. For cell-culture applications in incubators, this system integrated a dosing pump (Model: EZO-PMP, Atlas Scientific) capable of delivering very small dosages (in the micro- liters per minute range) of cell media by varying parameters such as flow rate, pump frequency, and total volume dispensed. These parameters were customizable to the requirements of cell-inoculated scaffolds and culturing protocols. Concurrently, real-time data was acquired from pH, conductivity, and temperature measurement sensors. For environmental diagnostic applications, barometric pressures and temperatures will be monitored using the same system with appropriate sensors. The data transfer was achieved through UART, SPI, and I2C protocols that allow both reading and writing functionality from sensors and instrumentation. The system was controlled using a smartphone-based RESTful API that communicated with the WiFi-enabled microcontroller mounted on the SBC (Raspberry Pi 3B+).",
                size="sm",
                padding="3%"
            ),
            pc.text("The overarching goal of the current research program is to create edge-connected devices for which SUPER funds and matching departmental funds are being sought. The funds if made available will support one undergraduate student in the Department of Computer Science, GWU. The research will synergistically couple high-fidelity measurements of biological and environmental particulate transport, low-cost and low power technologies with intelligent edge-compute capabilities and explore this novel area of research. The applications under consideration are non-invasive biosensing and health monitoring, air quality assessments and intelligent transportation.",
                size="sm",
                padding="3%"
            )
        )
    )
    
# about page
def about():
    return pc.text("About")

# def set_log_name(log):
#     log_name = log
#     return

# def get_log_name():
#     return log_name

# devlog page
def devlog():
        
    return pc.fragment(
        # menu
        pc.hstack(
            # home button
            pc.link(
                pc.button("Home"),
                href="/",
                button=True
            ),
            # devlog button
            pc.link(
                pc.button("Devlog"),
                href="/devlog",
                button=True
            ),
            # about button
            pc.link(
                pc.button("About"),
                href="/about",
                button=True
            ),
            pc.color_mode_button(pc.color_mode_icon(), float="right"),
            
            spacing="10%",
            justify="center",
            padding="3%"
        ),

        pc.vstack(
            pc.heading("Development Log", 
            size="lg",
            justify="center"
            ),
            # for each log, create a clickable card that contains a preview of the log
            pc.foreach(
                log_dict, 
                lambda log, id: pc.link(
                    pc.button(log, 
                              on_click = State.select(log)),
                    href="/log/" + (id+1),
                    button=True
                ),
            )
        )
    )


def log():
    return pc.text(State.selected_log)

# Add state and pages to the app.
app = pc.App(state=State)

app.add_page(index, route="/")
app.add_page(devlog, route="/devlog")
app.add_page(about, route="/about")

for id in ids:
    log_route = "/log/" + id
    print("added", log_route)
    app.add_page(log, route=log_route)


app.compile()