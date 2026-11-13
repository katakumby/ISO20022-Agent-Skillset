---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "52.4.5.12.1 PaymentInstrument <PmtInstrm>", "52.4.5.12.1.5 BankersDraftDetails <BkrsDrftDtls>", "52.4.5.12.1.5.3 DraweeIdentification <DrweeId>"]
file_pages: [3481]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.12.1.5.3 DraweeIdentification <DrweeId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3481 to 3481.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3481

```text
Definition: Party to which the cheque is made payable.
PayeeIdentification <PyeeId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
52.4.5.12.1.5.3  DraweeIdentification <DrweeId>
Presence: [0..1]
Definition: Financial institution on which the cheque is drawn, that is, the financial institution that
services the account of the entity that issued the cheque.
DraweeIdentification <DrweeId> contains the following FinancialInstitutionIdentification17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  3481
{Or     NameAndAddress <NmAndAdr> [1..1] ± 3481
Or     BICFI <BICFI> [1..1] IdentifierSet C7 3482
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3482
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 3483
   LEI <LEI> [0..1] IdentifierSet 3483
52.4.5.12.1.5.3.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 3481
Or   BICFI <BICFI> [1..1] IdentifierSet C7 3482
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 3482
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 3483
52.4.5.12.1.5.3.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3481 May 2026
```

