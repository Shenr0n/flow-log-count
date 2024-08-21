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
def get_output(flow_log, protocol_numbers, lookup_table, tags_count, port_protocol_count):

    untagged_count = 0
    tags_count_dict = {}
    port_protocol_count_dict = {}


    with open(flow_log, 'r', newline='') as logfile:
        for each_log in logfile:
            log_info = each_log.split()
            # Get dstport, protocol number from flow logs and then protocol name from protocol dict
            dstport, protocol = log_info[6], protocol_numbers[log_info[7]]

            # Check if (dstport,protocol) is in lookup dict, increment it's count or else mark it as untagged
            lookup_key = (dstport, protocol)

            if lookup_key in lookup_table:
                tags_count_dict[lookup_table[lookup_key]] += 1
            else:
                untagged_count += 1
            
            # Increment count value of (dstport,protocol) in port_protocol_op dict
            port_protocol_count_dict[lookup_key] += 1


    # Create a new output file for tags and port/protocol counts each, and write to it



def main():
    protocol_numbers, lookup_table = csv_to_dict("protocol-numbers-1.csv", "lookup_table.csv")

    get_output("flow_log.txt", protocol_numbers, lookup_table, "tags_count.txt", "port_protocol_count.txt")
    #print(lookup_table)
    #print(protocol_numbers)
    
    # Calling function for generating output
    #get_output()


if __name__ == "__main__":
    main()