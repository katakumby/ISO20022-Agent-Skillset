---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.20 CashParties33", "7.1.20.20.4 CreditorAgent <CdtrAgt>"]
file_pages: [458]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.20.4 CreditorAgent <CdtrAgt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 458 to 458.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 458

```text
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in a
structured field.
7.1.20.20.4  CreditorAgent <CdtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the creditor.
CreditorAgent <CdtrAgt> contains the following PartyIdentificationAndAccount148 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 458
   AlternateIdentification <AltrnId> [0..1] ± 459
   CashAccount <CshAcct> [0..1] ± 459
   ChargesAccount <ChrgsAcct> [0..1] ± 460
   CommissionAccount <ComssnAcct> [0..1] ± 460
   TaxAccount <TaxAcct> [0..1] ± 460
   AdditionalInformation <AddtlInf> [0..1] ± C4 460
7.1.20.20.4.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 458 February 2025
```

