---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.15 Market", "35.1.15.1 MarketIdentification98", "35.1.15.1.1 Identification <Id>"]
file_pages: [1524]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.15.1.1 Identification <Id>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1524 to 1524.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1524

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 1524
   Type <Tp> [1..1]  1524
{Or     Code <Cd> [1..1] CodeSet 1524
Or}     Proprietary <Prtry> [1..1] ± 1525
Constraints
• SmartContractAutomatedPricingRule
When Type/Code does not equal SmartContractAutomatedPricingSystem (SCAS) then Identification/
Description length must be maximum 35 characters.
35.1.15.1.1  Identification <Id>
Presence: [0..1]
Definition: Code allocated to places of trade (stock exchanges), to regulated markets (for example,
Electronic Trading Platforms - ECN), and to unregulated markets (for example, Automated Trading
Systems - ATS), as sources of prices and related information, in order to facilitate automated
processing.
Identification <Id> contains one of the following elements (see "MarketIdentification5Choice" on
page 1529 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 1529
Or}   Description <Desc> [1..1] Text 1529
35.1.15.1.2  Type <Tp>
Presence: [1..1]
Definition: Nature of a market in which transactions take place.
Type <Tp> contains one of the following MarketType19Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1524
Or}   Proprietary <Prtry> [1..1] ± 1525
35.1.15.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Market type expressed as an ISO 20022 code.
Datatype: "MarketType9Code" on page 2086
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1524 March 2026
```

