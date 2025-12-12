from pyscript import document

def compute_average(event):

    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)
    score3 = float(document.getElementById("score3").value)
    


    average = (score1 + score2 + score3) / 3
    average = round(average, 2)

  
    if average >= 75:
        result = "Yes"
    else:
        result = "No"

    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result