---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.4 Status <Sts>", "81.4.6.11.4.4.1 Status <Sts>"]
file_pages: [2795]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.4.1 Status <Sts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2795 to 2795.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2795

```text
Definition: Status of a penalty.
Status <Sts> contains the following PenaltyStatus2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1]  2795
{Or     Code <Cd> [1..1] CodeSet 2795
Or}     Proprietary <Prtry> [1..1] ± 2795
   Reason <Rsn> [0..*]  2796
     Reason <Rsn> [1..1]  2796
{Or       Code <Cd> [1..1] CodeSet 2796
Or}       Proprietary <Prtry> [1..1] ± 2797
     AdditionalStatusReason <AddtlStsRsn> [0..1] Text 2797
81.4.6.11.4.4.1  Status <Sts>
Presence: [1..1]
Definition: Status of a penalty.
Status <Sts> contains one of the following PenaltyStatus2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2795
Or}   Proprietary <Prtry> [1..1] ± 2795
81.4.6.11.4.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Penalty status, , in a coded form.
Datatype: "PenaltyStatus2Code" on page 3268
CodeName Name Definition
ACTV Active Penalty is active for the party.
NCOM NotComputed Penalty could not be computed.
REMO Removed Removal of a cash penalty where
settlement cannot be performed for
reasons that are independent from any
of the CSD participants or the CSD.
81.4.6.11.4.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Penalty status, in a proprietary form.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2795 August 2026
```

