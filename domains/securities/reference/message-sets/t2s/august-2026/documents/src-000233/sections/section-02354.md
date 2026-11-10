---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.10 SettlementStatus16Choice", "82.1.30.10.1 Pending <Pdg>", "82.1.30.10.1.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [3141]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.10.1.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3141 to 3141.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3141

```text
Definition: Instruction is pending. Settlement at the instructed settlement date is still possible.
Pending <Pdg> contains one of the following PendingStatus36Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3141
Or}   Reason <Rsn> [1..*] ± 3141
82.1.30.10.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.10.1.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Reason <Rsn> contains the following elements (see "PendingReason14" on page 3176 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  3176
{Or     Code <Cd> [1..1] CodeSet 3176
Or}     Proprietary <Prtry> [1..1] ± 3179
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3179
82.1.30.10.2  Failing <Flng>
Presence: [1..1]
Definition: Instruction is failing. Settlement at the instructed settlement date is no longer possible.
Failing <Flng> contains one of the following FailingStatus9Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3141
Or}   Reason <Rsn> [1..*] ± 3142
82.1.30.10.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3141 August 2026
```

