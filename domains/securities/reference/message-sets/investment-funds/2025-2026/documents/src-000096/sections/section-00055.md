---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["6 acmt.006.001.07 AccountManagementStatusReportV07", "6.2 Structure"]
file_pages: [87]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.006.001.07"]
---

# 6.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 87 to 87.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 87

```text
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctMgmtStsRpt> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 88
   RelatedReference <RltdRef> [1..2] ± 88
   StatusReport <StsRpt> [1..1]  89
     Status <Sts> [1..1] ± 89
     StatusReason <StsRsn> [0..*] ± 89
     AccountApplicationIdentification <AcctApplId> [0..1] Text 90
     ExistingAccountIdentification <ExstgAcctId> [0..*] ± 90
     AccountIdentification <AcctId> [0..1] Text 90
     AccountStatus <AcctSts> [0..1] ± C2, C3,
C4, C5,
C6, C7,
C9, C10,
C12
90
     BlockedStatus <BlckdSts> [0..1] ± 92
     FATCAReportingDate <FATCARptgDt> [0..1] Date 92
     CRSReportingDate <CRSRptgDt> [0..1] Date 93
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 93
   Extension <Xtnsn> [0..*] ± C11 93
6.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 ClosedStatus1Rule
If Closed is present then Enabled is not allowed.
C3 ClosedStatus2Rule
If Closed is present then Disabled is not allowed.
C4 ClosedStatus3Rule
If Closed is present then Pending is not allowed.
C5 ClosedStatus4Rule
If Closed is present then PendingOpening is not allowed.
Approved by the Securities SEG on 27 January 2026 acmt.006.001.07
AccountManagementStatusReportV07
Investment Funds - Maintenance 2025 - 2026 87 May 2026
```

