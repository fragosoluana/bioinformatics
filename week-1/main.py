def pattern_count(text, pattern):
    count = 0
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if text[i:i+k] == pattern:
            count += 1
    return count


def find_max_words(freq_words, freq):
    max_words = []
    for pattern in freq_words:
        if freq_words[pattern] == freq:
            max_words.append(pattern)

    return max_words


def find_frequent_words(text, k):
    freq_words = {}
    most_freq_pattern = 0
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        if pattern not in freq_words:
            freq_words[pattern] = 0
        freq_words[pattern] += 1

        if freq_words[pattern] > most_freq_pattern:
            most_freq_pattern = freq_words[pattern]

    return find_max_words(freq_words, most_freq_pattern)


def reverse_pattern(text):
    reverse = ""
    dna_pairs = {"A": "T", "G": "C", "T": "A", "C": "G"}
    for i in range(len(text) - 1, -1, -1):
        reverse += dna_pairs[text[i]]
    return reverse


def find_pattern_start(pattern, genome):
    starts = ""
    k = len(pattern)
    for i in range(len(genome)):
        if genome[i:i+k] == pattern:
            starts += f"{i} "

    return starts.rstrip()


def find_clumps(k, l, t, genome):
    patterns = {}
    clumps = set()
    result = []

    for i in range(len(genome) - l + 1):
        pattern = genome[i:i+k]

        if pattern in clumps:
            continue

        if pattern in patterns and i - patterns[pattern][0] < l and i + k < i + l:
            patterns[pattern].append(i)
        else:
            patterns[pattern] = [i]

        if len(patterns[pattern]) >= t:
            if pattern not in clumps:
                clumps.add(pattern)
                result.append(pattern)

    return result


if __name__ == "__main__":
    file = open("E_coli.txt")
    # print(pattern_count(C, file.readline().rstrip()))
    # print(find_frequent_words(file.readline().rstrip(), int(file.readline().rstrip())))
    # print(reverse_pattern(file.readline().rstrip()))
    print(len(find_clumps(9, 500, 3, file.readline())))