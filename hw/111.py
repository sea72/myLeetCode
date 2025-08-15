from math import inf

n = int(input())
before = input()
costs = list(map(int, input().split()))


# status
# one color:
#          0. 000   1. 111   2.222
# two color
#          3. 001   4. 002   5. 100  6. 122  7. 200  8. 211
# three color
#          9. 012    10. 021    11.102    12. 120   13. 201   14. 210

dp = [  [inf] * 15 for _ in range(n+1) ]
for j in range(15):
    dp[0][j] = 0

for i in range(1, n+1):
    cost = [ costs[i-1] if before[i-1] != str(j) else 0 for j in range(3) ]
    dp[i][0] = dp[i-1][0] + cost[0]
    dp[i][1] = dp[i-1][1] + cost[1]
    dp[i][2] = dp[i-1][2] + cost[2]

    if i >= 2:
        dp[i][3] = min(dp[i - 1][0], dp[i - 1][3]) + cost[1]
        dp[i][4] = min(dp[i - 1][0], dp[i - 1][4]) + cost[2]
        dp[i][5] = min(dp[i - 1][1], dp[i - 1][5]) + cost[0]
        dp[i][6] = min(dp[i - 1][1], dp[i - 1][6]) + cost[2]
        dp[i][7] = min(dp[i - 1][2], dp[i - 1][7]) + cost[0]
        dp[i][8] = min(dp[i - 1][2], dp[i - 1][8]) + cost[1]

    if i >= 3:
        dp[i][9] = min(dp[i - 1][3], dp[i - 1][9]) + cost[2]
        dp[i][10] = min(dp[i - 1][4], dp[i - 1][10]) + cost[1]
        dp[i][11] = min(dp[i - 1][5], dp[i - 1][11]) + cost[2]
        dp[i][12] = min(dp[i - 1][6], dp[i - 1][12]) + cost[0]
        dp[i][13] = min(dp[i - 1][7], dp[i - 1][13]) + cost[1]
        dp[i][14] = min(dp[i - 1][8], dp[i - 1][14]) + cost[0]

print(min(dp[-1]))




from array import array

INF = 10**15
n = int(input())
before = input()
costs = list(map(int, input().split()))

prev = array('q', [0] * 15)
cur = array('q', [0] * 15)

for i in range(1, n + 1):
    orig_color = ord(before[i - 1]) - 48
    c0 = 0 if orig_color == 0 else costs[i - 1]
    c1 = 0 if orig_color == 1 else costs[i - 1]
    c2 = 0 if orig_color == 2 else costs[i - 1]

    # one color
    cur[0] = prev[0] + c0
    cur[1] = prev[1] + c1
    cur[2] = prev[2] + c2

    if i >= 2:
        cur[3] = (prev[0] if prev[0] < prev[3] else prev[3]) + c1
        cur[4] = (prev[0] if prev[0] < prev[4] else prev[4]) + c2
        cur[5] = (prev[1] if prev[1] < prev[5] else prev[5]) + c0
        cur[6] = (prev[1] if prev[1] < prev[6] else prev[6]) + c2
        cur[7] = (prev[2] if prev[2] < prev[7] else prev[7]) + c0
        cur[8] = (prev[2] if prev[2] < prev[8] else prev[8]) + c1

    if i >= 3:
        cur[9]  = (prev[3] if prev[3] < prev[9] else prev[9]) + c2
        cur[10] = (prev[4] if prev[4] < prev[10] else prev[10]) + c1
        cur[11] = (prev[5] if prev[5] < prev[11] else prev[11]) + c2
        cur[12] = (prev[6] if prev[6] < prev[12] else prev[12]) + c0
        cur[13] = (prev[7] if prev[7] < prev[13] else prev[13]) + c1
        cur[14] = (prev[8] if prev[8] < prev[14] else prev[14]) + c0

    prev, cur = cur, prev  # 滚动数组

print(min(prev))




# from array import array

# INF = 10**15
# n = int(input())
# before = input()
# costs = list(map(int, input().split()))

# prev = array('q', [0] * 15)
# cur = array('q', [0] * 15)

# for i in range(1, n + 1):
#     orig_color = ord(before[i - 1]) - 48
#     c0 = 0 if orig_color == 0 else costs[i - 1]
#     c1 = 0 if orig_color == 1 else costs[i - 1]
#     c2 = 0 if orig_color == 2 else costs[i - 1]

