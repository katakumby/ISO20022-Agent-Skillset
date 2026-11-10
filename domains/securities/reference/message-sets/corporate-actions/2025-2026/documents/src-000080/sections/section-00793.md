---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.64 PendingStatus74Choice"]
file_pages: [988]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.64 PendingStatus74Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 988 to 988.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 988

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.64  PendingStatus74Choice
Definition: Choice between a reason or no reason for the corporate action event processing pending
status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 988
Or}   Reason <Rsn> [1..*] ± C1 988
16.1.15.64.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Reason not specified.
Datatype: "NoReasonCode" on page 1223
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
16.1.15.64.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the pending status.
Impacted by: C1 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following elements (see "PendingStatusReason29" on page 1153 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1] ± 1153
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1153
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 988 February 2026
```

