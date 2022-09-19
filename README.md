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

## 6.Solution: API Configuration <br />
The solution is there in the user subfolder <br />
### Setting up main4.py <br />
Your main4.py script should start by importing the FASTAPI modules <br />
On the second line, you can use the FASTAPI method to construct your app, as follow <br />
```
from fastapi import FastAPI

app = FastAPI()

```
### A simple endpoint <br />
You can specify a route for a default endpoint as follows: <br />
```
@app.get("/{user}")
```
The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to: <br />

the path /  <br />
using a get operation <br />

Then, you can define your index() function .your function should return a simple string that says "Hello" to whatever name the user has specified as a query string, as follows: <br />
```
    return "Hello " + user

```

The complete code is inside users subfolder <br />
The main4.py script. <br />

## 7.Endpoint Scripting <br />
### Summary <br />
Start by reading relevant modules: <br />
```
import pandas as pd
from fastapi import FastAPI
```
Then, instantiate your app with the FASTAP() call <br />
```
app = FastAPI()
```
Create a function that will read and return files. We can call this function an auxiliary function, or in other words, a helper function: <br />

```
def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata
```
Specify our first endpoint, with a default route: <br />

```
@app.get("/{user}")
def index(user):
    return str(user=='Bradford') + '\n'
```
Now, the most important part: specify another endpoint, with a different route, that accomplishes another, more complex task: <br />
```
@app.get("/medians/{filename}")
def summary(filename):
    thedata=readpandas(filename)
    return str(thedata.median(axis=0))
```

Finally, run the app,from the command line key in the command the python script is named as main.py and it is there in the median sub folder <br />

```

uvicorn main:app --reload
```
## 9.Exercise:Endpint scripting
All the files associated with this exercise is in medians folder <br />
Configuring an API is only the first step to having a useful API. After configuration, you need to write scripts for endpoints that can provide useful information<br />
to you and other users of the API.<br />

In this exercise, you'll write scripts for API endpoints so they can provide useful information about data. <br />
### Instructions: Function for Reading Data 
he first thing you need to add to your main3.py script is a function for reading data. <br />
You can call your function readpandas(). It should take a filename string as its input. It should use a pandas method to read a CSV whose filename is given by the <br /> function input. It should return the DataFrame that it read. <br />
### Instructions: Size Endpoint

Next, you can write a "size" endpoint that enables users to check the size of a dataset. <br />

Your "size" endpoint needs to start with a line that specifies the app route (the route should be called '/size'). <br />

Your endpoint needs a function, that you can call size(). This function should read a query string from the API user called "filename". Then, your function should<br />call the readpandas() function you created previously, passing the filename as the argument to this function. This will enable you to get the Dataframe <br />specified by the filename. <br />

Finally, you need to add a return statement to your size() function. It should return the number of rows of the pandas DataFrame the function read. <br />

### Instructions - Summary Endpoint
Next, you can write a "summary" endpoint that enables users to check the summary statistics - in this case the mean of each column of a dataset. <br />

Your "summary" endpoint needs to start with a line that specifies the app route (the route should be called '/summary'). <br />

Your endpoint needs a function, that you can call summary(). This function should read a query string from the API user called "filename". Then, your function <br />should call the readpandas() function you created previously, passing the filename as the argument to this function. This will enable you to get the Dataframe <br /> specified by the filename. <br />

You need to add a return statement to your summary() function. It should return the mean of the column of the pandas DataFrame the function read. <br />

Finally, you should test your summary() function. There's a dataset in the /L5 directory of your workspace called testdata.csv. You can pass the name 'testdata.csv'<br /> to your summary() function, and check the column means of the file. . You can also test your size() function by passing the testdata.csv<br />filename to it, and checking that it's working correctly, and returning the correct size. <br />

## 10. Solution :Endpoint Scripting
All the code and support files are there in the summary sub folder <br />
#### Solution
#### Reading the data
Your readpandas() function can be short. It should take a filename as its only argument, and it can use the pd.read_csv() method to read a CSV into a DataFrame. It<br /> should return the DataFrame in its return statement. The whole function can be written as follows: <br />
```
def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata
```
#### Size Endpoint
Your size endpoint needs to start with `@app.get('/size/{filename}')`, which specifies the API route of your endpoint. <br />
Then, you need a function called size() then it reads the panda dataframe and return the string length. <br />
```
def size(filename):
    thedata=readpandas(filename)
    return str(len(thedata.index))
```
### Summary endpoint
Your summary endpoint needs to start with `@app.get('/summary/{filename}')`, which specifies the API route of your endpoint. <br />

Then, you need a function called summary().Then, it needs to call your readpandas() function to get a pandas DataFrame of the CSV that the user specifies,Then, it <br /> needs to call your readpandas() function to get a pandas DataFrame of the CSV that the user specifies. <br />
```
def summary(filename):
    thedata=readpandas(filename)
    return str(thedata.mean(axis=1))
```
To run the app in the command line we key in the following command <br />
```
uvicorn main3:app --reload
```

## 17.Exercise :Full reporting pipeline
The entire code and supporting files for the exercise is there in the pickle subfolder <br />
First, you'll configure a new API. This API will have a new app configuration file that you can call main2.py. <br />

Second, you'll write a new endpoint for the API. This new endpoint will read a pickle file for a deployed model, and it will also read a dataset. It will use the<br />deployed pickle file to make predictions for the dataset, and it will return the prediction it makes. <br />
#### nstructions - API configuration
You should configure your new API by writing a script called main2.py. <br />

The main2.py script should follow the same configuration instructions as our previously configured API app files: <br />
import the needed methods from the fASTAPI module <br />
construct an app with a construction method from FASTAPI <br />
specify an endpoint route called '/prediction', intended to provide model predictions <br />
Use command line utility to run the app <br />
After you've complete the basic configuration, you'll be ready to script the prediction endpoint (see next step). <br />
### Instructions - Scripting the prediction Endpoint

Your endpoint called '/prediction' should include a function called predict(), that you will define. Your predict()function should do all of the following: <br />

read the pickle file called deployedmodel.pkl from the /L5 directory of your workspace <br />
read the dataset called predictiondata.csv from the /L5directory of your workspace <br />
use the deployedmodel.pkl pickle file to make predictions for the predictiondata.csv dataset <br />
return the prediction <br />
After you write the code for this endpoint, you'll be ready to call the endpoint and check the predicted value. <br />
## 18. Solution:Full Reporting pipeline
All the required files are in the pickle subfolder <br />
### API configuration
You can configure the API by importing the FAST API methods from FASTAPI  module, as follows: <br />
```
import pandas as pd
import pickle
from fastapi import FastAPI
```
Then instantiate the app
```
app = FastAPI()
```

You can create the prediction endpoint by using the '@' character to specify the '/prediction' route, and defining a function as follows: <br />

```
@app.get('/prediction')
def prediction():
```
We also need to read the file that is csv using the pandas method <br />
```
def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata
```

Here is the code for the prediction function <br />
```
@app.get('/prediction')
def prediction():
    thedata=pd.read_csv('predictiondata.csv')
    with open('deployedmodel.pkl', 'rb') as file:
        themodel = pickle.load(file)
    prediction=themodel.predict(thedata)
    return str(prediction)
```
To run the code in the command line we key in the command <br />
```
uvicorn main2:app --reload
```

That's all about all the code from flask to fastapi. <br />
































