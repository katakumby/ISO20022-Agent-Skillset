---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.26 TransactionOverhead <TxOvrhd>", "43.4.5.9.26.1 TotalOverheadApplied <TtlOvrhdApld>"]
file_pages: [1958]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.26.1 TotalOverheadApplied <TtlOvrhdApld>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1958 to 1958.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1958

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 1970
         Suffix <Sfx> [0..1] Text 1970
         Type <Tp> [1..1]  1970
{Or           Code <Cd> [1..1] CodeSet 1971
Or}           Proprietary <Prtry> [1..1] Text 1972
       Description <Desc> [0..1] Text 1972
     Quantity <Qty> [1..1]  1973
{Or       Quantity <Qty> [1..1] ± C16 1973
Or}       ProprietaryQuantity <PrtryQty> [1..1]  1973
         Quantity <Qty> [1..1] Quantity 1974
         QuantityType <QtyTp> [1..1] Text 1974
         Issuer <Issr> [1..1] Text 1974
         SchemeName <SchmeNm> [0..1] Text 1974
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1974
Constraints
• NonStandardsSLAReferenceRule
For each value of IndividualFee/Type, NonStandardSLAReference may only be present once.
• TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
43.4.5.9.26.1  TotalOverheadApplied <TtlOvrhdApld>
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
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1958 May 2026
```

