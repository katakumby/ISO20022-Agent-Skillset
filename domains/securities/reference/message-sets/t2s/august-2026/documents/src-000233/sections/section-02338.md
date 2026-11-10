---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.1 SettlementStatus32Choice", "82.1.30.1.1 Pending <Pdg>"]
file_pages: [3119]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.1.1 Pending <Pdg>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3119 to 3119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3119

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  3119
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3120
Or}     Reason <Rsn> [1..*]  3120
       Code <Cd> [1..1]  3120
{Or         Code <Cd> [1..1] CodeSet 3120
Or}         Proprietary <Prtry> [1..1] ± 3123
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3124
Or   Failing <Flng> [1..1]  3124
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3124
Or}     Reason <Rsn> [1..*]  3124
       Code <Cd> [1..1]  3125
{Or         Code <Cd> [1..1] CodeSet 3125
Or}         Proprietary <Prtry> [1..1] ± 3128
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3129
Or}   Proprietary <Prtry> [1..1] ± 3129
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
82.1.30.1.1  Pending <Pdg>
Presence: [1..1]
Definition: Instruction is pending. Settlement at the instructed settlement date is still possible.
Pending <Pdg> contains one of the following PendingStatus73Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3120
Or}   Reason <Rsn> [1..*]  3120
     Code <Cd> [1..1]  3120
{Or       Code <Cd> [1..1] CodeSet 3120
Or}       Proprietary <Prtry> [1..1] ± 3123
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3124
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3119 August 2026
```

