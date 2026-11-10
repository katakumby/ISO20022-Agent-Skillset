---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.20 CashSettlementDetails <CshSttlmDtls>", "47.4.4.8.20.1 PaymentInstrument <PmtInstrm>", "47.4.4.8.20.1.5 BankersDraftDetails <BkrsDrftDtls>", "47.4.4.8.20.1.5.3 DraweeIdentification <DrweeId>"]
file_pages: [2685]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.20.1.5.3 DraweeIdentification <DrweeId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2685 to 2685.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2685

```text
Definition: Party to which the cheque is made payable.
PayeeIdentification <PyeeId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
47.4.4.8.20.1.5.3  DraweeIdentification <DrweeId>
Presence: [0..1]
Definition: Financial institution on which the cheque is drawn, that is, the financial institution that
services the account of the entity that issued the cheque.
DraweeIdentification <DrweeId> contains the following FinancialInstitutionIdentification17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  2685
{Or     NameAndAddress <NmAndAdr> [1..1] ± 2685
Or     BICFI <BICFI> [1..1] IdentifierSet C6 2686
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2686
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 2687
   LEI <LEI> [0..1] IdentifierSet 2687
47.4.4.8.20.1.5.3.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 2685
Or   BICFI <BICFI> [1..1] IdentifierSet C6 2686
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2686
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 2687
47.4.4.8.20.1.5.3.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2685 May 2026
```

