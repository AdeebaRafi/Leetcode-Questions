import math

def cross_product(origin_point, first_point, second_point):
    return (first_point[0] - origin_point[0]) * (second_point[1] - origin_point[1]) - (first_point[1] - origin_point[1]) * (second_point[0] - origin_point[0])

def compute_convex_hull(coordinate_points):
    coordinate_points = sorted(coordinate_points)
    lower_hull = []
    for current_point in coordinate_points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], current_point) <= 0:
            lower_hull.pop()
        lower_hull.append(current_point)
    upper_hull = []
    for current_point in reversed(coordinate_points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], current_point) <= 0:
            upper_hull.pop()
        upper_hull.append(current_point)
    return lower_hull[:-1] + upper_hull[:-1]

def calculate_distance(point_one, point_two):
    return math.hypot(point_one[0] - point_two[0], point_one[1] - point_two[1])

def compute_dot_product(vector_one, vector_two):
    return vector_one[0] * vector_two[0] + vector_one[1] * vector_two[1]

def find_minimum_area_rectangle(convex_hull_points):
    number_of_points = len(convex_hull_points)
    if number_of_points == 1:
        return 0.0
    if number_of_points == 2:
        return calculate_distance(convex_hull_points[0], convex_hull_points[1]) * 0.0

    minimum_area = float('inf')
    farthest_point_index = 1

    for starting_index in range(number_of_points):
        next_index = (starting_index + 1) % number_of_points
        edge_vector = (convex_hull_points[next_index][0] - convex_hull_points[starting_index][0], convex_hull_points[next_index][1] - convex_hull_points[starting_index][1])
        edge_length = math.hypot(edge_vector[0], edge_vector[1])
        edge_vector = (edge_vector[0] / edge_length, edge_vector[1] / edge_length)  # normalize the edge vector

        # Find farthest point
        while True:
            next_farthest_index = (farthest_point_index + 1) % number_of_points
            if abs(cross_product(convex_hull_points[starting_index], convex_hull_points[next_index], convex_hull_points[next_farthest_index])) > abs(cross_product(convex_hull_points[starting_index], convex_hull_points[next_index], convex_hull_points[farthest_point_index])):
                farthest_point_index = next_farthest_index
            else:
                break

        maximum_projection = -float('inf')
        minimum_projection = float('inf')
        maximum_width = 0

        for test_point in convex_hull_points:
            projection_length = compute_dot_product((test_point[0] - convex_hull_points[starting_index][0], test_point[1] - convex_hull_points[starting_index][1]), edge_vector)
            maximum_projection = max(maximum_projection, projection_length)
            minimum_projection = min(minimum_projection, projection_length)
            width = abs(cross_product(convex_hull_points[starting_index], convex_hull_points[next_index], test_point)) / edge_length
            maximum_width = max(maximum_width, width)

        current_area = (maximum_projection - minimum_projection) * maximum_width
        minimum_area = min(minimum_area, current_area)

    return minimum_area

def solve_problem():
    total_test_cases = int(input())
    for _ in range(total_test_cases):
        number_of_coordinates = int(input())
        coordinate_list = []
        for _ in range(number_of_coordinates):
            coordinate_x, coordinate_y = map(float, input().split())
            coordinate_list.append((coordinate_x, coordinate_y))
        convex_hull_result = compute_convex_hull(coordinate_list)
        rectangle_area = find_minimum_area_rectangle(convex_hull_result)
        print(f"{rectangle_area:.10f}")

solve_problem()
