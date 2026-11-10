---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.18 CashSettlementDetails <CshSttlmDtls>", "53.4.5.18.1 CashInOrOut <CshInOrOut>", "53.4.5.18.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "53.4.5.18.1.1.4 ChequeDetails <ChqDtls>", "53.4.5.18.1.1.4.1 Number <Nb>"]
file_pages: [3741]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.18.1.1.4.1 Number <Nb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3741 to 3741.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3741

```text
ChequeDetails <ChqDtls> contains the following Cheque10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [0..1] Text 3741
   PayeeIdentification <PyeeId> [1..1] ± 3741
   DraweeIdentification <DrweeId> [0..1]  3741
     Party <Pty> [1..1]  3742
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3742
Or       BICFI <BICFI> [1..1] IdentifierSet C5 3742
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3743
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3744
     LEI <LEI> [0..1] IdentifierSet 3744
   DrawerIdentification <DrwrId> [0..1] ± 3745
53.4.5.18.1.1.4.1  Number <Nb>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the cheque as assigned by the financial institution.
Datatype: "Max35Text" on page 5403
53.4.5.18.1.1.4.2  PayeeIdentification <PyeeId>
Presence: [1..1]
Definition: Party to which the cheque is made payable.
PayeeIdentification <PyeeId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
53.4.5.18.1.1.4.3  DraweeIdentification <DrweeId>
Presence: [0..1]
Definition: Financial institution on which the cheque is drawn, that is, the financial institution that
services the account of the entity that issued the cheque.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3741 May 2026
```

