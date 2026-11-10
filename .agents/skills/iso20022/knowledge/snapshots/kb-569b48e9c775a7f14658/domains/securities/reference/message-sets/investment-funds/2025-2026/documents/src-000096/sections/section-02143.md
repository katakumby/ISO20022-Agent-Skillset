---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>", "49.4.5.13.1 PaymentInstrument <PmtInstrm>", "49.4.5.13.1.4 ChequeDetails <ChqDtls>", "49.4.5.13.1.4.1 Number <Nb>"]
file_pages: [2990]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.13.1.4.1 Number <Nb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2990 to 2990.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2990

```text
ChequeDetails <ChqDtls> contains the following Cheque10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [0..1] Text 2990
   PayeeIdentification <PyeeId> [1..1] ± 2990
   DraweeIdentification <DrweeId> [0..1]  2990
     Party <Pty> [1..1]  2991
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2991
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2991
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2992
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2993
     LEI <LEI> [0..1] IdentifierSet 2993
   DrawerIdentification <DrwrId> [0..1] ± 2994
49.4.5.13.1.4.1  Number <Nb>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the cheque as assigned by the financial institution.
Datatype: "Max35Text" on page 5403
49.4.5.13.1.4.2  PayeeIdentification <PyeeId>
Presence: [1..1]
Definition: Party to which the cheque is made payable.
PayeeIdentification <PyeeId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
49.4.5.13.1.4.3  DraweeIdentification <DrweeId>
Presence: [0..1]
Definition: Financial institution on which the cheque is drawn, that is, the financial institution that
services the account of the entity that issued the cheque.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2990 May 2026
```

