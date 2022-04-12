def control_flow(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
          
print(control_flow(1000000))
print(control_flow(95))
print(control_flow(90))
print(control_flow(89))
print(control_flow(85))
print(control_flow(75))
print(control_flow(65))
print(control_flow(59))
print(control_flow(0))
print(control_flow(-1000))
