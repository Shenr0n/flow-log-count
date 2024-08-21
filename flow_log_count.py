import csv

# Function to extract information from lookup input file and the protocol numbers with keywords to dictionaries
def csv_to_dict(protocol_info, lookup_table):
    protocol_numbers = {}
    lookup = {}

    # Extract protocol info
    with open(protocol_info, 'r', newline='') as csvfile:
        protocol_reader = csv.DictReader(csvfile, delimiter=',')
        #next(protocol_reader)
        for protocol_row in protocol_reader:
            p_key = protocol_row['Decimal']
            # Removing the " (deprecated)" string from keyword
            p_value = protocol_row['Keyword'].lower().split(' (')[0]
            protocol_numbers[p_key] = p_value

    # Extract lookup table info
    with open(lookup_table, 'r', newline='') as csvfile:
        lookup_reader = csv.DictReader(csvfile, delimiter=',')
        for lookup_row in lookup_reader:
            l_key = (lookup_row['dstport'],lookup_row['protocol'].lower())
            lookup[l_key] = lookup_row['tag']

    return protocol_numbers, lookup


# Function to count the tags and port/protocol combinations and generate output

def main():
    protocol_numbers, lookup_table = csv_to_dict("protocol-numbers-1.csv", "lookup_table.csv")
    print(lookup_table)
    print(protocol_numbers)


if __name__ == "__main__":
    main()