def count_valid_emails(emails):
    if not emails:
        return 0

    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue

        email = email.strip()

        if "@" not in email:
            continue

        local, _, domain = email.partition("@")

        if local and domain and "." in domain:
            count += 1

    return count
