# Haitham jalal Abdullah - Quiz Solution
# Sorting function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Main Function
def find_missing_ranges(frames: list[int]) -> dict:
    sorted_frames = bubble_sort(frames)
    gaps = []
    longest_gap = []
    missing_count = 0
    expected = 1

    # Find gaps
    for frame in sorted_frames:
        if frame > expected:
            gap = [expected, frame - 1]
            gaps.append(gap)
            gap_size = frame - expected
            missing_count += gap_size
            if not longest_gap or gap_size > (longest_gap[1] - longest_gap[0] + 1):
                longest_gap = gap
        expected = max(expected, frame + 1)
    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count
    }

frames = [1, 2, 3, 5, 6, 10, 11, 16]
result = find_missing_ranges(frames)
print("Result:", result)