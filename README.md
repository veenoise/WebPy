
# WebPy

This is a lexical and syntax analyzer for our course Principles of Programming Language. The concept for this language is improving python by adding explicit static types to make less errors, bugs, and unexpected results while writing. This is a special purpose programming language suited for web developers as it also contains built-in `app` function for creating a web server.

## Authors

- [Janine Anne Arzadon](https://www.github.com/veenoise)
- [William Eduard Chua (@veenoise)](https://www.github.com/veenoise)
- [Jason Espallardo](https://www.github.com/veenoise)
- [David Garcia (@Davidg13229)](https://www.github.com/Davidg13229)
- [Whayne Tyrece Tan](https://www.github.com/veenoise)

## Tech Stack

**Client:** React, TailwindCSS, TypeScript, Shadcn, MagicUI, HTML, CSS, JavaScript

**Server:** Flask

## Requirements

- Docker
- 7-zip, WinRAR, or any file extraction software for .gz file extension

## Run Locally

### Get a copy of the docker image
Download the docker image in this repository. You can get it from the Releases section in the right side of the repo.

### Extract the docker image
Extract the docker image using the tool you have.

### Load the docker image

```bash
docker load -i=webpy-docker-image.tar
```

### Run the application

```bash
docker run -p 4444:4444 -p 5000:5000 webpy-docker-image:v1.0.0
```

### Access the web app

Visit http://localhost:4444/

### Stop the web app

After you're done using the web application, press `ctrl + c` 3 times to exit docker. Then, we can stop the process the docker is currently running. Do the command below to determine the process id of the running container.


```bash
docker ps
```

Example output:

```bash
CONTAINER ID   IMAGE                       COMMAND                  CREATED         STATUS         PORTS                                                                                  NAMES
42533aff0bc6   webpy-docker-image:v1.0.0   "sh -c 'echo 'WebPy …"   7 seconds ago   Up 7 seconds   0.0.0.0:4444->4444/tcp, :::4444->4444/tcp, 0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   agitated_goodall
```

Kill the process:

```bash
docker kill 42533aff0bc6
```

## Contributing

Contributions are always welcome!

To modify the design, go to `src > components`. If you want to modify the `/home` endpoint, go to `src > routes > Home.tsx`. Read more about TailwindCSS https://tailwindcss.com/docs/flex, Shadcn https://ui.shadcn.com/docs/components/tabs, and MagicUI https://magicui.design/docs/components/confetti.

Fork the repo first then make a feature branch. Make changes to the code. Then, pull request that feature branch.
