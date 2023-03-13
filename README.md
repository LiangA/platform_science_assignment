# Driver Assignment

## Overview

In this project, I have applied [Hungarian algorithm](https://en.wikipedia.org/wiki/Hungarian_algorithm) to assign drivers to their destinations based on specific rules. The core algorithm used in this project is widely recognized as the best solution for assignment problem.

For the details of project design, implementation and analysis, please check [Module Document](./module_document.md).

## Getting Started

There are two ways to build up the environment: via *Github Codespace* or setup *locally* 

1. To use Github Codespace (new feature of github, not reliable but worth trying)
    - go to [this link](https://prod.liveshare.vsengsaas.visualstudio.com/join?D16BEEA6271F64940D1603D7328DBCC814A7) and you'll see a pop window like this
        ![image](https://user-images.githubusercontent.com/10252988/224461226-ece4b51d-4501-4cac-87a2-8c67aa428abf.png)
    - click "continue in web" and you'll see another pop window
        ![image](https://user-images.githubusercontent.com/10252988/224461275-16bea809-f311-4317-8ef3-0bb75920debe.png)
    - click "continue as anonymous" and type in a guest name
    - log into the terminal and start to test the module
    - (update) I noticed that ```pytest``` may not addded to path in the environment. You can try following commands to make it work:
      ```bash
      echo 'alias pytest="python /home/codespace/.local/lib/python3.10/site-packages/pytest/__main__.py"' > .bashrc
      source .bashrc
      ```
      Then ```pytest``` should be able to work:
      ```
      platform linux -- Python 3.10.4, pytest-7.2.2, pluggy-1.0.0
      rootdir: /workspaces/platform_science_assignment
      plugins: anyio-3.6.2
      collected 2 items                                                                                                                                                                           
      tests/test_algorithms.py ..                          [100%]
      ```

2. To run the project locally
    - make sure you have *Python 3.9+* and *pip* installed
        - [download python 3.9](https://www.python.org/downloads/release/python-390/)
        - [install pip](https://pip.pypa.io/en/stable/installation/)
        - after installing, you can run commands to test if the installations are success:
          ```bash
          python
          ```
          the output should be like
          ```
          Python 3.11.2 (main, Feb  8 2023, 14:49:25) [GCC 11.3.0] on linux
          Type "help", "copyright", "credits" or "license" for more information.
          >>>
          ```
          and
          ```bash
          pip --version
          ```
          the output should be like
          ```
          pip 23.0.1 from /home/alden/.local/lib/python3.11/site-packages/pip (python 3.11)
          ```
    - clone the repository to your local machine 
        ```bash
        git clone https://github.com/LiangA/platform_science_assignment.git
        ```
    - install the required packages
        ```bash
        cd platform_science_assignment
        pip install -r requirements.txt
        ```

## Usage

### To execute the program, run the following command: 

```bash
python driver_assignment.py --driver ./mock_data/driver_data --destinations ./mock_data/destinations_data
```

The ```--drivers``` and ```--destinations``` options are required. They are both *newline separated* files, and should contain *at least one* row of data (e.g. one name in drivers data and one address in destinations data). Any violation of the rule will cause an exception or wrong output. 

There are three sets of data in mock_data folder, you can add any set of data as you want.

### To run the tests, execute the following command:

```bash
pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.


