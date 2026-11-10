---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["40 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "40.4 Message Building Blocks", "40.4.2 SecuritiesAccountStatus <SctiesAcctSts>", "40.4.2.1 RelatedSecuritiesAccount <RltdSctiesAcct>"]
file_pages: [2121]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.020.001.01"]
---

# 40.4.2.1 RelatedSecuritiesAccount <RltdSctiesAcct>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2121 to 2121.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2121

```text
SecuritiesAccountStatus <SctiesAcctSts> contains the following SecuritiesAccountStatus2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RelatedSecuritiesAccount <RltdSctiesAcct> [0..1] ± 2121
   Status <Sts> [1..1] CodeSet 2121
   StatusReason <StsRsn> [0..*]  2122
     Reason <Rsn> [1..1]  2122
{Or       Code <Cd> [1..1] CodeSet 2122
Or}       Proprietary <Prtry> [1..1] Text 2122
     AdditionalInformation <AddtlInf> [0..1] Text 2122
Constraints
• PresenceRule
If Status equals COMP (Completed) then RelatedSecuritiesAccount must be present.
• StatusReasonRule
If Status equals REJT (Rejected) then StatusReason must be present.
40.4.2.1  RelatedSecuritiesAccount <RltdSctiesAcct>
Presence: [0..1]
Definition: Unique identification of the securities account referenced by a request.
RelatedSecuritiesAccount <RltdSctiesAcct> contains the following elements (see
"SecuritiesAccount19" on page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
40.4.2.2  Status <Sts>
Presence: [1..1]
Definition: Status of the securities account maintenance instruction.
Datatype: "Status6Code" on page 3305
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities 2121 August 2026
```

