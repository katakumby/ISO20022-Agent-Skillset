---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.3 InvestmentAccount74"]
file_pages: [4557, 4558]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.3 InvestmentAccount74

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4557 to 4558.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4557

```text
66.1.24.3  InvestmentAccount74
Definition: Information about a securities account and its characteristics.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4557 May 2026
```

## File page 4558

```text
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
   InvestmentAccountCategory <InvstmtAcctCtgy> [0..1] ± 4570
   Pledging <Pldgg> [0..1] CodeSet 4570
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4558 May 2026
```

