---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 Message Items Types", "11.2 Message Datatypes", "11.2.1 CodeSet", "11.2.1.9 NamePrefix2Code"]
file_pages: [183]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.2.1.9 NamePrefix2Code

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 183 to 183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 183

```text
11.2.1.9  NamePrefix2Code
Definition: Specifies the terms used to formally address a person.
Type: CodeSet
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
11.2.1.10  PreferredContactMethod2Code
Definition: Preferred method used to reach the individual contact within an organisation.
Type: CodeSet
CodeName Name Definition
MAIL Email Preferred method used to reach the
contact is per email.
FAXX Fax Preferred method used to reach the
contact is per fax.
LETT Letter Preferred method used to reach the
contact is per letter.
CELL MobileOrCellPhone Preferred method used to reach the
contact is per mobile or cell phone.
ONLI Online Preferred method used to reach the
contact is online.
PHON Phone Preferred method used to reach the
contact is per phone.
11.2.1.11  RequestType1Code
Definition: Specifies the request used to further detail the type of information that will be queried.
Type: CodeSet
CodeName Name Definition
RT01 ReleasePending Type is a request to release the pending
transactions.
RT02 HoldNormal Type is a request to hold normal
transactions.
RT03 Cancellation Type is a request to cancellation a
transaction.
RT04 ReSequence Type is a request to change the
sequence of the transactions.
RT05 ReleaseSuspicious Type is a request to release the
suspicious transactions.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
183 March 2024
```

