---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.76 ResponseStatus6Choice"]
file_pages: [1992]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.76 ResponseStatus6Choice

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1992 to 1992.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1992

```text
35.1.29.76  ResponseStatus6Choice
Definition: Choice of response status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Consented <Cnsntd> [1..1] ± 1992
Or   Rejected <Rjctd> [1..1] ± 1992
Or}   Pending <Pdg> [1..1] ± 1992
35.1.29.76.1  Consented <Cnsntd>
Presence: [1..1]
Definition: Reason provided for the status.
Consented <Cnsntd> contains one of the following elements (see "ConsentStatus4Choice" on
page 1872 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1872
Or}   Reason <Rsn> [1..*]  1872
     Code <Cd> [1..1]  1873
{Or       Code <Cd> [1..1] CodeSet 1873
Or}       Proprietary <Prtry> [1..1] ± 1873
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1874
35.1.29.76.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Rejected status of an instruction, advice or request.
Rejected <Rjctd> contains one of the following elements (see "RejectionStatus20Choice" on
page 1985 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1985
Or}   Reason <Rsn> [1..1]  1985
     Code <Cd> [1..1]  1986
{Or       Code <Cd> [1..1] CodeSet 1986
Or}       Proprietary <Prtry> [1..1] ± 1986
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1987
35.1.29.76.3  Pending <Pdg>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1992 March 2026
```

