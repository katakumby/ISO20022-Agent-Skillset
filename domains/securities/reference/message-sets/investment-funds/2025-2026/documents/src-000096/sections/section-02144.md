---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>", "49.4.5.13.1 PaymentInstrument <PmtInstrm>", "49.4.5.13.1.4 ChequeDetails <ChqDtls>", "49.4.5.13.1.4.3 DraweeIdentification <DrweeId>", "49.4.5.13.1.4.3.1 Party <Pty>"]
file_pages: [2991]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.13.1.4.3.1 Party <Pty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2991 to 2991.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2991

```text
DraweeIdentification <DrweeId> contains the following FinancialInstitutionIdentification17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  2991
{Or     NameAndAddress <NmAndAdr> [1..1] ± 2991
Or     BICFI <BICFI> [1..1] IdentifierSet C7 2991
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2992
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 2993
   LEI <LEI> [0..1] IdentifierSet 2993
49.4.5.13.1.4.3.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 2991
Or   BICFI <BICFI> [1..1] IdentifierSet C7 2991
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2992
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 2993
49.4.5.13.1.4.3.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
49.4.5.13.1.4.3.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C7 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2991 May 2026
```

