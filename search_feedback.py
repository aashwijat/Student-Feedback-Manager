def search_feedback_by_name(feedback_data, target_name):
    """
    Searches for user feedback entries by name (case-insensitive).

    Args:
        feedback_data (list or dict):  Data structure containing feedback.
        target_name (str): The name to search for.

    Returns:
        list: Matching feedback entries.
    """
    results = []
    target_name_lower = target_name.lower()

    if isinstance(feedback_data, list):
        for item in feedback_data:
            if isinstance(item, dict) and "name" in item and isinstance(item["name"], str) and item["name"].lower() == target_name_lower:
                results.append(item)
    elif isinstance(feedback_data, dict):
        for item in feedback_data.values():
             if isinstance(item, dict) and "name" in item and isinstance(item["name"], str) and item["name"].lower() == target_name_lower:
                results.append(item)
    else:
        return [] # Returns empty list if the input is not the expected type

    return results

def main():
    # Example usage:
    feedback_list = [
        {"name": "Alice Smith", "comment": "Great product!"},
        {"name": "Bob Johnson", "comment": "Needs improvement."},
        {"name": "Alice Smith", "comment": "Excellent service."},
    ]

    search_name = "Alice Smith"
    results = search_feedback_by_name(feedback_list, search_name)
    print(f"Feedback from {search_name}: {results}")

    feedback_dict = {
        "feedback_1": {"name": "Alice Smith", "comment": "Great product!"},
        "feedback_2": {"name": "Bob Johnson", "comment": "Needs improvement."},
        "feedback_3": {"name": "Alice Smith", "comment": "Excellent service."},
    }
    search_name = "Alice Smith"
    results = search_feedback_by_name(feedback_dict, search_name)
    print(f"Feedback from {search_name} (dict): {results}")

if __name__ == "__main__":
    main()
