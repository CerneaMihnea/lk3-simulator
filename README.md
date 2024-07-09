lk3-simulator
=============

This application is a simulator for an **IoT** device model **LK3**.

## Getting started

### Set up the enviroment

```bash

python3 -m vnev env
source env/bin/activate

```

### Install the necessary libraries

```bash
pip install flask gunicorn
```

### Start the app

```bash
python3 app.py 
```

### How to use the app

Access the main **URL (/)** to obtain the simulated data of the **LK3 IoT** device. These data are updated with each page access, providing a variety of values within the defined ranges.Base ip address is "127.0.0.1" and port "8001"

### Controller used for simulation

-  [LK3 controller](https://tinycontrol.pl/en/archives/lan-controller-30/)




