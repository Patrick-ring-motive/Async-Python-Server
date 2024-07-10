def none():
  return None


def Q(function, parameters):
  try:
    return function(*parameters)
  except:
    return None


async def AQ(function, parameters):
  try:
    return await function(*parameters)
  except:
    return None

def b(str):
  return bytes(str, 'utf8')

false = False
true = True


def delete(obj, attr):
  try:
    del obj[attr]
    return obj
  except:
    return obj

def println(*args, **kwargs):
  return print(*args,"\n",**kwargs)