def printJobScheduling(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    result = [False] * t
    job = ['-1'] * t
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
    return job

# Example usage
if __name__ == '__main__':
    number_of_jobs = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(number_of_jobs):
        job_id = input(f"Enter job ID for job {i+1}: ")
        deadline = int(input(f"Enter deadline (as a number) for job {i+1}: "))
        profit = int(input(f"Enter profit for job {i+1}: "))
        jobs.append([job_id, deadline, profit])
    
    time_slots = int(input("Enter the number of time slots available: "))
    
    print("Following is maximum profit sequence of jobs:")
    scheduled_jobs = printJobScheduling(jobs, time_slots)
    print(scheduled_jobs)
