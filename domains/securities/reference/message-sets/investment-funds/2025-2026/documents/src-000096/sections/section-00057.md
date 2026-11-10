---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["6 acmt.006.001.07 AccountManagementStatusReportV07", "6.4 Message Building Blocks", "6.4.3 StatusReport <StsRpt>"]
file_pages: [89]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.006.001.07"]
---

# 6.4.3 StatusReport <StsRpt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 89 to 89.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 89

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference13" on
page 4546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4546
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4547
6.4.3 StatusReport <StsRpt>
Presence: [1..1]
Definition: Status details of the account management instruction for which the status is provided.
StatusReport <StsRpt> contains the following AccountManagementStatusAndReason5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
6.4.3.1  Status <Sts>
Presence: [1..1]
Definition: Status of the account management instruction that was previously received.
Status <Sts> contains one of the following elements (see "Status25Choice" on page 5173 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Status <Sts> [1..1] CodeSet 5173
Or}   Rejected <Rjctd> [1..10] ± 5173
6.4.3.2  StatusReason <StsRsn>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 acmt.006.001.07
AccountManagementStatusReportV07
Investment Funds - Maintenance 2025 - 2026 89 May 2026
```

