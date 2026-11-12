---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["4 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "4.4 Message Building Blocks", "4.4.2 SecuritiesAccountStatus <SctiesAcctSts>", "4.4.2.1 RelatedSecuritiesAccount <RltdSctiesAcct>"]
file_pages: [29]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.020.001.01"]
---

# 4.4.2.1 RelatedSecuritiesAccount <RltdSctiesAcct>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 29 to 29.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 29

```text
SecuritiesAccountStatus <SctiesAcctSts> contains the following SecuritiesAccountStatus2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RelatedSecuritiesAccount <RltdSctiesAcct> [0..1] ± 29
   Status <Sts> [1..1] CodeSet 29
   StatusReason <StsRsn> [0..*]  30
     Reason <Rsn> [1..1]  30
{Or       Code <Cd> [1..1] CodeSet 30
Or}       Proprietary <Prtry> [1..1] Text 30
     AdditionalInformation <AddtlInf> [0..1] Text 30
Constraints
• PresenceRule
If Status equals COMP (Completed) then RelatedSecuritiesAccount must be present.
• StatusReasonRule
If Status equals REJT (Rejected) then StatusReason must be present.
4.4.2.1  RelatedSecuritiesAccount <RltdSctiesAcct>
Presence: [0..1]
Definition: Unique identification of the securities account referenced by a request.
RelatedSecuritiesAccount <RltdSctiesAcct> contains the following elements (see
"SecuritiesAccount19" on page 79 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 79
   Type <Tp> [0..1] ± 79
   Name <Nm> [0..1] Text 79
4.4.2.2  Status <Sts>
Presence: [1..1]
Definition: Status of the securities account maintenance instruction.
Datatype: "Status6Code" on page 96
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities - Securities Account Reference Data 29 December 2019
```

