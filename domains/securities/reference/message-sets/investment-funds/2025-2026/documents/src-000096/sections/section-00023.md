---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["3 acmt.002.001.08 AccountDetailsConfirmationV08", "3.4 Message Building Blocks", "3.4.5 InvestmentAccount <InvstmtAcct>"]
file_pages: [46, 47]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.002.001.08"]
---

# 3.4.5 InvestmentAccount <InvstmtAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 46 to 47.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 46

```text
3.4.5 InvestmentAccount <InvstmtAcct>
Presence: [0..1]
Definition: Confirmation of the information related to the investment account.
Impacted by: C21 "IncomePreferenceReinvestment1Rule", C31 "ReinvestmentPercentage1Rule", C17
"FinancialInstrumentDetailsGuideline"
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 46 May 2026
```

## File page 47

```text
InvestmentAccount <InvstmtAcct> contains the following elements (see "InvestmentAccount74" on
page 4557 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4559
   AccountStatus <AcctSts> [0..1] ± C6, C7,
C8, C9,
C10,
C11,
C14,
C15,
C32
4559
   BlockedStatus <BlckdSts> [0..1] ± 4561
   StatusDate <StsDt> [0..1] ± 4561
   Name <Nm> [0..1] Text 4562
   Designation <Dsgnt> [0..1] Text 4562
   Type <Tp> [0..1] ± 4562
   OwnershipType <OwnrshTp> [0..1] ± 4562
   TaxExemption <TaxXmptn> [0..1] ± 4563
   StatementFrequency <StmtFrqcy> [0..1] ± 4563
   ReferenceCurrency <RefCcy> [0..1] CodeSet C1 4563
   Language <Lang> [0..1] CodeSet C34 4563
   IncomePreference <IncmPref> [0..1] CodeSet 4564
   ReinvestmentDetails <RinvstmtDtls> [0..*] ± 4564
   TaxWithholdingMethod <TaxWhldgMtd> [0..1] CodeSet 4564
   TaxReporting <TaxRptg> [0..*] ± 4565
   LetterIntentDetails <LttrInttDtls> [0..1] ± 4566
   AccumulationRightReference <AcmltnRghtRef> [0..1] Text 4567
   RequiredSignatoriesNumber <ReqrdSgntriesNb> [0..1] Quantity 4567
   FundFamilyName <FndFmlyNm> [0..1] Text 4567
   FinancialInstrumentDetails <FinInstrmDtls> [0..*] ± C20 4567
   RoundingDetails <RndgDtls> [0..1] ± 4568
   AccountServicer <AcctSvcr> [0..1] ± 4569
   AccountUsageType <AcctUsgTp> [0..1] ± 4569
   ForeignStatusCertification <FrgnStsCertfctn> [0..1] CodeSet 4569
   AccountSignatureDateTime <AcctSgntrDtTm> [0..1] ± 4569
   TransactionChannelType <TxChanlTp> [0..1] ± 4570
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 47 May 2026
```

