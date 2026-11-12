---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.4 UnitsDetails <UnitsDtls>", "38.4.15.8.4.8 TransactionOverhead <TxOvrhd>", "38.4.15.8.4.8.1 TotalOverheadApplied <TtlOvrhdApld>"]
file_pages: [1402]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.4.8.1 TotalOverheadApplied <TtlOvrhdApld>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1402 to 1402.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1402

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 1414
         Suffix <Sfx> [0..1] Text 1414
         Type <Tp> [1..1]  1414
{Or           Code <Cd> [1..1] CodeSet 1415
Or}           Proprietary <Prtry> [1..1] Text 1416
       Description <Desc> [0..1] Text 1416
     Quantity <Qty> [1..1]  1417
{Or       Quantity <Qty> [1..1] ± C20 1417
Or}       ProprietaryQuantity <PrtryQty> [1..1]  1417
         Quantity <Qty> [1..1] Quantity 1418
         QuantityType <QtyTp> [1..1] Text 1418
         Issuer <Issr> [1..1] Text 1418
         SchemeName <SchmeNm> [0..1] Text 1418
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1418
Constraints
• NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
• TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
38.4.15.8.4.8.1  TotalOverheadApplied <TtlOvrhdApld>
Presence: [0..1]
Definition: Total amount of overhead applied to the transaction that impacts the settlement amount.
Impacted by: C1 "ActiveCurrency", C15 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1402 May 2026
```

