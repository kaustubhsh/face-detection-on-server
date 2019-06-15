# Face Detection on Server

It is a real time face detection project based on java script implemented project hosted through flask on python3.

It uses [OpenCv](https://opencv.org/) for the Face Detection using the [haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades) file.
It is hosted with Flask on localhost, Flask_ngrok on the local machine and can be implemented on the server using Apache2.

The front hand is developed using HTML and Java Script, that request for the webcam and send and receive  data from the server.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements from the requirement.txt file.

```bash
pip install -r requirements.txt 
```

## Usage
```bash 
python3 server.py
firefox index.html
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)
