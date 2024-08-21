## Assumptions and Notes
- The flow logs entries only supports the version 2 default log format as described in the following [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html).
- All input files should be in the same folder as the program "flow_log_count.py" and "protocol-numbers-1.csv"
- The flow logs and lookup table are in files called "flow_log.txt" and "lookup_table.csv" respectively.
- "protocol-numbers-1.csv" contains the [Assigned Internet Protocol Numbers from IANA](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml), which I used, to get the protocol names from protocol numbers in flow logs. **This file is required for the program's operations.**
- The generated output is split into two files "tags_count.txt" and "port_protocol_count.txt" containing the Tag counts and Port/Protocol Combination counts respectively. The input files can be very large with thousands of mappings, so I split up the output into two files for ease of parsing. I skipped the "Tag Counts: " and "Port/Protocol Combination Counts: " in the first lines of these output files.


## Techstack

- [Python 3.9.1]([https://docs.python.org/3/library/csv.html])
- Visual Studio Code

