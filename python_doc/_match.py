def http_error(status):
  # case 401 | 403 | 404:
  # return "Not allowed"
  match status:
    case 400:
      return "Bad request"
    case 404:
      return "Not found"
    case 418:
      return "I'm a teapot"
    case _:
      return "Something's wrong with the internet"
    
    
    
class Point:
  __match_args__ = ('x', 'y')  # 自定义类可通过在类中设置特殊属性 __match_args__，为属性指定其在模式中对应的位置
  def __init__(self,x,y):
    self.x = x
    self.y = y

points  = [Point(0,0)]      

match points:
  case []:
    print("No points")
  case [Point(0,0)]:
    print("The origin")
  case [Point(x,y)]:
    print(f"A point at ({x},{y})")
  case [Point(0,y1), Point(0,y2)]:
    print(f"Two points on the y-axis at y={y1} and y={y2}")
  case _:
    print("Something else")
    
# match point:
#     case Point(x, y) if x == y:
#         print(f"Y=X at {x}")
#     case Point(x, y):
#         print(f"Not on the diagonal")

# 使用as关键字可以捕获子模式
# case Point(x, y) as p:


# 模式可以使用具名常量。它们必须作为带点号的名称出现，以防止它们被解释为用于捕获的变量
from enum import Enum
class Color(Enum):
  RED = "red"
  GREEN = "green"
  BLUE = "blue"

color = Color(input("Enter a color: "))

match color:
  case Color.RED:
    print("I see red!")
  case Color.GREEN:
    print("Grass is green")
  case Color.BLUE:
    print("I'm feeling the blues")
  case _:
    print("I don't know that color")
