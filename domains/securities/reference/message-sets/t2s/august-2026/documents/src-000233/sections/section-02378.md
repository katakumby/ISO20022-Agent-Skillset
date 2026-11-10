---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.28 ProcessingStatus72Choice", "82.1.30.28.3 Rejected <Rjctd>"]
file_pages: [3165]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.28.3 Rejected <Rjctd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3165 to 3165.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3165

```text
PendingProcessing <PdgPrcg> contains one of the following elements (see "Reason18Choice" on
page 3142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [0..*] ± C6 3142
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3143
82.1.30.28.3  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction is rejected by the executing party.
Rejected <Rjctd> contains one of the following elements (see "Reason18Choice" on page 3142 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [0..*] ± C6 3142
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3143
82.1.30.28.4  Completed <Cmpltd>
Presence: [1..1]
Definition: Instruction has been completed by the executing party.
Completed <Cmpltd> contains the following Reason4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..*] ± C6 3165
82.1.30.28.4.1  Reason <Rsn>
Presence: [0..*]
Definition: Specifies the reason of the Status.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following elements (see "ProprietaryReason4" on page 3139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3165 August 2026
```

