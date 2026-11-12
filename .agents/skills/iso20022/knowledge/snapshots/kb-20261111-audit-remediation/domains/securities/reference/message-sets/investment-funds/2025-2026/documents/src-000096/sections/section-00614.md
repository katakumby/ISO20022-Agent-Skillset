---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.6 TransferStatus <TrfSts>", "34.4.4.6.1 Status <Sts>"]
file_pages: [843]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.6.1 Status <Sts>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 843 to 843.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 843

```text
TransferStatus <TrfSts> contains one of the following TransferStatus5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Status <Sts> [1..1] ± 843
Or   PendingSettlement <PdgSttlm> [1..1] ± 843
Or   Unmatched <Umtchd> [1..1] ± 844
Or   InRepair <InRpr> [1..1] ± 844
Or   Rejected <Rjctd> [1..10]  C25 844
     Reason <Rsn> [1..1]  845
{Or       Code <Cd> [1..1] CodeSet 845
Or}       Proprietary <Prtry> [1..1] ± 847
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 848
Or   FailedSettlement <FaildSttlm> [1..1] ± 848
Or   Cancelled <Canc> [1..1] ± 848
Or   Reversed <Rvsd> [1..1] ± 848
Or}   CancellationPending <CxlPdg> [1..1] ± 849
34.4.4.6.1  Status <Sts>
Presence: [1..1]
Definition: Status of the transfer is received, accepted, sent to next party, matched, already executed, or
settled.
Status <Sts> contains the following elements (see "TransferInstructionStatus5" on page 5205 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 5205
   Reason <Rsn> [0..1] Text 5205
34.4.4.6.2  PendingSettlement <PdgSttlm>
Presence: [1..1]
Definition: Status of the transfer is pending settlement.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 843 May 2026
```

