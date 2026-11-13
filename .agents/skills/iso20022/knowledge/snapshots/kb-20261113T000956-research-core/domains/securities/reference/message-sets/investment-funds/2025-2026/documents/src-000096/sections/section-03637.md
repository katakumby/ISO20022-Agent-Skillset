---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification"]
file_pages: [4887]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29 Organisation Identification

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4887 to 4887.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4887

```text
NetCashForecast <NetCshFcst> contains the following elements (see "NetCashForecast4" on
page 4413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [1..1] Date 4413
   NetAmount <NetAmt> [0..1] Amount C2, C10 4414
   NetUnitsNumber <NetUnitsNb> [0..1] ± 4414
   FlowDirection <FlowDrctn> [1..1] CodeSet 4414
   AdditionalBalance <AddtlBal> [0..1] ± 4414
Constraints
• AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list (AdditionalBalance/
TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders, AdditionalBalance/
TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders) must be present.
On Condition
    /AdditionalBalance is present
Following Must be True
    /AdditionalBalance/TotalUnitsFromUnitOrders Must be present
 Or    /AdditionalBalance/TotalUnitsFromCashOrders Must be present
 Or    /AdditionalBalance/TotalCashFromUnitOrders Must be present
 Or    /AdditionalBalance/TotalCashFromCashOrders Must be present
66.1.29 Organisation Identification
66.1.29.1  PartyIdentification2Choice
Definition: Choice of identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4887
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4888
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4888
66.1.29.1.1  BICOrBEI <BICOrBEI>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C5 "AnyBIC"
Datatype: "AnyBICIdentifier" on page 5389
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4887 May 2026
```

