import json
def main():
    lst =[]
    with open("values.json", "r") as f:
        data = json.loads(f.read())
        for i in data['values']:
            lst.append(i['value'])

    with open("tests.json", "r") as f1:
        data2= json.loads(f1.read())
        data2['value'] = lst[0]
        j = 1
        for i in data2['values']:
            i['value'] = lst[j]
            j+=1


    report = json.dumps(data2)
    with open("report.json", "w") as f2:
        f2.write(report)

if __name__ == '__main__':
    main()