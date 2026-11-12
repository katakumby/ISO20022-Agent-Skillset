---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "41.4.4.12.1 PaymentInstrument <PmtInstrm>", "41.4.4.12.1.1 CreditTransferDetails <CdtTrfDtls>", "41.4.4.12.1.1.4 DebtorAgent <DbtrAgt>", "41.4.4.12.1.1.4.1 Party <Pty>", "41.4.4.12.1.1.4.1.1 NameAndAddress <NmAndAdr>"]
file_pages: [1855]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.12.1.1.4.1.1 NameAndAddress <NmAndAdr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1855 to 1855.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1855

```text
Party <Pty> contains one of the following FinancialInstitutionIdentification10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 1855
Or   BICFI <BICFI> [1..1] IdentifierSet C6 1855
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 1855
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 1856
41.4.4.12.1.1.4.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
41.4.4.12.1.1.4.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C6 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
41.4.4.12.1.1.4.1.3  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [1..1]
Definition: Choice of identifier for a clearing system member, as assigned by the clearing system. In
some clearing systems, the accounts of the clearing system members are also assigned an identifier.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1855 May 2026
```

