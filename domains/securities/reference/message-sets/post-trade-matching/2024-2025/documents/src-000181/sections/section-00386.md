---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.20 CashParties33", "7.1.20.20.2 DebtorAgent <DbtrAgt>"]
file_pages: [452]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.20.2 DebtorAgent <DbtrAgt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 452 to 452.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 452

```text
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in a
structured field.
7.1.20.20.2  DebtorAgent <DbtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the debtor.
DebtorAgent <DbtrAgt> contains the following PartyIdentificationAndAccount148 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 452
   AlternateIdentification <AltrnId> [0..1] ± 453
   CashAccount <CshAcct> [0..1] ± 453
   ChargesAccount <ChrgsAcct> [0..1] ± 454
   CommissionAccount <ComssnAcct> [0..1] ± 454
   TaxAccount <TaxAcct> [0..1] ± 454
   AdditionalInformation <AddtlInf> [0..1] ± C4 454
7.1.20.20.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 452 February 2025
```

