# Pac-Man Search Algorithms
Spring 2019

This MP requirement was described in https://courses.engr.illinois.edu/cs440/sp2019/assignments/MP1/web/assignment1.html
## Credit to team members:
- _Chuanyue Shen_
- Jiazheng Li
- Shuju Shi

## Implement:
Write your search algorithms in *search.py* and do not edit any other files, except for testing.

## Requirements:
```
python3
pygame
```
## Running:
The main file to run the mp is mp1.py:

```
usage: mp1.py [-h] [--method {bfs,dfs,greedy,astar}] [--scale SCALE]
              [--fps FPS] [--human] [--save SAVE]
              filename
```

Examples of how to run MP1:
```
python mp1.py bigMaze.txt --method dfs
```
```
python mp1.py tinySearch.txt --scale 30 --fps 10 --human
```

For help run:
```
python mp1.py -h
```
Help Output:
```
CS440 MP1 Search

positional arguments:
  filename              path to maze file [REQUIRED]

optional arguments:
  -h, --help            show this help message and exit
  --method {bfs,dfs,greedy,astar}
                        search method - default bfs
  --scale SCALE         scale - default: 20
  --fps FPS             fps for the display - default 30
  --human               flag for human playable - default False
  --save SAVE           save output to image file - default not saved
```
