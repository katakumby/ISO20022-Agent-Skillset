---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "33.4 Message Building Blocks", "33.4.4 StatusReport <StsRpt>", "33.4.4.3 ClientReference <ClntRef>"]
file_pages: [813]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.010.001.07"]
---

# 33.4.4.3 ClientReference <ClntRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 813 to 813.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 813

```text
33.4.4.3  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the transfer. This reference can typically
be used in a hub scenario to give the reference of the transfer as assigned by the underlying client.
ClientReference <ClntRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
33.4.4.4  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a transfer cancellation, as assigned by the instructing
party.
Datatype: "Max35Text" on page 5403
33.4.4.5  Status <Sts>
Presence: [1..1]
Definition: Status of the transfer cancellation.
Status <Sts> contains one of the following Status31Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Status <Sts> [1..1] ± 813
Or   Rejected <Rjctd> [1..1] ± 814
Or   Complete <Cmplt> [1..1] ± 814
Or}   Pending <Pdg> [1..1] ± 814
33.4.4.5.1  Status <Sts>
Presence: [1..1]
Definition: Status of the transfer cancellation is accepted or sent to next party.
Status <Sts> contains the following elements (see "TransferCancellationStatus3" on page 5187 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 5187
   Reason <Rsn> [0..1] Text 5187
Approved by the Securities SEG on 27 January 2026 sese.010.001.07
TransferCancellationStatusReportV07
Investment Funds - Maintenance 2025 - 2026 813 May 2026
```

