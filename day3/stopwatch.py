from datetime import datetime

def stopwatch():
    input("Hit enter to start stopwatch ")
    start_time = datetime.now()
    input("Hit enter to stop stopwatch ")
    end_time = datetime.now()
    
    print(f"Time duration : {end_time - start_time}")

stopwatch()
