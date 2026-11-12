---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 semt.015.001.10 IntraPositionMovementConfirmationV10", "6.4 Message Building Blocks", "6.4.9 IntraPositionDetails <IntraPosDtls>", "6.4.9.2 SecuritiesSubBalanceIdentification <SctiesSubBalId>"]
file_pages: [174]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.015.001.10"]
---

# 6.4.9.2 SecuritiesSubBalanceIdentification <SctiesSubBalId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 174 to 174.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 174

```text
SettledQuantity <SttldQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
6.4.9.2  SecuritiesSubBalanceIdentification <SctiesSubBalId>
Presence: [0..1]
Definition: Number identifying a Securities Sub balance Type for example restriction identification.
SecuritiesSubBalanceIdentification <SctiesSubBalId> contains the following elements (see
"GenericIdentification37" on page 1498 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1498
   Issuer <Issr> [0..1] Text 1498
6.4.9.3  CollateralMonitorAmount <CollMntrAmt>
Presence: [0..1]
Definition: Value of the collateral available for the delivery settlement process at the account level.
CollateralMonitorAmount <CollMntrAmt> contains the following elements (see
"AmountAndDirection44" on page 1375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
6.4.9.4  PreviouslySettledQuantity <PrevslySttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument previously settled.
Impacted by: C12 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 174 March 2026
```

