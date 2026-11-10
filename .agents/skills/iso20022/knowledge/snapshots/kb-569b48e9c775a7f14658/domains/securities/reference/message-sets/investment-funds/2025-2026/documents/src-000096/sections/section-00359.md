---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.7 AccountDetails <AcctDtls>", "24.4.8.1 Transferee <Trfee>"]
file_pages: [497]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.8.1 Transferee <Trfee>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 497 to 497.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 497

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party1 <Pty1> [0..1] ± 508
       Party2 <Pty2> [0..1] ± 508
       Party3 <Pty3> [0..1] ± 509
       Party4 <Pty4> [0..1] ± 509
       Party5 <Pty5> [0..1] ± 510
   PhysicalTransfer <PhysTrf> [0..1] CodeSet 510
   PhysicalTransferDetails <PhysTrfDtls> [0..1] ± C22 510
   ClientReference <ClntRef> [0..1] ± 511
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
24.4.8.1  Transferee <Trfee>
Presence: [0..1]
Definition: Party that receives (transferee) securities from the delivering agent (transferor).
Transferee <Trfee> contains the following elements (see "PartyIdentification139" on page 5043 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
24.4.8.2  TransfereeRegisteredAccount <TrfeeRegdAcct>
Presence: [0..1]
Definition: Account into which the securities are to be received.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 497 May 2026
```

