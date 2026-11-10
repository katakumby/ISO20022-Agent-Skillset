---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.1 Account", "66.1.1.2 ConfirmationType1Choice", "66.1.1.2.1 Code <Cd>"]
file_pages: [4324]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.1.2.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4324 to 4324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4324

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4324
Or}   Proprietary <Prtry> [1..1] ± 4324
66.1.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Confirmation type expressed as a code.
Datatype: "AccountManagementType2Code" on page 5271
CodeName Name Definition
ACCO AccountOpening Refers to an account opening instruction
message.
ACCM AccountModification Refers to an account modification
instruction message.
GACC GetAccountDetails Refers to a get account details message.
66.1.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Confirmation type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.1.3  AccountOpeningType1Choice
Definition: Choice of formats for the account opening type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4324
Or}   Proprietary <Prtry> [1..1] ± 4325
66.1.1.3.1  Code <Cd>
Presence: [1..1]
Definition: Type of account opening instruction expressed as a code.
Datatype: "AccountOpeningType1Code" on page 5272
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4324 May 2026
```

