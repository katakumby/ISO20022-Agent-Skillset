---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.10 AmountDetails <AmtDtls>", "7.4.13.23.10.1 GrossAmount <GrssAmt>"]
file_pages: [492]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.10.1 GrossAmount <GrssAmt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 492 to 492.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 492

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ChargesAmount <ChrgsAmt> [0..1] Amount C1, C14 504
   EntitledAmount <EntitldAmt> [0..1] Amount C1, C14 504
   OriginalAmount <OrgnlAmt> [0..1] Amount C1, C14 505
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C1, C14 505
   IncomePortion <IncmPrtn> [0..1] Amount C1, C14 505
   EqualisationAmount <EqulstnAmt> [0..1] Amount C1, C14 506
   FATCATaxAmount <FATCATaxAmt> [0..1] Amount C1, C14 506
   NRATaxAmount <NRATaxAmt> [0..1] Amount C1, C14 507
   BackUpWithholdingTaxAmount
<BckUpWhldgTaxAmt>
[0..1] Amount C1, C14 507
   TaxOnIncomeAmount <TaxOnIncmAmt> [0..1] Amount C1, C14 507
   TransactionTax <TxTax> [0..1] Amount C1, C14 508
   DeemedAmount <DmdAmt> [0..1] Amount C1, C14 508
   ForeignIncomeAmount <FrgnIncmAmt> [0..1] Amount C1, C14 509
   DeemedDividendAmount <DmdDvddAmt> [0..1] Amount C1, C14 509
   DeemedFundAmount <DmdFndAmt> [0..1] Amount C1, C14 509
   DeemedInterestAmount <DmdIntrstAmt> [0..1] Amount C1, C14 510
   DeemedRoyaltiesAmount <DmdRyltsAmt> [0..1] Amount C1, C14 510
   BuyUpAmount <BuyUpAmt> [0..1] Amount C1, C14 511
7.4.13.23.10.1  GrossAmount <GrssAmt>
Presence: [0..1]
Definition: Amount of money before any tax deductions have been made.
Impacted by: C1 "ActiveCurrency", C14 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 492 February 2026
```

