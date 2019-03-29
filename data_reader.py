import os

if not os.path.isfile('data.csv'):
    data = open('data.csv', 'w')

    files_to_be_read = ['combined_data_1.txt', 'combined_data_2.txt', 'combined_data_3.txt', 'combined_data_4.txt']

    for file in files_to_be_read:
        with open('C:/Users/Akshay Medge/Downloads/netflix-prize-data/{}'.format(file)) as opened_file:
            for line in opened_file:
                line = line.strip()
                if line.endswith(':'):
                    m_id = line.replace(':', '')
                else:
                    row = [x for x in line.split(',')]    # row = line.split(',')
                    row.insert(0, m_id)
                    data.write(','.join(row))   # data.write(','+'row')
                    data.write('\n')
            print('done with {} file'.format(file))
    data.close()