#     # one color
#     cur[0] = prev[0] + c0
#     cur[1] = prev[1] + c1
#     cur[2] = prev[2] + c2

#     if i >= 2:
#         cur[3] = (prev[0] if prev[0] < prev[3] else prev[3]) + c1
#         cur[4] = (prev[0] if prev[0] < prev[4] else prev[4]) + c2
#         cur[5] = (prev[1] if prev[1] < prev[5] else prev[5]) + c0
#         cur[6] = (prev[1] if prev[1] < prev[6] else prev[6]) + c2
#         cur[7] = (prev[2] if prev[2] < prev[7] else prev[7]) + c0
#         cur[8] = (prev[2] if prev[2] < prev[8] else prev[8]) + c1

#     if i >= 3:
#         cur[9]  = (prev[3] if prev[3] < prev[9] else prev[9]) + c2
#         cur[10] = (prev[4] if prev[4] < prev[10] else prev[10]) + c1
#         cur[11] = (prev[5] if prev[5] < prev[11] else prev[11]) + c2
#         cur[12] = (prev[6] if prev[6] < prev[12] else prev[12]) + c0
#         cur[13] = (prev[7] if prev[7] < prev[13] else prev[13]) + c1
#         cur[14] = (prev[8] if prev[8] < prev[14] else prev[14]) + c0

#     prev, cur = cur, prev  # 滚动数组

# print(min(prev))

import sys
def calculate_min_transformation_cost(n, original_string, transformation_costs):
    """
    Calculates the minimum cost to transform a string into a sequence
    of three distinct character types (0, 1, 2) by partitioning it into
    three contiguous segments.

    Each character in the original string has an associated cost to change it.
    The algorithm considers all 6 permutations of (0, 1, 2) for the target
    character types of the three segments.

    Args:
        n (int): The length of the string.
        original_string (str): The input string 'p'.
        transformation_costs (list of int): The costs 't' associated with
                                            changing each character.

    Returns:
        int: The minimum total transformation cost.
    """
    # 1. Preprocessing: Calculate prefix sums for the cost of converting
    # a prefix of the string to all '0's, all '1's, or all '2's.
    # prefix_cost_to_zeros[i] will store the cost to make string[0...i-1] all '0's.
    prefix_cost_to_zeros = [0] * (n + 1)
    prefix_cost_to_ones = [0] * (n + 1)
    prefix_cost_to_twos = [0] * (n + 1)

    for i in range(1, n + 1):
        current_char = original_string[i - 1]
        cost_to_change_char = transformation_costs[i - 1]

        # Cost to convert current prefix to '0's
        prefix_cost_to_zeros[i] = prefix_cost_to_zeros[i - 1] + (
            0 if current_char == "0" else cost_to_change_char
        )
        # Cost to convert current prefix to '1's
        prefix_cost_to_ones[i] = prefix_cost_to_ones[i - 1] + (
            0 if current_char == "1" else cost_to_change_char
        )
        # Cost to convert current prefix to '2's
        prefix_cost_to_twos[i] = prefix_cost_to_twos[i - 1] + (
            0 if current_char == "2" else cost_to_change_char
        )

    # Store references to these prefix sum arrays for easier access by index (0, 1, 2)
    # This allows dynamic access based on the permutation order.
    prefix_arrays_map = (prefix_cost_to_zeros, prefix_cost_to_ones, prefix_cost_to_twos)

    min_overall_cost = float("inf")

    # 2. Iterate through all 6 permutations of (0, 1, 2) for the three segments.
    # Each 'order' represents (target_char_for_segment_1, target_char_for_segment_2, target_char_for_segment_3)
    # The values 0, 1, 2 here are just indices to prefix_arrays_map.
    for order_indices in [
        (0, 1, 2),
        (0, 2, 1),
        (1, 0, 2),
        (1, 2, 0),
        (2, 0, 1),
        (2, 1, 0),
    ]:

        # Get the specific prefix sum arrays based on the current permutation order
        target_prefix_array_A = prefix_arrays_map[
            order_indices[0]
        ]  # For the first segment type
        target_prefix_array_B = prefix_arrays_map[
            order_indices[1]
        ]  # For the second segment type
        target_prefix_array_C = prefix_arrays_map[
            order_indices[2]
        ]  # For the third segment type

        # --- Dynamic Programming with Two Passes ---
        # This part effectively finds optimal cut points for the segments.
        # It's based on minimizing (Cost_A[i] - Cost_B[i]) + (Cost_B[j] - Cost_C[j]) + Cost_C[n]
        # where i is the end of segment 1, and j is the end of segment 2.

        # Pass 1: Calculate min_val_A_minus_B[j] = min_{0 <= i <= j} (target_prefix_array_A[i] - target_prefix_array_B[i])
        # This finds the minimum cost for the first part (first segment cost minus the second segment's prefix cost)
        # up to index j.
        min_cost_diff_A_minus_B = float("inf")
        min_val_A_minus_B_at_j = [0] * (n + 1)
        for j in range(n + 1):
            current_diff = target_prefix_array_A[j] - target_prefix_array_B[j]
            if current_diff < min_cost_diff_A_minus_B:
                min_cost_diff_A_minus_B = current_diff
            min_val_A_minus_B_at_j[j] = min_cost_diff_A_minus_B

        # Pass 2: Enumerate the second cut point 'j' (end of the second segment).
        # Calculate the total cost for this permutation:
        # min_{0 <= j <= n} ( min_{0 <= i <= j} (Cost_A[i] - Cost_B[i]) + (Cost_B[j] - Cost_C[j]) ) + Cost_C[n]
        # This finds the overall minimum cost for the first two segments combined (up to j),
        # plus the cost of the third segment from j to n.
        min_cost_for_first_two_segments = float("inf")
        for j in range(n + 1):
            cost_up_to_j = min_val_A_minus_B_at_j[j] + (
                target_prefix_array_B[j] - target_prefix_array_C[j]
            )
            if cost_up_to_j < min_cost_for_first_two_segments:
                min_cost_for_first_two_segments = cost_up_to_j

        # Add the cost of the third segment (from index j to the end of the string 'n').
        # This is essentially Cost_C[n] minus the part already covered by (prefixB[j] - prefixC[j])
        # The derivation `min_pre[j] + (prefixB[j]-prefixC[j]) + prefixC[n]` correctly sums
        # `(prefixA[i] - prefixB[i]) + (prefixB[j] - prefixC[j]) + prefixC[n]` over chosen i,j.
        current_permutation_total_cost = (
            min_cost_for_first_two_segments + target_prefix_array_C[n]
        )

        # Update the overall minimum cost found across all permutations
        min_overall_cost = min(min_overall_cost, current_permutation_total_cost)

    return min_overall_cost


