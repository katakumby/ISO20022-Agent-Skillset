---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.11 Miscellaneous", "6.1.11.2 Authorisation1Choice", "6.1.11.2.1 Code <Cd>"]
file_pages: [553]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.11.2.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 553 to 553.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 553

```text
6.1.11.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the authorisation, in a coded form.
Datatype: "Authorisation1Code" on page 588
CodeName Name Definition
AUTH PreAuthorisedFile Indicates a file has been pre authorised
or approved within the originating
customer environment and no further
approval is required.
FDET FileLevelAuthorisationDetails Indicates that a file requires additional
file level approval, with the ability to view
both the payment information block and
supporting customer credit transaction
detail.
FSUM FileLevelAuthorisationSummary Indicates that a file requires additional
file level approval, with the ability to view
only the payment information block level
information.
ILEV InstructionLevelAuthorisation Indicates that a file requires all customer
transactions to be authorised or
approved.
6.1.11.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the authorisation, in a free text form.
Datatype: "Max128Text" on page 608
6.1.11.3  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 553
   Envelope <Envlp> [1..1] (External Schema) 554
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
6.1.11.3.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Definition: Unambiguous reference to the location where the supplementary data must be inserted in
the message instance.
In the case of XML, this is expressed by a valid XPath.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 553 March 2026
```

