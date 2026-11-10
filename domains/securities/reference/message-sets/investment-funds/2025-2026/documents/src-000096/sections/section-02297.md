---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.10 BulkCashSettlementDetails <BlkCshSttlmDtls>", "50.4.4.10.1 PaymentInstrument <PmtInstrm>", "50.4.4.10.1.2 CreditTransferDetails <CdtTrfDtls>", "50.4.4.10.1.2.10 CreditorAgent <CdtrAgt>", "50.4.4.10.1.2.10.1 Party <Pty>"]
file_pages: [3214]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.10.1.2.10.1 Party <Pty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3214 to 3214.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3214

```text
CreditorAgent <CdtrAgt> contains the following FinancialInstitutionIdentification17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  3214
{Or     NameAndAddress <NmAndAdr> [1..1] ± 3214
Or     BICFI <BICFI> [1..1] IdentifierSet C6 3214
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3215
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 3216
   LEI <LEI> [0..1] IdentifierSet 3216
50.4.4.10.1.2.10.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 3214
Or   BICFI <BICFI> [1..1] IdentifierSet C6 3214
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 3215
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 3216
50.4.4.10.1.2.10.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
50.4.4.10.1.2.10.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C6 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3214 May 2026
```

