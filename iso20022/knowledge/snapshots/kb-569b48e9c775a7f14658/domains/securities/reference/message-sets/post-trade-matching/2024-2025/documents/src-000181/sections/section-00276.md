---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.40 SecuritiesLendingType2Choice", "7.1.19.40.2 Proprietary <Prtry>"]
file_pages: [334]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.40.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 334 to 334.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 334

```text
Definition: Securities lending type expressed as an ISO 20022 code.
Datatype: "SecuritiesLendingType1Code" on page 645
CodeName Name Definition
NWRG NewRegistration Securities lending contract is new and
registered.
RENW RollOverRenewal Securities lending contract is renewed.
CABK CallBack Securities lending contract is called
back.
7.1.19.40.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities lending type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.41  SettlementStandingInstructionDatabase4Choice
Definition: Choice of format for the standing settlement instruction information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 334
Or}   Proprietary <Prtry> [1..1] ± 335
7.1.19.41.1  Code <Cd>
Presence: [1..1]
Definition: Settlement standing instruction database expressed as an ISO 20022 code.
Datatype: "SettlementStandingInstructionDatabase1Code" on page 646
CodeName Name Definition
INTE InternalDatabase The settlement standing instruction
database to be used is the receiver's
internal database.
BRKR BrokerDatabase The settlement standing instruction
database to be used is the broker's
database.
VEND VendorDatabase The settlement standing instruction
database to be used is the database of
the vendor.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 334 February 2025
```

