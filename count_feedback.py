def count_feedbacks_by_user(feedback_data, target_name):
    """
    Counts the number of feedback entries by a specific user.

    Args:
        feedback_data (list or dict): Data containing feedback entries.
        target_name (str): The name of the user to count feedback for (case-insensitive).

    Returns:
        int: The number of feedback entries by the user.
    """
    count = 0
    target_name_lower = target_name.lower()

    if isinstance(feedback_data, list):
        for item in feedback_data:
            if isinstance(item, dict) and "name" in item and isinstance(item["name"], str) and item["name"].lower() == target_name_lower:
                count += 1
    elif isinstance(feedback_data, dict):
        for item in feedback_data.values():
            if isinstance(item, dict) and "name" in item and isinstance(item["name"], str) and item["name"].lower() == target_name_lower:
                count += 1
    return count

def main():
    """Provides examples of using count_feedbacks_by_user."""
    feedback_list = [
        {"name": "Alice Smith", "comment": "Great product!"},
        {"name": "Bob Johnson", "comment": "Needs improvement."},
        {"name": "Alice Smith", "comment": "Excellent service."},
    ]
    user_name = "Alice Smith"
    feedback_count = count_feedbacks_by_user(feedback_list, user_name)
    print(f"User '{user_name}' provided {feedback_count} feedback(s) in the list.")

    feedback_dict = {
        "feedback_1": {"name": "Alice Smith", "comment": "Great product!"},
        "feedback_2": {"name": "Bob Johnson", "comment": "Needs improvement."},
        "feedback_3": {"name": "Alice Smith", "comment": "Excellent service."},
    }
    user_name = "Alice Smith"
    feedback_count = count_feedbacks_by_user(feedback_dict, user_name)
    print(f"\nUser '{user_name}' provided {feedback_count} feedback(s) in the dictionary.")

if __name__ == "__main__":
    main()
