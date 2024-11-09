import numpy as np 


def read_inputs(filename: str) -> list[str]:
    with open(filename, "r") as f:
        lines = f.readlines() 

    return lines 


def part1() -> None: 
    filename = "part1.txt"
    lines = read_inputs(filename) 

    # Parse 
    words_line = lines[0]
    words = words_line[6:].strip("\n").split(",")
    
    runes = lines[2].strip("\n") 
    
    word_count = 0
    for i in range(len(runes)):
        for word in words:
            n = len(word)
            if runes[i:i+n] == word:
                word_count += 1

    print(f"Part1: {word_count}")

def part2() -> None:
    filename = "part2.txt"
    lines = read_inputs(filename) 

    # Parse 
    words_line = lines[0]
    words = words_line[6:].strip("\n").split(",")
    
    counts = 0 
    for runes in lines[2:]:
        runes = runes.strip("\n")
        n = len(runes)
        s = set()
        # Forward pass
        for i in range(n):
            for word in words:
                m = len(word)
                if runes[i:i+m] == word or runes[i:i+m] == word[::-1]:
                    s.update(list(range(i, i+m)))
                
        
        counts += len(s)

    print(f"Part2: {counts}")


def part3() -> None: 
    filename = "part3.txt"
    lines = read_inputs(filename)

    # Parse 
    words_line = lines[0]
    words = words_line[6:].strip("\n").split(",")

    n = len(lines[2:])
    m = len(lines[2]) - 1
    mat = np.empty((n, m), dtype="str")
    
    for i, line in enumerate(lines[2:]):
        for j, c in enumerate(line.strip("\n")):
            mat[i][j] = c


    
    s = set() 
    # Rows 
    for i in range(n):
        row = np.hstack((mat[i], mat[i], mat[i]))
        for j in range(m):
            for word in words:
                w = np.array([c for c in word])
                k = len(w)
                if np.all(row[j: j+k] == w) or np.all(row[j: j+k] == w[::-1]):
                    idxs = (np.array(list(range(j, j+k))) % m).tolist()
                    idxs = [(i,id) for id in idxs]
                    s.update(idxs)


    # Cols 
    for j in range(m):
        # col = np.hstack((mat[:, j]))
        col = mat[:, j].tolist()
        col = "".join(col)
        for i in range(n):
            for word in words:
                # w = np.array([c for c in word])
                # k = len(w)
                k = len(word)
                if col[i: i+k] == word or col[i:i+k] == word[::-1]:
                    idxs = (np.array(list(range(i, i+k))) % n).tolist()
                    idxs = [(id, j) for id in idxs]
                    s.update(idxs)

    counts = len(s)
    print(f"Part3: {counts}")

if __name__ == "__main__":
    part1()
    part2()
    part3()
