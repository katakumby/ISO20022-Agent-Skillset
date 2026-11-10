---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.9.1 Transferor <Trfr>"]
file_pages: [673]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.9.1 Transferor <Trfr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 673 to 673.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 673

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party1 <Pty1> [0..1] ± 684
       Party2 <Pty2> [0..1] ± 684
       Party3 <Pty3> [0..1] ± 685
       Party4 <Pty4> [0..1] ± 685
       Party5 <Pty5> [0..1] ± 686
   PhysicalTransfer <PhysTrf> [0..1] CodeSet 686
   PhysicalTransferDetails <PhysTrfDtls> [0..1] ± C22 686
   ClientReference <ClntRef> [0..1] ± 687
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
28.4.9.1  Transferor <Trfr>
Presence: [0..1]
Definition: Party that delivers (transferor) securities to the receiving agent (transferee).
Transferor <Trfr> contains the following elements (see "PartyIdentification139" on page 5043 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
28.4.9.2  TransferorRegisteredAccount <TrfrRegdAcct>
Presence: [0..1]
Definition: Account from which the securities are to be delivered.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 673 May 2026
```

