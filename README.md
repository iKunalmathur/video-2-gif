# Into

video2gif as the name says converts videos to GIF and provide a set of customized option to make GIF of your flavor

## Installation

Step 1 - Clone this repo

Step 2 - Create data and out folder (required)

Step 3 - MoviePy (required)

```python
(sudo) pip install moviepy
```

Checkout documentation for more : https://zulko.github.io/moviepy/install.html

## Usage

Run Script

```python
python main.py
```

User Inputs :

- File Path : (e.g. "./data/sample.mp4")
- 🏁 Start (in seconds) ? [default=0]
- 🚧 End (in seconds) ? [default=10]
- 🔍 Resize (between 1 - 0) ? [default=0.3] # reduce its size (to 30% of the original)
- 🐢 Speed (between 1 - 0) ? [default=0.5] # Play at half speed
- ⏲ FPS (Higher FPS higher build time) ? [default=5] 5 frames per second

Folders & Filename

- Output file name example "output_2022_03_15-12_57_18_PM.gif"
- "data" to store source files
- "out" to store outputs

## Credits

_old but gold_

For more stuff must checkout https://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python

### If this was helpful, please give a star to this repo. 😃
