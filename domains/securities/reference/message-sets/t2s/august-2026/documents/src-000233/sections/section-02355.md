---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.10 SettlementStatus16Choice", "82.1.30.10.2 Failing <Flng>", "82.1.30.10.2.2 Reason <Rsn>"]
file_pages: [3142]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.10.2.2 Reason <Rsn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3142 to 3142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3142

```text
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.10.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the failing status.
Reason <Rsn> contains the following elements (see "FailingReason7" on page 3131 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  3131
{Or     Code <Cd> [1..1] CodeSet 3131
Or}     Proprietary <Prtry> [1..1] ± 3134
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3135
82.1.30.10.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 3130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 3130
   ProprietaryReason <PrtryRsn> [0..*] ± C6 3130
82.1.30.11  Reason18Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [0..*] ± C6 3142
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3143
82.1.30.11.1  Reason <Rsn>
Presence: [0..*]
Definition: Specifies the reason of the Status.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3142 August 2026
```

