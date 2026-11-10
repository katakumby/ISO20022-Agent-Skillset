---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.19 PaymentDetails <PmtDtls>", "34.4.4.19.4 CashSettlementDetails <CshSttlmDtls>", "34.4.4.19.4.2 ChequeDetails <ChqDtls>", "34.4.4.19.4.2.1 Number <Nb>"]
file_pages: [923]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.19.4.2.1 Number <Nb>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 923 to 923.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 923

```text
ChequeDetails <ChqDtls> contains the following Cheque12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [0..1] Text 923
   PayeeIdentification <PyeeId> [0..1] ± 923
   DraweeIdentification <DrweeId> [0..1]  923
     Party <Pty> [1..1]  924
{Or       NameAndAddress <NmAndAdr> [1..1] ± 924
Or       BICFI <BICFI> [1..1] IdentifierSet C6 924
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 925
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 926
     LEI <LEI> [0..1] IdentifierSet 926
   DrawerIdentification <DrwrId> [0..1] ± 927
34.4.4.19.4.2.1  Number <Nb>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the cheque as assigned by the financial institution.
Datatype: "Max35Text" on page 5403
34.4.4.19.4.2.2  PayeeIdentification <PyeeId>
Presence: [0..1]
Definition: Party to which the cheque is made payable.
PayeeIdentification <PyeeId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
34.4.4.19.4.2.3  DraweeIdentification <DrweeId>
Presence: [0..1]
Definition: Financial institution on which the cheque is drawn, that is, the financial institution that
services the account of the entity that issued the cheque.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 923 May 2026
```

