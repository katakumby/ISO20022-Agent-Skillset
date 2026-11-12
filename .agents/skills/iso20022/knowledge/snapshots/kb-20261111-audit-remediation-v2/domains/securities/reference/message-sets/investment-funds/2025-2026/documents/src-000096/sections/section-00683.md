---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.19 PaymentDetails <PmtDtls>", "34.4.4.19.4 CashSettlementDetails <CshSttlmDtls>", "34.4.4.19.4.2 ChequeDetails <ChqDtls>", "34.4.4.19.4.2.3 DraweeIdentification <DrweeId>", "34.4.4.19.4.2.3.1 Party <Pty>"]
file_pages: [924]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.19.4.2.3.1 Party <Pty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 924 to 924.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 924

```text
DraweeIdentification <DrweeId> contains the following FinancialInstitutionIdentification17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  924
{Or     NameAndAddress <NmAndAdr> [1..1] ± 924
Or     BICFI <BICFI> [1..1] IdentifierSet C6 924
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 925
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 926
   LEI <LEI> [0..1] IdentifierSet 926
34.4.4.19.4.2.3.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 924
Or   BICFI <BICFI> [1..1] IdentifierSet C6 924
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 925
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 926
34.4.4.19.4.2.3.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
34.4.4.19.4.2.3.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C6 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 924 May 2026
```

