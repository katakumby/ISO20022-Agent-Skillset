---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.10 PaymentDetails <PmtDtls>", "40.4.15.10.2 CreditTransferDetails <CdtTrfDtls>", "40.4.15.10.2.5 IntermediaryAgent1 <IntrmyAgt1>", "40.4.15.10.2.5.1 BICFI <BICFI>"]
file_pages: [1575]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.10.2.5.1 BICFI <BICFI>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1575 to 1575.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1575

```text
IntermediaryAgent1 <IntrmyAgt1> contains the following FinancialInstitutionIdentification16
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C9 1575
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1575
   NameAndAddress <NmAndAdr> [0..1] ± 1576
   LEI <LEI> [0..1] IdentifierSet 1576
   ProprietaryIdentification <PrtryId> [0..1] Text 1577
   BranchIdentification <BrnchId> [0..1] ± 1577
40.4.15.10.2.5.1  BICFI <BICFI>
Presence: [0..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C9 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
40.4.15.10.2.5.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Definition: Information used to identify a member within a clearing system.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1575 May 2026
```

