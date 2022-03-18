def char_validator_thompson(char):
    if char in ["*","?","|","_","+"]:
        return False
    elif char == "ε":
        return True
    elif char.isalpha():
        return True
    elif char.isnumeric():
        return True  
    else: 
        return False

def char_validator_afn(self,char):
        if char.isalpha():
            return True
        elif char.isnumeric():
            return True
        elif char == "ε":
            return True          
        else: 
            return False

def char_validator_leaf(char):
  if char.isalpha():
    return True
  elif char.isnumeric():
    return True
  elif char == "ε":
    return True
  elif char == "#":
    return True
  else: 
    return False
