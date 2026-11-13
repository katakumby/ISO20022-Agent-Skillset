---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.1 StandingOrderIdentification <StgOrdrId>"]
file_pages: [716]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.1 StandingOrderIdentification <StgOrdrId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 716 to 716.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 716

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DebtorAccount <DbtrAcct> [0..1] ± C8, C7 729
       TotalsPerStandingOrder <TtlsPerStgOrdr> [0..1]  730
         SetPredefinedOrder <SetPrdfndOrdr> [1..1]  730
           TotalAmount <TtlAmt> [1..1] Amount 731
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 731
           Currency <Ccy> [0..1] CodeSet C1 731
         PendingPredefinedOrder <PdgPrdfndOrdr> [1..1]  731
           TotalAmount <TtlAmt> [1..1] Amount 732
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 732
           Currency <Ccy> [0..1] CodeSet C1 732
         SetStandingOrder <SetStgOrdr> [1..1]  732
           TotalAmount <TtlAmt> [1..1] Amount 733
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 733
           Currency <Ccy> [0..1] CodeSet C1 733
         PendingStandingOrder <PdgStgOrdr> [1..1]  733
           TotalAmount <TtlAmt> [1..1] Amount 734
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 734
           Currency <Ccy> [0..1] CodeSet C1 734
       ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 734
Or}     BusinessError <BizErr> [1..*]  735
       Error <Err> [1..1]  735
{Or         Code <Cd> [1..1] CodeSet 735
Or}         Proprietary <Prtry> [1..1] Text 735
       Description <Desc> [0..1] Text 735
31.4.2.1.1  StandingOrderIdentification <StgOrdrId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 716 February 2025
```

