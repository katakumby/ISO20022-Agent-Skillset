---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.8 Reinvestment4", "66.1.24.8.3 ReinvestmentPercentage <RinvstmtPctg>"]
file_pages: [4618, 4619]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.8.3 ReinvestmentPercentage <RinvstmtPctg>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4618 to 4619.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4618

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.24.8.3  ReinvestmentPercentage <RinvstmtPctg>
Presence: [1..1]
Definition: Percentage of the reinvestment.
Datatype: "PercentageRate" on page 5401
66.1.24.9  InvestmentAccount73
Definition: Information about a securities account and its characteristics.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4618 May 2026
```

## File page 4619

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4620
   Name <Nm> [0..1] Text 4620
   Designation <Dsgnt> [0..1] Text 4620
   Type <Tp> [0..1] ± 4621
   OwnershipType <OwnrshTp> [1..1] ± 4621
   TaxExemption <TaxXmptn> [0..1] ± 4621
   StatementFrequency <StmtFrqcy> [0..1] ± 4621
   ReferenceCurrency <RefCcy> [0..1] CodeSet C1 4622
   Language <Lang> [0..1] CodeSet C34 4622
   IncomePreference <IncmPref> [0..1] CodeSet 4622
   ReinvestmentDetails <RinvstmtDtls> [0..*] ± 4622
   TaxWithholdingMethod <TaxWhldgMtd> [0..1] CodeSet 4623
   TaxReporting <TaxRptg> [0..*] ± 4623
   LetterIntentDetails <LttrInttDtls> [0..1] ± 4624
   AccumulationRightReference <AcmltnRghtRef> [0..1] Text 4625
   RequiredSignatoriesNumber <ReqrdSgntriesNb> [0..1] Quantity 4625
   FundFamilyName <FndFmlyNm> [0..1] Text 4625
   FinancialInstrumentDetails <FinInstrmDtls> [0..*] ± C20 4625
   RoundingDetails <RndgDtls> [0..1] ± 4626
   AccountServicer <AcctSvcr> [0..1] ± 4627
   BlockedStatus <BlckdSts> [0..1] ± 4627
   AccountUsageType <AcctUsgTp> [0..1] ± 4628
   ForeignStatusCertification <FrgnStsCertfctn> [0..1] CodeSet 4628
   AccountSignatureDateTime <AcctSgntrDtTm> [0..1] ± 4628
   TransactionChannelType <TxChanlTp> [0..1] ± 4628
   InvestmentAccountCategory <InvstmtAcctCtgy> [0..1] ± 4628
   Pledging <Pldgg> [0..1] CodeSet 4629
   Collateral <Coll> [0..1] CodeSet 4629
   ThirdPartyRights <ThrdPtyRghts> [0..1] ± 4629
   PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl> [0..1] ± 4630
   AccountingStatus <AcctgSts> [0..1] ± 4630
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4619 May 2026
```

