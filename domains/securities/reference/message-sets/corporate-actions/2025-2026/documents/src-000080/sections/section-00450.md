---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.15 RateDetails <RateDtls>", "8.4.12.10.15.1 AdditionalQuantityForSubscribedResultantSecurities <AddtlQtyForSbcbdRsltntScties>"]
file_pages: [604]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.15.1 AdditionalQuantityForSubscribedResultantSecurities <AddtlQtyForSbcbdRsltntScties>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 604 to 604.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 604

```text
RateDetails <RateDtls> contains the following CorporateActionRate125 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalQuantityForSubscribedResultantSecurities
<AddtlQtyForSbcbdRsltntScties>
[0..1] ± 604
   AdditionalQuantityForExistingSecurities
<AddtlQtyForExstgScties>
[0..1] ± 604
   NewToOld <NewToOd> [0..1] ± 605
   ChargesFees <ChrgsFees> [0..1] ± 605
   FiscalStamp <FsclStmp> [0..1] Rate 606
   ApplicableRate <AplblRate> [0..1] Rate 606
   TaxCreditRate <TaxCdtRate> [0..1] ± 606
   FinancialTransactionTaxRate <FinTxTaxRate> [0..1] Rate 606
   WithholdingTaxRate <WhldgTaxRate> [0..*] ± 606
   SecondLevelTax <ScndLvlTax> [0..*] ± 607
8.4.12.10.15.1  AdditionalQuantityForSubscribedResultantSecurities <AddtlQtyForSbcbdRsltntScties>
Presence: [0..1]
Definition: Quantity of additional intermediate securities/new equities awarded for a given quantity of
securities derived from subscription.
AdditionalQuantityForSubscribedResultantSecurities <AddtlQtyForSbcbdRsltntScties> contains
one of the following elements (see "RatioFormat20Choice" on page 1099 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityToQuantity <QtyToQty> [1..1] ± 1099
Or}   AmountToAmount <AmtToAmt> [1..1]  1099
     Amount1 <Amt1> [1..1] Amount C1 1099
     Amount2 <Amt2> [1..1] Amount C1 1100
8.4.12.10.15.2  AdditionalQuantityForExistingSecurities <AddtlQtyForExstgScties>
Presence: [0..1]
Definition: Quantity of additional securities for a given quantity of underlying securities where underlying
securities are not exchanged or debited, for example, 1 for 1: 1 new equity credited for every 1
underlying equity = 2 resulting equities.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 604 February 2026
```

