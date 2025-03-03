# fullstack intern assignment — nervesparks

hey,  
this is my submission for the fullstack developer intern assignment at nervesparks.

the task was simple on the surface — take a JSON file, read some routes, and spin up a flask server that handles them.  
but for me, it was more about writing something that feels clean, understandable, and easy to work with. nothing over the top. just solid, readable code that does exactly what it says it will.


## so, what does this do?

- you define your routes and middlewares in a `config.json` file.
- `generate_server.py` takes that config and builds out a fully working flask server.
- that server (in `server.py`) listens for requests on the paths you’ve set and responds as expected.

basically, you decide the structure, and the code handles the rest.


## how to get it running:

1. clone this repo:
```bash
git clone <repo-link>
cd fullstack-intern-assignment
```

2. install the requirements:
```bash
pip install -r requirements.txt
```

3. generate the server:
```bash
python generate_server.py
```

4. start the server:
```bash
python server.py
```

5. check if it works:  
head over to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and test the routes:
- `/` → a little welcome note
- `/hello` → just saying hello back
- `/user` (POST) → confirms the user creation


## structure of things:

| file | purpose |
|------|---------|
| `config.json` | the setup file where you write the routes and middlewares. |
| `generate_server.py` | reads the config and builds your server code. |
| `server.py` | the actual server that runs and handles the routes. |
| `requirements.txt` | keeps track of the dependencies needed to run this. |
| `README.md` | you're reading it :) |


## a small note:

i didn’t want this to feel complicated or heavy.  
just something that's easy to read, easy to run, and easy to build on if needed.

there’s definitely room to add more — like better error handling, extra middleware support, or making the config even smarter.  
but for now, this feels good to go.


thanks for checking it out :)  
and yeah, if you made it this far, i hope the code speaks for itself.