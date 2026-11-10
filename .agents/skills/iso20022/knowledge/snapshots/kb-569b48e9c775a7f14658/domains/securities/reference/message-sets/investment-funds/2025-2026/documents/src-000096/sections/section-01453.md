---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.32 CashSettlementDetails <CshSttlmDtls>", "43.4.5.9.32.1 PaymentInstrument <PmtInstrm>", "43.4.5.9.32.1.2 ChequeDetails <ChqDtls>", "43.4.5.9.32.1.2.4 DrawerIdentification <DrwrId>"]
file_pages: [2031]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.32.1.2.4 DrawerIdentification <DrwrId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2031 to 2031.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2031

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
43.4.5.9.32.1.2.4  DrawerIdentification <DrwrId>
Presence: [0..1]
Definition: Account owner that issues the cheque ordering the drawee bank to pay a specific amount,
upon demand, to the payee.
DrawerIdentification <DrwrId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
43.4.5.9.32.1.3  BankersDraftDetails <BkrsDrftDtls>
Presence: [1..1]
Definition: Cheque drawn by a bank on itself or its agent. A person who owes money to another buys
the draft from a bank for cash and hands it to the creditor.
BankersDraftDetails <BkrsDrftDtls> contains the following Cheque10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [0..1] Text 2031
   PayeeIdentification <PyeeId> [1..1] ± 2031
   DraweeIdentification <DrweeId> [0..1]  2032
     Party <Pty> [1..1]  2032
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2032
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2033
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2033
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2034
     LEI <LEI> [0..1] IdentifierSet 2034
   DrawerIdentification <DrwrId> [0..1] ± 2035
43.4.5.9.32.1.3.1  Number <Nb>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the cheque as assigned by the financial institution.
Datatype: "Max35Text" on page 5403
43.4.5.9.32.1.3.2  PayeeIdentification <PyeeId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2031 May 2026
```

