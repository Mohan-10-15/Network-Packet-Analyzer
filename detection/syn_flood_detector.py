import time

syn_tracker = {}

TIME_WINDOW = 10
SYN_THRESHOLD = 100

def detect_syn_flood(src_ip):

    current_time = time.time()

    if src_ip not in syn_tracker:
        syn_tracker[src_ip] = []

    syn_tracker[src_ip].append(current_time)

    syn_tracker[src_ip] = [
        t for t in syn_tracker[src_ip]
        if current_time - t <= TIME_WINDOW
    ]

    return len(syn_tracker[src_ip]) > SYN_THRESHOLD