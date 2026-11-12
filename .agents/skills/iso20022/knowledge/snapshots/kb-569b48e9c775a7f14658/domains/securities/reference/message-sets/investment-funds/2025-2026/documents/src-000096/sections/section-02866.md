---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>", "55.4.5.21.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "55.4.5.21.1.1.2 CreditTransferDetails <CdtTrfDtls>", "55.4.5.21.1.1.2.8 IntermediaryAgent2 <IntrmyAgt2>", "55.4.5.21.1.1.2.8.1 Party <Pty>"]
file_pages: [4032]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1.1.2.8.1 Party <Pty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4032 to 4032.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4032

```text
IntermediaryAgent2 <IntrmyAgt2> contains the following FinancialInstitutionIdentification17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  4032
{Or     NameAndAddress <NmAndAdr> [1..1] ± 4032
Or     BICFI <BICFI> [1..1] IdentifierSet C6 4032
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4033
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 4034
   LEI <LEI> [0..1] IdentifierSet 4034
55.4.5.21.1.1.2.8.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 4032
Or   BICFI <BICFI> [1..1] IdentifierSet C6 4032
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4033
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 4034
55.4.5.21.1.1.2.8.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
55.4.5.21.1.1.2.8.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C6 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4032 May 2026
```

