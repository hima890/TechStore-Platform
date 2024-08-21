1. Terminate the Process Manually
After pressing CTRL+C, check if the Flask process is still running.

You can find the process by using the following command:

bash
Copy code
lsof -i :5000
This will show the process ID (PID) that is using port 5000.

To terminate the process, use:

bash
Copy code
kill -9 <PID>
Replace <PID> with the actual process ID from the previous command.