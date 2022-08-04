seconds = int(input('duration = ' ))
minutes = seconds//60
residue_from_minutes_in_seconds = seconds%60
hours = minutes//60
residue_from_hours_in_minutes = minutes%60
days = hours//24
residue_from_days_in_hours = hours%24

if seconds < 60:
  print(seconds, "сек")

if seconds >= 60 and seconds < 3600:
  print(minutes, 'мин', 
        residue_from_minutes_in_seconds, 'сек')

if seconds >= 3600 and seconds < 86400:
  print(hours, 'час', 
        residue_from_hours_in_minutes, 'мин',            
        residue_from_minutes_in_seconds, 'сек')

if seconds >= 86400:
  print(days, 'дн',
        residue_from_days_in_hours, 'час',  
        residue_from_hours_in_minutes, 'мин',      
        residue_from_minutes_in_seconds, 'сек')
