---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "33.4 Message Building Blocks", "33.4.4 StatusReport <StsRpt>", "33.4.4.5 Status <Sts>", "33.4.4.5.2 Rejected <Rjctd>"]
file_pages: [814]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.010.001.07"]
---

# 33.4.4.5.2 Rejected <Rjctd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 814 to 814.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 814

```text
33.4.4.5.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Status of the transfer cancellation is rejected.
Rejected <Rjctd> contains the following elements (see "RejectionReason33" on page 5266 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5267
{Or     Code <Cd> [1..1] CodeSet 5267
Or}     Proprietary <Prtry> [1..1] ± 5267
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 5267
33.4.4.5.3  Complete <Cmplt>
Presence: [1..1]
Definition: Status of the transfer cancellation is complete. The cancellation instruction has been
accepted and processed, the cancellation is complete.
Complete <Cmplt> contains the following elements (see "CancelledCompleteReason1" on page 5259
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5259
{Or     Code <Cd> [1..1] CodeSet 5259
Or}     Proprietary <Prtry> [1..1] ± 5259
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 5260
33.4.4.5.4  Pending <Pdg>
Presence: [1..1]
Definition: Status of the transfer cancellation is pending.
Pending <Pdg> contains the following elements (see "TransferCancellationPendingStatus1" on
page 5264 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] Text 5264
33.4.4.6  StatusInitiator <StsInitr>
Presence: [0..1]
Definition: Party that initiates the status.
Approved by the Securities SEG on 27 January 2026 sese.010.001.07
TransferCancellationStatusReportV07
Investment Funds - Maintenance 2025 - 2026 814 May 2026
```

