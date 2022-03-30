# Control Flow
  Control Flow refers to the use of comparison logic to determine what to do next. By that, I mean using if, elif, else statements to filter what code to run based on
  certain conditions. 

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
