---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.10 PaymentDetails <PmtDtls>", "36.4.15.10.2 CreditTransferDetails <CdtTrfDtls>", "36.4.15.10.2.9 CreditorAgent <CdtrAgt>", "36.4.15.10.2.9.1 BICFI <BICFI>"]
file_pages: [1200]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.10.2.9.1 BICFI <BICFI>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1200 to 1200.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1200

```text
CreditorAgent <CdtrAgt> contains the following FinancialInstitutionIdentification16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C9 1200
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1200
   NameAndAddress <NmAndAdr> [0..1] ± 1201
   LEI <LEI> [0..1] IdentifierSet 1201
   ProprietaryIdentification <PrtryId> [0..1] Text 1202
   BranchIdentification <BrnchId> [0..1] ± 1202
36.4.15.10.2.9.1  BICFI <BICFI>
Presence: [0..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C9 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
36.4.15.10.2.9.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Definition: Information used to identify a member within a clearing system.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1200 May 2026
```

