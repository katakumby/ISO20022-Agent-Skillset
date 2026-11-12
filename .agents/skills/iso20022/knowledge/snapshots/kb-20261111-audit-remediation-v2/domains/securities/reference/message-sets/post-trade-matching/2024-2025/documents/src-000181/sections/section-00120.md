---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "5.4 Message Building Blocks", "5.4.5 ConfirmationParties <ConfPties>"]
file_pages: [154]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.030.001.03"]
---

# 5.4.5 ConfirmationParties <ConfPties>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 154 to 154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 154

```text
5.4.5 ConfirmationParties <ConfPties>
Presence: [0..*]
Definition: Parties involved in the confirmation of the details of a trade.
ConfirmationParties <ConfPties> contains the following ConfirmationParties8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AffirmingParty <AffrmgPty> [1..1] ± 154
   Buyer <Buyr> [0..1] ± 155
   Borrower <Brrwr> [0..1] ± 156
   Seller <Sellr> [0..1] ± 157
   Lender <Lndr> [0..1] ± 158
   TradeBeneficiaryParty <TradBnfcryPty> [0..1] ± 159
5.4.5.1  AffirmingParty <AffrmgPty>
Presence: [1..1]
Definition: Party (buyer or seller) that positively affirms the details of a previously agreed security trade
confirmation.
Approved by the Securities SEG on 13 February 2025 setr.030.001.03
SecuritiesTradeConfirmationResponseV03
Post Trade Matching - Maintenance 2024 - 2025 154 February 2025
```

