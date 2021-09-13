import json

if __name__ == '__main__':

    try:
        with open('user.json', 'r') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])
        split = output.split(',')

        for obj in data:
            a = '\n'

            for b in split:
                a += f'{obj[b]},'

            a = a.removesuffix(',')
            output += a

        with open('user.csv', 'w') as f:
            f.write(output)

    except Exception as e:
        print(f"There is someting error: {str(e)}")