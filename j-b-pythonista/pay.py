import math

# Const values

Fulltime_40_Year=   2080
Fulltime_35_Year=   1820
Fulltime_40_Month=  160
Fulltime_35_Month=  140
Working_Day_40=     40
Working_Day_35=     35
YearWeeks=          52
Working_Week=       5
Federal_Holidays=   11
Month_in_Weeks=     4
Average_Year_Hours= 2022



class Pay:
    TIME_GIVEN  = ["Hourly", "Weekly", "Monthly", "Annually"]
    
    def __init__(self, lower_bound, upper_bound, time_given="Hourly", is_fulltime=True):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.time_given = time_given
        self.is_fulltime = is_fulltime
    
    def monthly_pay(self):
        if self.time_given == "Fulltime":
            return self.lower_bound / 12
        else:
            return self.lower_bound * Fulltime_40_Month    
        