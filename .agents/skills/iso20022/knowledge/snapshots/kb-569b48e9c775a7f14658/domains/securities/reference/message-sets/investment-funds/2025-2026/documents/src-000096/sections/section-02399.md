---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.35 CashSettlementDetails <CshSttlmDtls>", "52.4.5.10.35.1 PaymentInstrument <PmtInstrm>", "52.4.5.10.35.1.2 CreditTransferDetails <CdtTrfDtls>", "52.4.5.10.35.1.2.4 DebtorAgent <DbtrAgt>", "52.4.5.10.35.1.2.4.1 Party <Pty>", "52.4.5.10.35.1.2.4.1.1 NameAndAddress <NmAndAdr>"]
file_pages: [3375]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.35.1.2.4.1.1 NameAndAddress <NmAndAdr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3375 to 3375.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3375

```text
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 3375
Or   BICFI <BICFI> [1..1] IdentifierSet C7 3375
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 3375
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 3376
52.4.5.10.35.1.2.4.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
52.4.5.10.35.1.2.4.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C7 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
52.4.5.10.35.1.2.4.1.3  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [1..1]
Definition: Choice of identifier for a clearing system member, as assigned by the clearing system. In
some clearing systems, the accounts of the clearing system members are also assigned an identifier.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3375 May 2026
```

