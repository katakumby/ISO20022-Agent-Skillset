---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.33 CashSettlementDetails <CshSttlmDtls>", "46.4.5.10.33.1 PaymentInstrument <PmtInstrm>", "46.4.5.10.33.1.2 ChequeDetails <ChqDtls>", "46.4.5.10.33.1.2.3 DraweeIdentification <DrweeId>", "46.4.5.10.33.1.2.3.1 Party <Pty>"]
file_pages: [2449]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.33.1.2.3.1 Party <Pty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2449 to 2449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2449

```text
DraweeIdentification <DrweeId> contains the following FinancialInstitutionIdentification17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  2449
{Or     NameAndAddress <NmAndAdr> [1..1] ± 2449
Or     BICFI <BICFI> [1..1] IdentifierSet C7 2449
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2450
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 2451
   LEI <LEI> [0..1] IdentifierSet 2451
46.4.5.10.33.1.2.3.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 2449
Or   BICFI <BICFI> [1..1] IdentifierSet C7 2449
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2450
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 2451
46.4.5.10.33.1.2.3.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
46.4.5.10.33.1.2.3.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C7 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2449 May 2026
```

