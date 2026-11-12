---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.26 TransactionOverhead <TxOvrhd>", "46.4.5.10.26.1 TotalOverheadApplied <TtlOvrhdApld>"]
file_pages: [2378]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.26.1 TotalOverheadApplied <TtlOvrhdApld>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2378 to 2378.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2378

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 2390
         Suffix <Sfx> [0..1] Text 2390
         Type <Tp> [1..1]  2390
{Or           Code <Cd> [1..1] CodeSet 2391
Or}           Proprietary <Prtry> [1..1] Text 2392
       Description <Desc> [0..1] Text 2392
     Quantity <Qty> [1..1]  2393
{Or       Quantity <Qty> [1..1] ± C16 2393
Or}       ProprietaryQuantity <PrtryQty> [1..1]  2393
         Quantity <Qty> [1..1] Quantity 2394
         QuantityType <QtyTp> [1..1] Text 2394
         Issuer <Issr> [1..1] Text 2394
         SchemeName <SchmeNm> [0..1] Text 2394
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2394
Constraints
• NonStandardsSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
• TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
46.4.5.10.26.1  TotalOverheadApplied <TtlOvrhdApld>
Presence: [0..1]
Definition: Total amount of overhead applied to the transaction that impacts the settlement amount.
Impacted by: C3 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2378 May 2026
```

