---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["34 camt.102.001.03 CreateStandingOrderV03", "34.2 Structure"]
file_pages: [756]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.102.001.03"]
---

# 34.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 756 to 756.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 756

```text
34.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CretStgOrdr> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 757
   StandingOrderIdentification <StgOrdrId> [1..1]  758
     Identification <Id> [0..1] Text 758
     Account <Acct> [1..1] ± C8, C7 758
     AccountOwner <AcctOwnr> [0..1] ± 759
   ValueSet <ValSet> [1..1]  C9 759
     Amount <Amt> [0..1] ± 760
     Creditor <Cdtr> [0..1] ± 760
     CreditorAccount <CdtrAcct> [0..1] ± C8, C7 761
     Debtor <Dbtr> [0..1] ± 762
     DebtorAccount <DbtrAcct> [0..1] ± C8, C7 762
     ExecutionType <ExctnTp> [0..1]  763
{Or       Time <Tm> [1..1] Time 763
Or}       Event <Evt> [1..1]  763
{Or         Code <Cd> [1..1] CodeSet 764
Or}         Proprietary <Prtry> [1..1] Text 764
     Frequency <Frqcy> [0..1] CodeSet 764
     ValidityPeriod <VldtyPrd> [0..1]  764
{Or       FromDate <FrDt> [1..1] Date 765
Or       ToDate <ToDt> [1..1] Date 765
Or}       FromToDate <FrToDt> [1..1] ± 765
     ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 765
   SupplementaryData <SplmtryData> [0..*] ± C10 765
34.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Payments SEG on 04 February 2025 camt.102.001.03 CreateStandingOrderV03
Cash Management - Maintenance 2024 - 2025 756 February 2025
```

