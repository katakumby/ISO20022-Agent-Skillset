---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "2.2 Structure"]
file_pages: [7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.023.001.02"]
---

# 2.2 Structure

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 7 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesEndOfPrcRpt> [1..1]  
   Pagination <Pgntn> [0..*] ± 8
   ReportGeneralDetails <RptGnlDtls> [1..1]  9
     ReportNumber <RptNb> [0..1] Text 9
     QueryReference <QryRef> [0..1] ± 9
     ReportIdentification <RptId> [0..1] Text 9
     ReportDateTime <RptDtTm> [1..1] ± 9
     Frequency <Frqcy> [0..1] ± 10
     UpdateType <UpdTp> [0..1] ± 10
     NoticeType <NtceTp> [0..1] ± 10
   ConfirmationParties <ConfPties> [0..*]  11
     Buyer <Buyr> [0..1] ± 11
     Borrower <Brrwr> [0..1] ± 12
     Seller <Sellr> [0..1] ± 13
     Lender <Lndr> [0..1] ± 14
     BrokerOfCredit <BrkrOfCdt> [0..1] ± 15
     IntroducingFirm <IntrdcgFirm> [0..1] ± 16
     StepInFirm <StepInFirm> [0..1] ± 17
     StepOutFirm <StepOutFirm> [0..1] ± 18
     ClearingFirm <ClrFirm> [0..1] ± 19
     ExecutingBroker <ExctgBrkr> [0..1] ± 20
     CMUParty <CMUPty> [0..1] ± 21
     CMUCounterparty <CMUCtrPty> [0..1] ± 22
     AffirmingParty <AffrmgPty> [0..1] ± 23
     TradeBeneficiaryParty <TradBnfcryPty> [0..1] ± 24
   Investor <Invstr> [0..*] ± C6 25
   SupplementaryData <SplmtryData> [0..*] ± C7 26
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 7 February 2025
```

