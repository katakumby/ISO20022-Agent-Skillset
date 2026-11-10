---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.51 SettlementStatus34Choice", "82.1.30.51.2 Failing <Flng>", "82.1.30.51.2.2 Reason <Rsn>"]
file_pages: [3200]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.51.2.2 Reason <Rsn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3200 to 3200.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3200

```text
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.51.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the failing status.
Reason <Rsn> contains the following elements (see "FailingReason15" on page 3200 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  3200
{Or     Code <Cd> [1..1] CodeSet 3201
Or}     Proprietary <Prtry> [1..1] ± 3201
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3202
82.1.30.51.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 3130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 3130
   ProprietaryReason <PrtryRsn> [0..*] ± C6 3130
82.1.30.52  FailingReason15
Definition: Specifies the reason why the instruction or request has a failing settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  3200
{Or     Code <Cd> [1..1] CodeSet 3201
Or}     Proprietary <Prtry> [1..1] ± 3201
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3202
82.1.30.52.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a failing status.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3200 August 2026
```

