---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.9 UnitsDetails <UnitsDtls>", "35.4.14.10.9.8 TransactionOverhead <TxOvrhd>", "35.4.14.10.9.8.1 TotalOverheadApplied <TtlOvrhdApld>"]
file_pages: [1041]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.9.8.1 TotalOverheadApplied <TtlOvrhdApld>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1041 to 1041.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1041

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 1053
         Suffix <Sfx> [0..1] Text 1053
         Type <Tp> [1..1]  1053
{Or           Code <Cd> [1..1] CodeSet 1054
Or}           Proprietary <Prtry> [1..1] Text 1055
       Description <Desc> [0..1] Text 1055
     Quantity <Qty> [1..1]  1056
{Or       Quantity <Qty> [1..1] ± C22 1056
Or}       ProprietaryQuantity <PrtryQty> [1..1]  1056
         Quantity <Qty> [1..1] Quantity 1057
         QuantityType <QtyTp> [1..1] Text 1057
         Issuer <Issr> [1..1] Text 1057
         SchemeName <SchmeNm> [0..1] Text 1057
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1057
Constraints
• NonStandardSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
• TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
35.4.14.10.9.8.1  TotalOverheadApplied <TtlOvrhdApld>
Presence: [0..1]
Definition: Total amount of overhead applied to the transaction that impacts the settlement amount.
Impacted by: C1 "ActiveCurrency", C18 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1041 May 2026
```

