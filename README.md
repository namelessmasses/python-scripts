# M.A.S.K - Mail Address Safe Keeper

## Address Creation

- Created for a specific domain address
  - user@example.com allows communication with user@example.com and only user@example.com.
  - <regex> allows communication with any address matching the provided regular expression.
- Valid from a specific date to an optional expiration date.
- Created address is UUIDv5 of the provided parameters.
  - from_address: the address or regex
  - to_address: the created address
  - valid_from: the start date
  - valid_to: the optional expiration date
    - if none provided uses the maximum date supported by python datetime library.
- Forwarded to a user provided email address.

## Receiving Mail

1. Extract To address from the email.
2. Lookup the to_address in the database.
3. If found, check if the current date is within the valid_from and valid_to range
4. If valid, check if the from_address is a regex or specific address
   - If regex, match the From address against the regex.
   - If specific address, compare the From address with the from_address.
5. If all checks pass, then
   1. Record,
      1. message-id
      1. From:
   1. Forward the email to the user provided email address.

## Replying to a received Mail

* What fields get forwarded in a reply?

## Sending Mail

1. Extract the To address from the email.
2. Lookup the to_address in the database.
3. If found, check if the current date is within the valid_from and valid_to range
4. 