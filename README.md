# Xtractor

The **Xtractor** allows you to easily extract tables from a pdf. This is essentially a wrapper for the very versatile [PDF Plumber module](https://github.com/jsvine/pdfplumber) for users who want to be able to handle this on the command line.

## Installing dependencies

```
git clone <repo>
cd xtractor
python3 -m venv venv
source venv/bin/activate
python3 pip install -r requirements.txt
```

The above code sets up a virtual environment and installs the dependencies.

# Running the program

To run this repo in the activated virtual environment:

```
python3 xtractor.py "data/bhs_buidlings.pdf" --dfr
```

 While the program is working, you'll see a progress bar in the terminal. This will output a .csv in the `out` folder.

Voilà! You now have a .csv of data to do with what you please.

