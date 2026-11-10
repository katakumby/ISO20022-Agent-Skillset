---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["6 acmt.006.001.07 AccountManagementStatusReportV07", "6.4 Message Building Blocks", "6.4.3 StatusReport <StsRpt>", "6.4.3.3 AccountApplicationIdentification <AcctApplId>"]
file_pages: [90, 91]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.006.001.07"]
---

# 6.4.3.3 AccountApplicationIdentification <AcctApplId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 90 to 91.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 90

```text
Definition: Reason for the status of the account management instruction.
StatusReason <StsRsn> contains one of the following elements (see
"AcceptedStatusReason1Choice" on page 5186 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5186
Or}   Proprietary <Prtry> [1..1] ± 5187
6.4.3.3  AccountApplicationIdentification <AcctApplId>
Presence: [0..1]
Definition: Unique and unambiguous identifier of the account opening or modification instruction at
application level.
Datatype: "Max35Text" on page 5403
6.4.3.4  ExistingAccountIdentification <ExstgAcctId>
Presence: [0..*]
Definition: Account to which the account opening is related.
ExistingAccountIdentification <ExstgAcctId> contains the following elements (see "Account23" on
page 4325 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 4325
   RelatedAccountDetails <RltdAcctDtls> [0..1] ± 4325
6.4.3.5  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
6.4.3.6  AccountStatus <AcctSts>
Presence: [0..1]
Definition: Status of the account.
Impacted by: C2 "ClosedStatus1Rule", C3 "ClosedStatus2Rule", C4 "ClosedStatus3Rule", C5
"ClosedStatus4Rule", C6 "ClosedStatus5Rule", C7 "ClosedStatus6Rule", C9
"EnabledDisabledStatus1Rule", C10 "EnabledDisabledStatus2Rule", C12 "StatusElementRule"
Approved by the Securities SEG on 27 January 2026 acmt.006.001.07
AccountManagementStatusReportV07
Investment Funds - Maintenance 2025 - 2026 90 May 2026
```

## File page 91

```text
AccountStatus <AcctSts> contains the following elements (see "AccountStatus2" on page 5174 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Enabled <Nbld> [0..1] ± 5176
   Disabled <Dsbld> [0..1] ± 5176
   Pending <Pdg> [0..1] ± 5177
   PendingOpening <PdgOpng> [0..1] ± 5177
   Proforma <Profrm> [0..1] ± 5177
   Closed <Clsd> [0..1] ± 5178
   ClosurePending <ClsrPdg> [0..1] ± 5178
   Other <Othr> [0..*] ± 5179
Constraints
• ClosedStatus1Rule
If Closed is present then Enabled is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Enabled Must be absent
• ClosedStatus2Rule
If Closed is present then Disabled is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Disabled Must be absent
• ClosedStatus3Rule
If Closed is present then Pending is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Pending Must be absent
• ClosedStatus4Rule
If Closed is present then PendingOpening is not allowed.
On Condition
    /Closed is present
Following Must be True
    /PendingOpening Must be absent
• ClosedStatus5Rule
If Closed is present then Proforma is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Proforma Must be absent
Approved by the Securities SEG on 27 January 2026 acmt.006.001.07
AccountManagementStatusReportV07
Investment Funds - Maintenance 2025 - 2026 91 May 2026
```

