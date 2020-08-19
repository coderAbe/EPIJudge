import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def name(a, b):
    return Coordinate(x = a, y = b)

def maze_to_graphs(maze):
    graph = {}
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if not maze[i][j]:
                curr_vertex = name(i, j);
                graph[curr_vertex] = ([])
                if(i < len(maze) - 1 and not maze[i+1][j]):
                    graph[curr_vertex].append(name(i+1, j)) 
                if(i > 0 and not maze[i-1][j]):
                    graph[curr_vertex].append(name(i-1, j)) 
                if(j < len(maze[i]) - 1 and not maze[i][j+1]):
                    graph[curr_vertex].append(name(i, j+1)) 
                if(j > 0 and not maze[i][j-1]):
                    graph[curr_vertex].append(name(i, j-1)) 
    return graph


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    path = [] 
    def is_reachable(graph, curr, dest, visited=set()):
        if curr == dest:
            return True
        elif curr in visited or curr not in graph:
            return False
        path.append(curr)
        visited.add(curr)
        if any(is_reachable(graph, node, dest, visited) for node in graph[curr]):
            return True
        del path[-1]
        return False

    graph = maze_to_graphs(maze)

    is_reachable(graph, name(s.x, s.y), name(e.x, e.y))

    if path:
        path.append(e)


    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
