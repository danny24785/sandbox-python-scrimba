total_race_time=int(input("What is the total race time in seconds?"))
pitstops_amount=int(input("How many pitstops were made?"))
average_pitstop_duration=int(input("What was the average pitstop duration in seconds?"))

total_pitstop_time=int(pitstops_amount*average_pitstop_duration)
percentage_spent_in_pits=round(float((total_pitstop_time/total_race_time)*100), 2)

print(f"Total pitstop time in seconds: {total_pitstop_time} seconds")
print(f"Percentage of race time spent in pits: {percentage_spent_in_pits} procent")
if(percentage_spent_in_pits > 5):
    print("You need a new pit crew. 🛠️")