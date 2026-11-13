---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.17 RateDetails <RateDtls>"]
file_pages: [191]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.17 RateDetails <RateDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 191 to 191.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 191

```text
LastTradingDate <LastTradgDt> contains one of the following elements (see "DateFormat30Choice"
on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.11.24.17  RateDetails <RateDtls>
Presence: [0..1]
Definition: Provides information about the rates related to securities movement.
RateDetails <RateDtls> contains the following CorporateActionRate128 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalQuantityForSubscribedResultantSecurities
<AddtlQtyForSbcbdRsltntScties>
[0..1] ± 191
   AdditionalQuantityForExistingSecurities
<AddtlQtyForExstgScties>
[0..1] ± 192
   NewToOld <NewToOd> [0..1] ± 192
   TransformationRate <TrfrmatnRate> [0..1] Rate 193
   ChargesFees <ChrgsFees> [0..1] ± 193
   FiscalStamp <FsclStmp> [0..1] ± 193
   ApplicableRate <AplblRate> [0..1] ± 194
   TaxCreditRate <TaxCdtRate> [0..1] ± 194
   FinancialTransactionTaxRate <FinTxTaxRate> [0..1] ± 194
   WithholdingTaxRate <WhldgTaxRate> [0..*] ± 194
   SecondLevelTax <ScndLvlTax> [0..*] ± 195
3.4.11.24.17.1  AdditionalQuantityForSubscribedResultantSecurities <AddtlQtyForSbcbdRsltntScties>
Presence: [0..1]
Definition: Quantity of additional intermediate securities/new equities awarded for a given quantity of
securities derived from subscription.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 191 February 2026
```

