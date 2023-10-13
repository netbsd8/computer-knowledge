"""
127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0"
200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I
;Nav)"
"""

import sys
from collections import defaultdict

def dictify_logline(line):
    split_line = line.split()
    return {
        'remote_host': split_line[0],
        'status': split_line[8],
        'bytes_sent': split_line[9],
    }

def generate_log_report(logfile):
    m = defaultdict(int)
    ret = []
    with open(logfile, 'r') as f:
        for line in f:
            line_dict = dictify_logline(line)
            m[line_dict[0]] += line_dict[2]

    for key, val in m.items():
        item = [key] + [str(val)]
        ret.append(item)
    return ret

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print(__doc__)
        sys.exit(1)

    infile_name = sys.argv[1]
    log_report = generate_log_report(infile_name) 

