
# WebPy

This is a lexical and syntax analyzer for our course Principles of Programming Language. The concept for this language is improving python by adding explicit static types to make less errors, bugs, and unexpected results while writing. This is a special purpose programming language suited for web developers as it also contains built-in `app` function for creating a web server.

## Authors

- [Janine Anne Arzadon](https://www.github.com/veenoise)
- [William Eduard Chua (@veenoise)](https://www.github.com/veenoise)
- [Jason Espallardo](https://www.github.com/veenoise)
- [David Garcia (@Davidg13229)](https://www.github.com/Davidg13229)
- [Whayne Tyrece Tan](https://www.github.com/veenoise)

## Tech Stack

**Client:** React, TailwindCSS, TypeScript, Shadcn, MagicUI

**Server:** Flask

## Requirements

- Python 3.12.7
- Node.js v20.18.0

## Run Locally

### Clone the repo

```bash
git clone https://github.com/veenoise/WebPy.git
```

### Go to the project directory

```bash
cd WebPy
```

### Create a python virtual environment

```bash
python3 -m venv .venv
```

### Use the virtual environment

#### Windows:

```bash
.\venv\Scripts\activate
```

#### Linux:

```bash
source ./.venv/bin/activate
```

### Install dependencies

```bash
npm install
```

and

```bash
pip3 install -r requirements.txt
```

### Start the server

```bash
npm run dev
```

and open another terminal and run the Flask app

```bash
cd python_modules
python3 app.py
```

### Access the web app

Visit http://127.0.0.1:5137/

### Stop the web app

After you're done using the web application, press `ctrl + c` to stop react. Switch to the other terminal where Flask app is running, and press `ctrl + c` to stop it as well.

## Contributing

Contributions are always welcome!

To modify the design, go to `src > components`. If you want to modify the `/home` endpoint, go to `src > routes > Home.tsx`. Read more about TailwindCSS https://tailwindcss.com/docs/flex, Shadcn https://ui.shadcn.com/docs/components/tabs, and MagicUI https://magicui.design/docs/components/confetti.

Fork the repo first then make a feature branch. Make changes to the code. Then, pull request that feature branch.