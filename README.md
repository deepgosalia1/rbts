# Bitcoin Trading Application
# CS 6360 Term Project

* Hita Gangineni
* Deep Dimple Gosalia
* Bhavesh Prasad Pudi
* Shashank Kathavate

## Tools:
* Python3
* Flask
* Azure SQL
* React JS and its dependencies
   * "@emotion/react": "^11.5.0"
   * "@emotion/styled": "^11.3.0"
   * "@mui/icons-material": "^5.1.0"
   * "@mui/material": "^5.1.0"
   * "@mui/styled-engine": "^5.1.0"
   * "@mui/styled-engine-sc": "^5.1.0"
   * "@mui/styles": "^5.1.0"
   * "@mui/x-data-grid": "^5.0.0-beta.7"
   * "@testing-library/jest-dom": "^5.15.0"
   * "@testing-library/react": "^11.2.7"
   * "@testing-library/user-event": "^12.8.3"
   * "@tsamantanis/react-glassmorphism": "^1.1.2"
   * "aws-sdk": "^2.1033.0"
   * "bcrypt": "^5.0.1"
   * "bcryptjs": "^2.4.3"
   * "bootstrap": "^5.1.3"
   * "grommet": "^2.18.0"
   * "grommet-icons": "^4.6.2"
   * "isomorphic-fetch": "^3.0.0"
   * "mock-aws-s3": "^4.0.2"
   * "nock": "^13.2.1"
   * "plotly.js": "^2.6.3"
   * "react": "^17.0.2"
   * "react-bootstrap": "^2.0.2"
   * "react-datepicker": "^4.3.0"
   * "react-dom": "^17.0.2"
   * "react-plotly.js": "^2.5.1"
   * "react-scripts": "4.0.3"
   *  "sha1": "^1.1.1"
   *  "styled-components": "^5.3.3"
   *  "web-vitals": "^1.1.2"
* Python3 Packages:
  * flask,flask-cors
  * pyodbc
  * pandas
  * jsonify from flask
  * requests
  * apscheduler

## Database:
The application is developed on Azure tsql database,we have created a microsoft azure account and created our database table in azure transact sql.
  

## Install:
* The application first requires that Nodejs setup with a reactjs project and Python3.
* Using the inbuilt installation tool for python, Pip, the above mentioned packages need to be installed. This can be done by using the python -m pip install {package}.
* The above may be installed in a virtual environment (recommended).
* The application API must be run from the project directory.
* SQL server management studio, better known as SSMS can be downloaded and installed to manage the Azure cloud database. SSMS provides querying functionality and a user friendly UI to interpret database operation.


## Run:

* Run the python flask by navigating into API folder in the code and using the command:-
  ```
  py main.py
  ```
* Copy Paste the local ip of the machine being run in the file callApi.js line 9 and then run:-
  ```
  npm start
  ```



