const bottom1 = "C:\\Temp\\Python\\Bat\\bottom1.bat";
const bottom2 = "C:\\Temp\\Python\\Bat\\bottom2.bat";
const bottom3 = "C:\\Temp\\Python\\Bat\\bottom3.bat";

function RunScript(value) {
    fetch('/run_script', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ path: value })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            // Show a message to user.
            document.getElementById('result').textContent = data.message;
        })
        .catch(error => {
            console.error('Erro:', error);
            // Show a error message to user.
            document.getElementById('result').textContent = 'Error executing script.';
        });
}
