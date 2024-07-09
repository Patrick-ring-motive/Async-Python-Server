
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