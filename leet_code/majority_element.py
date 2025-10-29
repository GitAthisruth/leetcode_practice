def majority_element_naive(elements):
    counter = {}
    for i in elements:
        counter[i] = counter.get(i,0)+1
    val = max(counter.items(),key=lambda x:x[1])
    if val[1]>len(elements)//2:
        return 1

    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))



