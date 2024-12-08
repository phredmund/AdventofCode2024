def import_input():
    with open('day01/input.txt', mode="r") as f:
        return f.read()
    
def split_lists(raw_input):
    raw_split = raw_input.split('\n')
    left_list = []
    right_list = []
    for item in raw_split:
        x = item.split()
        left_list.append(int(x[0]))
        right_list.append(int(x[1]))
    return (left_list, right_list)

def compare_lists(list1, list2):
    total_delta = 0
    list1.sort()
    list2.sort()
    for index, item in enumerate(list1):
        x = item
        y = list2[index]
        total_delta = total_delta + abs(x - y)
    return total_delta

def get_similarity_score(list1, list2):
    total_score = 0
    for item in list1:
        x = list2.count(item)
        total_score = total_score + (item * x)
    return total_score

def main():
    input = import_input()
    input2 = split_lists(input)
    print(f"[Part 1] Total delta: {compare_lists(input2[0], input2[1])}")
    print(f"[Part 2] Similarity score: {get_similarity_score(input2[0], input2[1])}")
    

if __name__ == '__main__':
    main()

