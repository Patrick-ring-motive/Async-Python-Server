
def b(str):
  return bytes(str, 'utf8')

def zreadFile(filename):
  try:
    thisFile = open(filename, "r") 
    txt = thisFile.read()
    thisFile.close()
    return txt
  except Exception as e:
    if hasattr(e, 'message'):
        return e.message
    else:
        return f"{e}"

def zreadFileBytes(filename):
    try:
        thisFile = open(filename, mode="rb") 
        bts = thisFile.read()
        thisFile.close()
        return bts
    except Exception as e:
        if hasattr(e, 'message'):
            return b(e.message)
        else:
            return b(f"{e}")