---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.8.1 Transferee <Trfee>"]
file_pages: [585]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.8.1 Transferee <Trfee>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 585 to 585.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 585

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Depository <Dpstry> [0..1] ± 596
       Party1 <Pty1> [0..1] ± 597
       Party2 <Pty2> [0..1] ± 597
       Party3 <Pty3> [0..1] ± 597
       Party4 <Pty4> [0..1] ± 598
       Party5 <Pty5> [0..1] ± 598
   PhysicalTransfer <PhysTrf> [0..1] CodeSet 599
   PhysicalTransferDetails <PhysTrfDtls> [0..1] ± C23 599
   ClientReference <ClntRef> [0..1] ± 600
Constraints
• PhysicalTransferDetails1Rule
If PhysicalTransfer is PHYS (Physical), then PhysicalTransferDetails must be present.
On Condition
    /PhysicalTransfer is equal to value 'Physical'
Following Must be True
    /PhysicalTransferDetails Must be present
• PhysicalTransferDetails2Rule
If PhysicalTransfer is DEMT (Dematerialised), then PhysicalTransferDetails is not allowed.
On Condition
    /PhysicalTransfer is equal to value 'Dematerialised'
Following Must be True
    /PhysicalTransferDetails Must be absent
26.4.8.1  Transferee <Trfee>
Presence: [0..1]
Definition: Party that receives (transferee) securities from the delivering agent (transferor).
Transferee <Trfee> contains the following elements (see "PartyIdentification139" on page 5043 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
26.4.8.2  TransfereeRegisteredAccount <TrfeeRegdAcct>
Presence: [0..1]
Definition: Account into which the securities are to be received.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 585 May 2026
```

