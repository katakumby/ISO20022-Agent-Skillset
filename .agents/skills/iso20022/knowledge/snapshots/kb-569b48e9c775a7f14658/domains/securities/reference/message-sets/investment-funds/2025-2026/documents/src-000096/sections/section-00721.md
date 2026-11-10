---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.9 PaymentDetails <PmtDtls>", "35.4.14.9.2 CreditTransferDetails <CdtTrfDtls>", "35.4.14.9.2.3 DebtorAgent <DbtrAgt>", "35.4.14.9.2.3.1 BICFI <BICFI>"]
file_pages: [993]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.9.2.3.1 BICFI <BICFI>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 993 to 993.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 993

```text
DebtorAgent <DbtrAgt> contains the following FinancialInstitutionIdentification16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C10 993
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 993
   NameAndAddress <NmAndAdr> [0..1] ± 994
   LEI <LEI> [0..1] IdentifierSet 994
   ProprietaryIdentification <PrtryId> [0..1] Text 995
   BranchIdentification <BrnchId> [0..1] ± 995
35.4.14.9.2.3.1  BICFI <BICFI>
Presence: [0..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C10 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
35.4.14.9.2.3.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Definition: Information used to identify a member within a clearing system.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 993 May 2026
```

