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




