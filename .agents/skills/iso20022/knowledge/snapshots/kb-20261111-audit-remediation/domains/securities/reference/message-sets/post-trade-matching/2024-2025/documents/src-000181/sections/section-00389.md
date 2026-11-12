---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.20 CashParties33", "7.1.20.20.3 Creditor <Cdtr>"]
file_pages: [455]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.20.3 Creditor <Cdtr>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 455 to 455.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 455

```text
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in a
structured field.
7.1.20.20.3  Creditor <Cdtr>
Presence: [0..1]
Definition: Party to which an amount of money is due.
Creditor <Cdtr> contains the following PartyIdentificationAndAccount148 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 455
   AlternateIdentification <AltrnId> [0..1] ± 456
   CashAccount <CshAcct> [0..1] ± 456
   ChargesAccount <ChrgsAcct> [0..1] ± 457
   CommissionAccount <ComssnAcct> [0..1] ± 457
   TaxAccount <TaxAcct> [0..1] ± 457
   AdditionalInformation <AddtlInf> [0..1] ± C4 457
7.1.20.20.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 455 February 2025
```

