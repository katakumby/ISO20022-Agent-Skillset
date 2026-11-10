---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.8 AccountDetails <AcctDtls>", "30.4.9.18 PhysicalTransfer <PhysTrf>"]
file_pages: [775]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.9.18 PhysicalTransfer <PhysTrf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 775 to 775.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 775

```text
Party5 <Pty5> contains the following elements (see "PartyIdentificationAndAccount194" on page 5009
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5010
   LEI <LEI> [0..1] IdentifierSet 5010
   AlternateIdentification <AltrnId> [0..1] ± 5010
   SafekeepingAccount <SfkpgAcct> [0..1] ± 5010
   ProcessingDate <PrcgDt> [0..1] ± 5011
   ProcessingIdentification <PrcgId> [0..1] Text 5011
   AdditionalInformation <AddtlInf> [0..1] ± C4 5011
30.4.9.18  PhysicalTransfer <PhysTrf>
Presence: [0..1]
Definition: Indicates whether the financial instrument is to be physically delivered.
Datatype: "PhysicalTransferType1Code" on page 5341
CodeName Name Definition
DEMT Dematerialised Dematerialised transfer.
PHYS Physical Physical transfer.
30.4.9.19  PhysicalTransferDetails <PhysTrfDtls>
Presence: [0..1]
Definition: Parameters of a physical delivery.
Impacted by: C23 "NameAndAddress1Rule"
PhysicalTransferDetails <PhysTrfDtls> contains the following elements (see "DeliveryParameters4"
on page 5106 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RegisteredAddressIndicator <RegdAdrInd> [1..1] Indicator 5106
   NameAndAddress <NmAndAdr> [0..1] ± 5106
   ContactPerson <CtctPrsn> [0..1] ± 5106
Constraints
• NameAndAddress1Rule
If RegisteredAddressIndicator is "true" or "1" (Yes), then NameAndAddress is not allowed.
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 775 May 2026
```

