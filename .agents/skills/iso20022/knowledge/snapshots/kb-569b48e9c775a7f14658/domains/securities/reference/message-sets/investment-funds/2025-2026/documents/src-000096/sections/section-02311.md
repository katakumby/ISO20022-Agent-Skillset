---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.10 BulkCashSettlementDetails <BlkCshSttlmDtls>", "50.4.4.10.1 PaymentInstrument <PmtInstrm>", "50.4.4.10.1.3 DirectDebitDetails <DrctDbtDtls>", "50.4.4.10.1.3.8 CreditorAgent <CdtrAgt>", "50.4.4.10.1.3.8.1 Party <Pty>", "50.4.4.10.1.3.8.1.1 NameAndAddress <NmAndAdr>"]
file_pages: [3228]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.10.1.3.8.1.1 NameAndAddress <NmAndAdr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3228 to 3228.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3228

```text
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 3228
Or   BICFI <BICFI> [1..1] IdentifierSet C6 3228
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 3228
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 3229
50.4.4.10.1.3.8.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
50.4.4.10.1.3.8.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C6 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
50.4.4.10.1.3.8.1.3  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [1..1]
Definition: Choice of identifier for a clearing system member, as assigned by the clearing system. In
some clearing systems, the accounts of the clearing system members are also assigned an identifier.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3228 May 2026
```

