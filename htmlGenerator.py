import dominate
from dominate.tags import *

def createPath(path, problem):
  doc = dominate.document(title='Path para el problema')
  with doc.head:
    link(rel='stylesheet', href='style.css')
  with doc:
    h1('Este es el path para resolver el ' + problem)
    with div(cls='container'):
      for grid in path:
        new_grid = (grid[i:i+4] for i in range(0, len(grid), 4))
        with table().add(tbody()):
          for subgrid in new_grid:
            with tr():
              for element in subgrid:
                if not element:
                  td('X', cls='vacio')
                  continue
                td(element)
  with open('path.html', 'w') as f:
    f.write(doc.render())