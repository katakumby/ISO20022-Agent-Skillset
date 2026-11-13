---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.33 CashSettlementDetails <CshSttlmDtls>", "46.4.5.10.33.1 PaymentInstrument <PmtInstrm>", "46.4.5.10.33.1.2 ChequeDetails <ChqDtls>", "46.4.5.10.33.1.2.1 Number <Nb>"]
file_pages: [2448]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.33.1.2.1 Number <Nb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2448 to 2448.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2448

```text
ChequeDetails <ChqDtls> contains the following Cheque10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [0..1] Text 2448
   PayeeIdentification <PyeeId> [1..1] ± 2448
   DraweeIdentification <DrweeId> [0..1]  2448
     Party <Pty> [1..1]  2449
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2449
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2449
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2450
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2451
     LEI <LEI> [0..1] IdentifierSet 2451
   DrawerIdentification <DrwrId> [0..1] ± 2452
46.4.5.10.33.1.2.1  Number <Nb>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the cheque as assigned by the financial institution.
Datatype: "Max35Text" on page 5403
46.4.5.10.33.1.2.2  PayeeIdentification <PyeeId>
Presence: [1..1]
Definition: Party to which the cheque is made payable.
PayeeIdentification <PyeeId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
46.4.5.10.33.1.2.3  DraweeIdentification <DrweeId>
Presence: [0..1]
Definition: Financial institution on which the cheque is drawn, that is, the financial institution that
services the account of the entity that issued the cheque.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2448 May 2026
```

