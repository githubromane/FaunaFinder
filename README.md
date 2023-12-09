# SantaWishList

This project was very rewarding, both for its completeness and for the application of the theoretical knowledge acquired in the Machine Learning in Production course. We think that these uses will be very useful for our future jobs.
Our site is a simple online Christmas list where you can add, delete or modify a gift.

## How To Run

### With Docker compose

1. Verify that you have Docker on your laptop.

2. Open a terminal in your project directory and run the command : 
```
docker-compose up
```

### Without Docker

1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command (on Windows):
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in the file `app.py`.



