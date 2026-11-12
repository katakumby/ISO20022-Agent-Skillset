---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.15 Status", "13.1.15.5 ProcessingStatus72Choice", "13.1.15.5.3 Rejected <Rjctd>"]
file_pages: [503]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.15.5.3 Rejected <Rjctd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 503 to 503.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 503

```text
PendingProcessing <PdgPrcg> contains one of the following elements (see "Reason18Choice" on
page 501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [0..*] ± C1 501
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 501
13.1.15.5.3  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction is rejected by the executing party.
Rejected <Rjctd> contains one of the following elements (see "Reason18Choice" on page 501 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [0..*] ± C1 501
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 501
13.1.15.5.4  Completed <Cmpltd>
Presence: [1..1]
Definition: Instruction has been completed by the executing party.
Completed <Cmpltd> contains the following Reason4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..*] ± C1 503
13.1.15.5.4.1  Reason <Rsn>
Presence: [0..*]
Definition: Specifies the reason of the Status.
Impacted by: C1 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following elements (see "ProprietaryReason4" on page 500 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 500
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 500
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 503 March 2024
```

