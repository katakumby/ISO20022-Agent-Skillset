---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.19 CashSettlementDetails <CshSttlmDtls>", "41.4.4.8.19.1 PaymentInstrument <PmtInstrm>", "41.4.4.8.19.1.3 BankersDraftDetails <BkrsDrftDtls>", "41.4.4.8.19.1.3.3 DraweeIdentification <DrweeId>"]
file_pages: [1826]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.19.1.3.3 DraweeIdentification <DrweeId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1826 to 1826.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1826

```text
Definition: Party to which the cheque is made payable.
PayeeIdentification <PyeeId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
41.4.4.8.19.1.3.3  DraweeIdentification <DrweeId>
Presence: [0..1]
Definition: Financial institution on which the cheque is drawn, that is, the financial institution that
services the account of the entity that issued the cheque.
DraweeIdentification <DrweeId> contains the following FinancialInstitutionIdentification17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  1826
{Or     NameAndAddress <NmAndAdr> [1..1] ± 1826
Or     BICFI <BICFI> [1..1] IdentifierSet C6 1827
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1827
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 1828
   LEI <LEI> [0..1] IdentifierSet 1828
41.4.4.8.19.1.3.3.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 1826
Or   BICFI <BICFI> [1..1] IdentifierSet C6 1827
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 1827
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 1828
41.4.4.8.19.1.3.3.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1826 May 2026
```

