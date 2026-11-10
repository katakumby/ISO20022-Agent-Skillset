---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "47.4.4.12.1 PaymentInstrument <PmtInstrm>", "47.4.4.12.1.5 BankersDraftDetails <BkrsDrftDtls>", "47.4.4.12.1.5.3 DraweeIdentification <DrweeId>"]
file_pages: [2755]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.12.1.5.3 DraweeIdentification <DrweeId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2755 to 2755.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2755

```text
Definition: Party to which the cheque is made payable.
PayeeIdentification <PyeeId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
47.4.4.12.1.5.3  DraweeIdentification <DrweeId>
Presence: [0..1]
Definition: Financial institution on which the cheque is drawn, that is, the financial institution that
services the account of the entity that issued the cheque.
DraweeIdentification <DrweeId> contains the following FinancialInstitutionIdentification17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  2755
{Or     NameAndAddress <NmAndAdr> [1..1] ± 2755
Or     BICFI <BICFI> [1..1] IdentifierSet C6 2756
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2756
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 2757
   LEI <LEI> [0..1] IdentifierSet 2757
47.4.4.12.1.5.3.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 2755
Or   BICFI <BICFI> [1..1] IdentifierSet C6 2756
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2756
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 2757
47.4.4.12.1.5.3.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2755 May 2026
```

