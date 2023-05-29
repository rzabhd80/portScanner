# portScanner
IP port scanner 
A cli application for scanning servers port on given ip

## How to set up :
in order to use this application, you should have **python**,**pip** and **virtualenv** installed. first off, create a virtualenv 
and activate it via source command. Then install all dependencies listed in `requirements.txt` via `pip install -r requirements.txt`.
once you have done so, you can run the application.

## How to use :
Since this app uses [argparse](https://docs.python.org/3/library/argparse.html) for parsing given arguments, you can simply use help descriptions
provided in the application. Here is a simple example :
`python app.py 192.168.200.10 --port 8080-8085 --protocol udp --action run`
this command scans ports from 8080 up to 8085 for any open udp connection,this app supports both TCP and UDP scanning.

### may i have your attention plz? :)

since this app is just a simple university project, i couldnt afford to spend a lot of time on it, thus there might be some inefficient implementations. 
Feel free to add issues or pull requests to make it better