### Main Program Execution


def main():
    """
    Reads input for the string length, the string itself, and transformation costs,
    then calculates and prints the minimum transformation cost.
    Handles basic input errors.
    """
    try:
        n_str = input().strip()
        n = int(n_str)
        if n < 0:
            print("Error: String length (n) cannot be negative.", file=sys.stderr)
            return

        original_string = input().strip()
        if len(original_string) != n:
            print(
                f"Warning: Expected string length {n}, but got {len(original_string)}. Using provided string length.",
                file=sys.stderr,
            )
            n = len(original_string)  # Adjust n to actual string length if mismatch

        transformation_costs_str = input().strip()
        transformation_costs = list(map(int, transformation_costs_str.split()))

        if len(transformation_costs) != n:
            print(
                f"Error: Expected {n} costs, but got {len(transformation_costs)}.",
                file=sys.stderr,
            )
            return

        # Ensure all costs are non-negative
        if any(cost < 0 for cost in transformation_costs):
            print("Error: Transformation costs cannot be negative.", file=sys.stderr)
            return

        # Calculate and print the result
        result = calculate_min_transformation_cost(
            n, original_string, transformation_costs
        )
        print(result)

    except ValueError:
        # print(
        #     "Invalid input. Please ensure all inputs are correct integers/string.",
        #     file=sys.stderr,
        # )
        pass
    except EOFError:
        # Handles cases where input stream ends unexpectedly
        # print("\nEnd of input received. Exiting.", file=sys.stderr)
        pass
    except Exception as e:
        # Catch any other unexpected errors
        # print(f"An unexpected error occurred: {e}", file=sys.stderr)
        pass


if __name__ == "__main__":
    main()
