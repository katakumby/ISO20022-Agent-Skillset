---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.15 Market", "35.1.15.1 MarketIdentification98", "35.1.15.1.2 Type <Tp>", "35.1.15.1.2.2 Proprietary <Prtry>"]
file_pages: [1525]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.15.1.2.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1525 to 1525.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1525

```text
CodeName Name Definition
FUND Fund The place is a fund (transfer agent, fund
itself, etc.).
LMAR LocalMarket The place is a local market.
THEO Theoretical The place is theoretical.
VEND Vendor The place is a vendor.
SCAS SmartContractAutomatedPricingSystem Source of price quotation is a smart
contract automated pricing system.
35.1.15.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.15.2  MarketClientSide6Choice
Definition: Choice of format for the market/client side information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1525
Or}   Proprietary <Prtry> [1..1] ± 1525
35.1.15.2.1  Code <Cd>
Presence: [1..1]
Definition: Market side or a client side information expressed as an ISO 20022 code.
Datatype: "MarketClientSide1Code" on page 2086
CodeName Name Definition
CLNT ClientSide Instruction is for a client side transaction.
MAKT MarketSide Instruction is for a market side
transaction.
35.1.15.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market side or a client side information expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1525 March 2026
```

