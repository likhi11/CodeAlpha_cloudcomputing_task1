def is_duplicate(new_entry, existing_entries):
    """
    Checks if the new entry already exists in the database.
    """
    for doc in existing_entries:
        if doc.to_dict() == new_entry:
            return True
    return False