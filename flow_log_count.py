import csv
from collections import defaultdict

# Function to extract information from lookup input file and the protocol numbers with keywords to dictionaries
def csv_to_dict(protocol_info, lookup_table):
    protocol_numbers = defaultdict(str)
    lookup = defaultdict(str)

    # Extract protocol info
    try:
        with open(protocol_info, 'r', newline='') as csvfile:
            protocol_reader = csv.DictReader(csvfile, delimiter=',')
            #next(protocol_reader)
            for protocol_row in protocol_reader:
                p_key = protocol_row['Decimal']
                # Removing the " (deprecated)" string from keyword
                p_value = protocol_row['Keyword'].lower().split(' (')[0]
                protocol_numbers[p_key] = p_value
    except FileNotFoundError:
        print(f"File {protocol_info} not found")
        return None, None
    except Exception as e:
        print(f"Error {e}")
        return None, None

    # Extract lookup table info
    try:
        with open(lookup_table, 'r', newline='') as csvfile:
            lookup_reader = csv.DictReader(csvfile, delimiter=',')
            for lookup_row in lookup_reader:
                l_key = (lookup_row['dstport'],lookup_row['protocol'].lower())
                lookup[l_key] = lookup_row['tag']
    except FileNotFoundError:
        print(f"File {lookup_table} not found")
        return None, None
    except Exception as e:
        print(f"Error {e}")
        return None, None

    return protocol_numbers, lookup


# Function to count the tags and port/protocol combinations
def get_count(flow_log, protocol_numbers, lookup_table):

    untagged_count = 0
    tags_count_dict = defaultdict(int)
    port_protocol_count_dict = defaultdict(int)

    try:
        with open(flow_log, 'r', newline='') as logfile:
            for each_log in logfile:
                log_info = each_log.strip().split()
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
    except FileNotFoundError:
        print(f"File {flow_log} not found")
        return None, None
    except Exception as e:
        print(f"Error {e}")
        return None, None

    tags_count_dict['Untagged'] = untagged_count
    return tags_count_dict, port_protocol_count_dict


# Create a new output file for tags and port/protocol counts each, and write to it
def generate_output(tags_count_dict, port_protocol_count_dict, tags_count, port_protocol_count):
    
    # Write Tag Counts output file
    try:
        with open(tags_count, 'w', newline='') as tags_count_file:
            tags_count_file.write("Tag,Count\n")
            for tag, count in tags_count_dict.items():
                tags_count_file.write(f"{tag},{count}\n")
    except Exception as e:
        print(f"Error {e}")


    # Write Port Protocol Combination Counts output file
    try:
        with open(port_protocol_count, 'w', newline='') as port_protocol_count_file:
            port_protocol_count_file.write("Port,Protocol,Count\n")
            for (port, protocol), count in port_protocol_count_dict.items():
                #port_protocol_count_file.write(port+','+protocol+','+str(count)+'\n')
                port_protocol_count_file.write(f"{port},{protocol},{count}\n")
    except Exception as e:
        print(f"Error {e}")

def main():

    # Loading CSV info into dictionaries
    protocol_numbers, lookup_table = csv_to_dict("protocol-numbers-1.csv", "lookup_table.csv")
    #print(lookup_table)
    #print(protocol_numbers)

    # Getting counts
    tags_count_dict, port_protocol_count_dict = get_count("flow_log.txt", protocol_numbers, lookup_table)
    #print(tags_count_dict)
    #print(port_protocol_count_dict)

    # Generate output files
    generate_output(tags_count_dict, port_protocol_count_dict, "tags_count.txt", "port_protocol_count.txt")


if __name__ == "__main__":
    main()