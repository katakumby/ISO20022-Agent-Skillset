---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.19 CashSettlementDetails <CshSttlmDtls>", "41.4.4.8.19.1 PaymentInstrument <PmtInstrm>", "41.4.4.8.19.1.1 CreditTransferDetails <CdtTrfDtls>", "41.4.4.8.19.1.1.8 IntermediaryAgent2 <IntrmyAgt2>", "41.4.4.8.19.1.1.8.1 Party <Pty>"]
file_pages: [1809]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.19.1.1.8.1 Party <Pty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1809 to 1809.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1809

```text
IntermediaryAgent2 <IntrmyAgt2> contains the following FinancialInstitutionIdentification17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  1809
{Or     NameAndAddress <NmAndAdr> [1..1] ± 1809
Or     BICFI <BICFI> [1..1] IdentifierSet C6 1809
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1810
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 1811
   LEI <LEI> [0..1] IdentifierSet 1811
41.4.4.8.19.1.1.8.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 1809
Or   BICFI <BICFI> [1..1] IdentifierSet C6 1809
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 1810
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 1811
41.4.4.8.19.1.1.8.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
41.4.4.8.19.1.1.8.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C6 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1809 May 2026
```

