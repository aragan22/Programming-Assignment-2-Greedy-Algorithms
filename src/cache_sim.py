import sys
from collections import deque, OrderedDict


def simulate_fifo(k, reqs):
    """
    FIFO (First-In, First-Out)
    """
    cache = set()
    order = deque()  # insertion order
    misses = 0

    for r in reqs:
        if r in cache:
            # hit
            continue

        # miss
        misses += 1
        if len(cache) < k:
            cache.add(r)
            order.append(r)
        else:
            # evict oldest
            victim = order.popleft()
            cache.remove(victim)
            cache.add(r)
            order.append(r)

    return misses


def simulate_lru(k, reqs):
    """
    LRU (Least Recently Used)
    """
    cache = OrderedDict()
    misses = 0

    for r in reqs:
        if r in cache:
            # hit: move to MRU
            cache.move_to_end(r, last=True)
        else:
            # miss
            misses += 1
            if len(cache) == k:
                # pop LRU (oldest)
                cache.popitem(last=False)
            cache[r] = True  # value is irrelevant

    return misses


def simulate_optff(k, reqs):
    """
    OPTFF (Belady’s Farthest-in-Future, optimal offline).
    """
    m = len(reqs)

    # Precompute next occurrence for each position i:
    # next_occ[i] = index j > i such that reqs[j] == reqs[i] and j is minimal,
    # or -1 if there is no future occurrence.
    next_occ = [-1] * m
    last_pos = {}  # value -> next index to the right

    for i in range(m - 1, -1, -1):
        r = reqs[i]
        if r in last_pos:
            next_occ[i] = last_pos[r]
        else:
            next_occ[i] = -1
        last_pos[r] = i

    cache = set()              # items currently cached
    next_for_key = {}          # item -> next occurrence index (or -1)
    misses = 0

    for i in range(m):
        r = reqs[i]
        if r not in cache:
            # miss
            misses += 1
            if len(cache) < k:
                cache.add(r)
            else:
                # choose victim with farthest next use (or never used again)
                victim = None
                best_effective = -1  # larger = farther in the future

                for x in cache:
                    nxt = next_for_key.get(x, -1)
                    # Treat "never used again" as infinity
                    effective = m + 1 if nxt == -1 else nxt
                    if effective > best_effective:
                        best_effective = effective
                        victim = x

                # evict victim
                cache.remove(victim)
                next_for_key.pop(victim, None)
                cache.add(r)

        # Update next occurrence information for r
        next_for_key[r] = next_occ[i]

    return misses


def main():
    data = sys.stdin.read().split()
    if len(data) < 2:
        return

    k = int(data[0])
    m = int(data[1])
    reqs = list(map(int, data[2:]))

    # If fewer than m requests were provided, truncate m
    if len(reqs) < m:
        m = len(reqs)
        reqs = reqs[:m]
    else:
        reqs = reqs[:m]

    fifo_misses = simulate_fifo(k, reqs)
    lru_misses = simulate_lru(k, reqs)
    opt_misses = simulate_optff(k, reqs)

    print(f"FIFO  : {fifo_misses}")
    print(f"LRU   : {lru_misses}")
    print(f"OPTFF : {opt_misses}")


if __name__ == "__main__":
    main()
