---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.24 PartyIdentification117", "7.1.20.24.1 AnyBIC <AnyBIC>"]
file_pages: [472]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.24.1 AnyBIC <AnyBIC>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 472 to 472.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 472

```text
7.1.20.24.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 662
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
7.1.20.24.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification36" on
page 279 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 279
   Issuer <Issr> [1..1] Text 279
   SchemeName <SchmeNm> [0..1] Text 279
7.1.20.24.3  NameAndAddress <NmAndAdr>
Presence: [0..1]
Definition: Identification of a party with its name and address in free text.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 472 February 2025
```

