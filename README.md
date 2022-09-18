# flask2fastapi
## Command to run the fastapi code <br />
Get inside the respective folders and run the following command : uvicorn main:app --reload <br />
make sure main is the name of the python file <br />
We need to run the code in the terminal.We need to be inside the respective folders such as within the medians folder.Make sure fastapi installed.python needs to be installed <br />
Using the command line prompt key in the command uvicorn main:app --reload <br />
## Summary <br />
In order to configure an API using FASTAPI.We will have to create a python script.We will call it as main.py <br />
The following needs to be accomplished for our main.py script <br />
* import needed capabilities from FASTAPI module.<br />
* Instantiate the app using FASTAPI() call <br />
* Import capabilities unicorn to run the app <br />
* Run the app using --reload parameters in command line <br />
## Demo <br />
We can configure the main.py script as follows. <br />
First we need to import capabilities from the FASTAPI module <br />
" from fastapi import Fast API " <br />
Then instantiate the app <br />
app = FastAPI() <br />
Then, specify the end point for the function. <br />
To run the app one important thing,unicorn capabilities need to be installed as it helps in running the script .<br />
uvicorn main:app --reload <br />
## Get started with FASTAPI <br />
To get going with FASTAPI we need to install FASTAPI <br />
We will use PIP to install FASTAPI as shown below <br />
pip install fastapi <br />
For code to execute properly we need uvicorn too <br />
pip install uvicorn <br />
I have worked on a windows system with Anaconda prompt <br />

First clone the repo <br />
make sure fastapi and uvicorn is installed <br />
Check for respective subfolders <br />
![alt text](https://github.com/AbhiLegend/flask2fastapi/blob/main/images/2.PNG) <br /> 
All the subfolders have python fastapi codes <br />
Now let's take a look at an example and see how to run the code. <br />
![alt text](https://github.com/AbhiLegend/flask2fastapi/blob/main/images/3.PNG) <br /> 
We are inside the user folder.Again,we see that there is a python file named as main4.py <br />
![alt text](https://github.com/AbhiLegend/flask2fastapi/blob/main/images/4.PNG) <br />
key in the command to run the code for fast api uvicorn main:app --reload <br />
We will see the app starts with logs being shown in command prompt <br />
![alt text](https://github.com/AbhiLegend/flask2fastapi/blob/main/images/5.PNG) <br />
if we pass in a string after the / in the browser.We will see the output being prompted <br />
![alt text](https://github.com/AbhiLegend/flask2fastapi/blob/main/images/6.PNG) <br />
We will see the output.Similarly other folders are to be explored and we can run the code accordingly <br />
## Explanation of the code as shown in Flask in Lesson 5 :Model reporting and monitoring <br />
### 3.Configuring API <br />
#### Demo <br />
The solution is under the user subfolder
You can configure an main4.py script as follows: <br />
First, import capabilities from the FAST API module: <br />
```
from fastapi import FastAPI

```
Then, instantiate the app: <br />
```
app = FastAPI()
```
Then, specify an endpoint with its own function: <br />
```
@app.get("/{user}")
def index(user):
    return "Hello " + user

```
Finally, run the app using command line 
```
uvicorn main4:app --reload

```














