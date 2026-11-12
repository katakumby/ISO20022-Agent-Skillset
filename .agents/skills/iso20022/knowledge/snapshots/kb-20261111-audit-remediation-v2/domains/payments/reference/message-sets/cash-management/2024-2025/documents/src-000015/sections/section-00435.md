---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["22 camt.024.001.08 ModifyStandingOrderV08", "22.2 Structure"]
file_pages: [592]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.024.001.08"]
---

# 22.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 592 to 592.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 592

```text
Identifies the standing order.
C. NewStandingOrderValueSet
New set of values for the standing order.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
22.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ModfyStgOrdr> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 594
   StandingOrderIdentification <StgOrdrId> [1..1]  594
     Identification <Id> [0..1] Text 594
     Account <Acct> [1..1] ± C8, C7 594
     AccountOwner <AcctOwnr> [0..1] ± 595
   NewStandingOrderValueSet <NewStgOrdrValSet> [1..1]  C9 596
     Amount <Amt> [0..1] ± 597
     Creditor <Cdtr> [0..1] ± 598
     CreditorAccount <CdtrAcct> [0..1] ± C8, C7 598
     Debtor <Dbtr> [0..1] ± 599
     DebtorAccount <DbtrAcct> [0..1] ± C8, C7 599
     ExecutionType <ExctnTp> [0..1]  600
{Or       Time <Tm> [1..1] Time 600
Or}       Event <Evt> [1..1]  600
{Or         Code <Cd> [1..1] CodeSet 601
Or}         Proprietary <Prtry> [1..1] Text 601
     Frequency <Frqcy> [0..1] CodeSet 601
     ValidityPeriod <VldtyPrd> [0..1]  601
{Or       FromDate <FrDt> [1..1] Date 602
Or       ToDate <ToDt> [1..1] Date 602
Or}       FromToDate <FrToDt> [1..1] ± 602
     ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 602
   SupplementaryData <SplmtryData> [0..*] ± C10 602
Approved by the Payments SEG on 04 February 2025 camt.024.001.08 ModifyStandingOrderV08
Cash Management - Maintenance 2024 - 2025 592 February 2025
```

