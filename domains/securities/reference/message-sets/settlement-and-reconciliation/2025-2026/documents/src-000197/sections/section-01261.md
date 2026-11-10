---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.20 Price", "35.1.20.10 PriceInformation29", "35.1.20.10.5 QuotationDate <QtnDt>"]
file_pages: [1718]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.20.10.5 QuotationDate <QtnDt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1718 to 1718.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1718

```text
SourceOfPrice <SrcOfPric> contains the following elements (see "MarketIdentification98" on
page 1523 for details)
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
35.1.20.10.5  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date on which the price is obtained. With an investment fund, this is as stated in the
prospectus.
QuotationDate <QtnDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.21 Quantity
35.1.21.1  QuantityAndAccount114
Definition: Details on a quantity, account and other related information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementQuantity <SttlmQty> [1..1] ± C12 1719
   DenominationChoice <DnmtnChc> [0..1] Text 1719
   CashAccount <CshAcct> [0..1] ± 1719
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1720
   SafekeepingPlace <SfkpgPlc> [0..1] ± C33 1720
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1718 March 2026
```

