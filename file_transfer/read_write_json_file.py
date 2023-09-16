import json

def rw_json():
    # create data
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }

    # print json.dumps
    print ( json.dumps(data) )
    print ( json.dumps(data, indent=4) )

    # write json file using json.dumpS
        # get data
    json_str = json.dumps( data )
    print ( json_str )
        # write data into json file using json.dump
    with open( 'data.json', 'w', encoding='utf-8' ) as wf:
        json.dump( data, wf )
        # read data from file
    with open( 'data.json', 'r', encoding='utf-8' ) as rf:
        rData = json.load(rf)
        print ( rData )


if __name__ == '__main__':
    rw_json()