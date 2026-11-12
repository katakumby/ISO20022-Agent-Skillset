---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.20 CashSettlementDetails <CshSttlmDtls>", "47.4.4.8.20.1 PaymentInstrument <PmtInstrm>", "47.4.4.8.20.1.2 CreditTransferDetails <CdtTrfDtls>", "47.4.4.8.20.1.2.6 IntermediaryAgent1 <IntrmyAgt1>", "47.4.4.8.20.1.2.6.1 Party <Pty>"]
file_pages: [2653]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.20.1.2.6.1 Party <Pty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2653 to 2653.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2653

```text
IntermediaryAgent1 <IntrmyAgt1> contains the following FinancialInstitutionIdentification17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  2653
{Or     NameAndAddress <NmAndAdr> [1..1] ± 2653
Or     BICFI <BICFI> [1..1] IdentifierSet C6 2653
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2654
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 2655
   LEI <LEI> [0..1] IdentifierSet 2655
47.4.4.8.20.1.2.6.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 2653
Or   BICFI <BICFI> [1..1] IdentifierSet C6 2653
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2654
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 2655
47.4.4.8.20.1.2.6.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
47.4.4.8.20.1.2.6.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C6 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2653 May 2026
```

