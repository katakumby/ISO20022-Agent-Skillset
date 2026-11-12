---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.2 CodeSet", "6.2.2.48 FloorLimitType1Code"]
file_pages: [901]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.2.48 FloorLimitType1Code

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 901 to 901.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 901

```text
6.2.2.48  FloorLimitType1Code
Definition: Indicates whether the floor limit applies to credit, to debit or to both credit and debit entries.
Type: CodeSet
CodeName Name Definition
CRED Credit Floor limit applies to credit entries.
DEBT Debit Floor limit applies to debit entries.
BOTH Both Floor limit applies to both credit and
debit entries.
6.2.2.49  InterestType1Code
Definition: Indicates which type of interest is applied to a balance left on an account.
Type: CodeSet
CodeName Name Definition
INDY IntraDay During or within a business day.
OVRN OverNight Period of time between the end of a
business day and the start of the next
business day (usually the day after).
6.2.2.50  ISO2ALanguageCode
Definition: Identification of the language name according to the ISO 639-1 codes. The type is validated
by the list of values coded with two alphabetic characters, defined in the standard.
Type: CodeSet
Format
pattern [a-z]{2,2}
6.2.2.51  NamePrefix2Code
Definition: Specifies the terms used to formally address a person.
Type: CodeSet
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
6.2.2.52  OnLineCapability1Code
Definition: On-line and off-line capabilities of the POI (Point Of Interaction).
Type: CodeSet
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
901 March 2026
```

