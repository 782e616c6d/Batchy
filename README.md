<div id="header" align="center">
<img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png" alt="py-logo" width="200"/>
</div>
  
This project allows scripts to be executed remotely via a web interface.

### Technologies Used

* Flask (Python): Web framework for server development.
* HTML: Web page structure.
* JavaScript: Interactive client functionality.

### How it works

1. The user accesses the web page.
2. By clicking on one of the “Run Script” buttons, the path of the corresponding script is sent to the server.
3. The Flask server receives the request and executes the script provided.
4. The result of the execution (success or error) is sent back to the web page.
5. The result message is displayed to the user.

### Requirements

* Python 3.x
* Flask

### Installation

1. Clone this repository.
2. Install the dependencies:

```bash
pip install flask
```

### Running the Project

1. Navigate to the project folder.
2. Run the following command:

```bash
python app.py
```

3. Access `http://127.0.0.1:5000/` in your web browser.

### Usage

* Change the paths of the scripts defined in the `bottom1`, `bottom2`, and `bottom3` variables in the `script.js` file.
* Click on one of the “Run Script” buttons to execute the corresponding script.

### Security Considerations

* Running arbitrary scripts on the server can be a security risk. Make sure you limit the scripts that can be run and implement appropriate authentication and authorization mechanisms.
* Scripts must be located in a secure directory and accessible only by the application.
