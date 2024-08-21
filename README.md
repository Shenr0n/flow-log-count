## Assumptions and Notes
- The flow logs entries only supports the version 2 default log format as described in the following [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html). It is a text file and each log entry has 14 fields. The lookup table is defined as a csv file, and it has 3 columns, dstport,protocol,tag.
- "protocol-numbers-1.csv" contains the [Assigned Internet Protocol Numbers from IANA](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml), which I used, to get the protocol names from protocol numbers in flow logs. **This file is required for the program's operations.**
- The generated output is split into two files "tags_count.txt" and "port_protocol_count.txt" containing the Tag counts and Port/Protocol Combination counts respectively. The input files can be very large with thousands of mappings, so I split up the output into two files for ease of parsing. I skipped the "Tag Counts: " and "Port/Protocol Combination Counts: " strings in the first lines of these output files.
---
### Testing
- Testing was successful with a flow log file above 10 MB and lookup file with more than 14000 mappings.
- All other requirements from the instruction email, have been tested and satisfied as well.
- The sample input and output files from testing, have been provided in this repository.
- The program works without a Buffered Reader as the files are small enough.
---
### Techstack

- [Python 3.9.1](https://docs.python.org)
- Visual Studio Code
---
### Instructions to Compile/Run
- I used Python 3.9.1 for this assessment.
- All input files should be in the same folder as the program "flow_log_count.py" and "protocol-numbers-1.csv" **Files required.**
- The flow logs and lookup table inputs should be in files called "flow_log.txt" and "lookup_table.csv" respectively. Renaming of your input files might be required, if necessary.
- Two files are generated as outputs "tags_count.txt" and "port_protocol_count.txt".

##### After all input and program files are in the same folder, the following can be input in terminal to generate output files:

```
python3 flow_log_count.py
```
or
```
python flow_log_count.py
```

### Other References
https://docs.python.org/3/tutorial/errors.html

https://docs.python.org/3/library/string.html

https://docs.python.org/3/library/collections.html#collections.defaultdict