---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.9 PaymentDetails <PmtDtls>", "35.4.14.9.2 CreditTransferDetails <CdtTrfDtls>", "35.4.14.9.2.5 IntermediaryAgent1 <IntrmyAgt1>", "35.4.14.9.2.5.5 ProprietaryIdentification <PrtryId>"]
file_pages: [999]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.9.2.5.5 ProprietaryIdentification <PrtryId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 999 to 999.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 999

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
35.4.14.9.2.5.5  ProprietaryIdentification <PrtryId>
Presence: [0..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
Datatype: "Max35Text" on page 5403
35.4.14.9.2.5.6  BranchIdentification <BrnchId>
Presence: [0..1]
Definition: Identification of a specific branch of the financial institution.
BranchIdentification <BrnchId> contains the following elements (see "BranchData2" on page 4483
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4483
   Name <Nm> [0..1] Text 4483
   PostalAddress <PstlAdr> [0..1] ± 4483
35.4.14.9.2.6  IntermediaryAgent1Account <IntrmyAgt1Acct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the intermediary agent 1 at its servicing agent in
the payment chain.
IntermediaryAgent1Account <IntrmyAgt1Acct> contains the following
AccountIdentificationAndName9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 999
   IBAN <IBAN> [0..1] IdentifierSet C26 999
   BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1000
   Other <Othr> [0..1] ± 1000
35.4.14.9.2.6.1  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
35.4.14.9.2.6.2  IBAN <IBAN>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 999 May 2026
```

