#author : Piyush Rajendra Chaudhari
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import cx_Oracle

connection = cx_Oracle.connect("piyush/piyushchaudhari@localhost")



def queryExecutor(qry1, qry2, qry3):
    totalCountOfUni = 0
    reqAvgGREScore = 0
    p = []  # empty list to have GRE SCORE of Selected applied Universities
    cursor = connection.cursor()
    l = list(cursor.execute(qry1))

    totalCountOfUni = totalCountOfUni + len(l)
    o = [p.append(i[1]) for i in l]
    l = list(cursor.execute(qry2))
    totalCountOfUni = totalCountOfUni + len(l)
    o = [p.append(i[1]) for i in l]
    l = list(cursor.execute(qry3))
    totalCountOfUni = totalCountOfUni + len(l)
    o = [p.append(i[1]) for i in l]
    reqAvgGREScore = statistics.mean(p)

    return totalCountOfUni, reqAvgGREScore


def logicDBFunc(pref1, pref2, pref3):
    cursor = connection.cursor()

    view = f'CREATE VIEW pref_uni AS SELECT preference1, preference2, preference3, GRE_SCORE FROM student_gre'
    cursor.execute(view)

    queryp1 = f'select preference1, GRE_SCORE from pref_uni where preference1 = \'{pref1}\''
    queryp2 = f'select preference2, GRE_SCORE from pref_uni where preference2 = \'{pref1}\''
    queryp3 = f'select preference3, GRE_SCORE from pref_uni where preference3 = \'{pref1}\''
    count1, average1 = queryExecutor(queryp1, queryp2, queryp3)

    # delUniSelected = Ui_prefMainWindow.comboUniDeleteSelect.currentText()
    # print(delUniSelected)
    # queryDelete = 'delete from UNIVERSITY_LIST where university_name = \'{}\''.format(delUniSelected)

    queryp4 = f'select preference1, GRE_SCORE from pref_uni where preference1 = \'{pref2}\''
    queryp5 = f'select preference2, GRE_SCORE from pref_uni where preference2 = \'{pref2}\''
    queryp6 = f'select preference3, GRE_SCORE from pref_uni where preference3 = \'{pref2}\''
    count2, average2 = queryExecutor(queryp4, queryp5, queryp6)
    queryp7 = f'select preference1, GRE_SCORE from pref_uni where preference1 = \'{pref3}\''
    queryp8 = f'select preference2, GRE_SCORE from pref_uni where preference2 = \'{pref3}\''
    queryp9 = f'select preference3, GRE_SCORE from pref_uni where preference3 = \'{pref3}\''
    count3, average3 = queryExecutor(queryp7, queryp8, queryp9)
    view1 = f'DROP VIEW pref_uni'
    cursor.execute(view1)
    # print("piyu")
    cursor.close()

    y = [count1, count2, count3]
    avgList = [average1, average2, average3]

    logicOfAdmission = list(zip(y, avgList))
    logicOfAdmission.sort(reverse=False)

    toRetrievePreference = {average1: pref1, average2: pref2, average3: pref3}

    xLabel = [pref1, pref2, pref3]

    colours = ['#FFA500', '#87CEEB', '#228B22']
    plt.xlabel("Entered Preferences")
    plt.ylabel("Applied Student Count")
    plt.bar(x=np.arange(1, 4), height=y, color=colours, width=0.3)

    titleMsgUni = toRetrievePreference[logicOfAdmission[0][1]]
    titleMsg = f'GRE Analyzer : Predicted University -> {titleMsgUni}'

    plt.title(titleMsg)
    plt.xticks(np.arange(1, 4), xLabel, rotation=45)
    plt.show()