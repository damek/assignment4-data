# Problem (mask_pii): 3 points

Main code file: [mask_pii.py](../mask_pii.py)

## Question 1

Write a function to mask out emails. Your function will take a string as input, and replace all
instances of email addresses with the string "|||EMAIL_ADDRESS|||". To detect email addresses,
you can look up regular expressions that do this reliably.
Deliverable: A function that replaces all email addresses in a given string with the string
"|||EMAIL_ADDRESS|||", returning a pair containing both the new string and the number of
instances that were masked. Implement the adapter [run_mask_emails] and make sure it passes
all tests in uv run pytest -k test_mask_emails.

**Answer:** Passed

How to run: 
```bash
uv run pytest -k test_mask_emails
```

## Question 2

Write a function to mask out phone numbers. Your function will take a string as input, and replace
all instances of phone numbers with the string "|||PHONE_NUMBER|||". Doing this reliably can
be extremely challenging, as phone numbers might be written in an extremely diverse set of
5
formats, but you should try to capture at least the most common phone number formats used in
the United States, and be robust to minor syntactic deviations.
Deliverable: A function that replaces phone numbers in a given string with the string
"|||PHONE_NUMBER|||", returning a pair containing both the new string and the number of
instances that were masked. Implement the adapter [run_mask_phone_numbers] and make sure
it passes uv run pytest -k test_mask_phones.

**Answer:** Passed

How to run: 
```bash
uv run pytest -k test_mask_phones
```

## Question 3

Write a function to mask out IP addresses. For this problem, it is enough to focus on IPv4
addresses (4 numbers up to 255 separated by points). Your function will take a string as input,
and replace all instances of IP addresses with the string "|||IP_ADDRESS|||".
Deliverable: A function that replaces IPv4 addresses in a given string with the string
"|||IP_ADDRESS|||", returning a pair containing both the new string and the number of in-
stances that were masked. Implement the adapter [run_mask_ips] and make sure it passes
uv run pytest -k test_mask_ips.

**Answer:** Passed

How to run: 
```bash
uv run pytest -k test_mask_ips
```

## Question 4

What problems do you think might arise downstream in a language model when these filters are
naïvely applied on the training set? How might you mitigate these issues?
Deliverable: A 2-5 sentence response.

**Answer:** When a user inputs data into a language model, they will not mask emails. So essentially need to pre-convert their inputs to mask emails. I think that posses a problem for disambiguation later on: which email address did |||EMAIL_ADDRESS||| refer to? Same issue can happen with phone numbers and ips, unfortunately. The word for this is of course distribution shift.

## Question 5

Run your PII masking functions on text extracted from the WARC files (via your previously-
implemented text extraction function). Look through 20 random examples where a replacement
was made; give some examples of false positives and false negatives.
Deliverable: A 2-5 sentence response.

False positives:
```
http://naistekas.delfi.ee/joululeht/joulud/miks-mehed-ei-moista-et-45aastane-naine-on-palju-parem-kui-25ne.d?id=|||PHONE_NUMBER||| Vasta Tsiteeri```
```

False Negatives: 
```
 البريد الإلكتروني الخاص بك: معلومات@w88.com
```