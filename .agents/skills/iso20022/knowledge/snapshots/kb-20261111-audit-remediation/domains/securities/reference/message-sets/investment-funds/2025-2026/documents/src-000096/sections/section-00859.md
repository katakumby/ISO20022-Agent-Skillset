---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.10 PaymentDetails <PmtDtls>", "36.4.15.10.2 CreditTransferDetails <CdtTrfDtls>", "36.4.15.10.2.3 DebtorAgent <DbtrAgt>", "36.4.15.10.2.3.5 ProprietaryIdentification <PrtryId>"]
file_pages: [1190]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.10.2.3.5 ProprietaryIdentification <PrtryId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1190 to 1190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1190

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
36.4.15.10.2.3.5  ProprietaryIdentification <PrtryId>
Presence: [0..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
Datatype: "Max35Text" on page 5403
36.4.15.10.2.3.6  BranchIdentification <BrnchId>
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
36.4.15.10.2.4  DebtorAgentAccount <DbtrAgtAcct>
Presence: [0..1]
Definition: Identifies the account of the debtor's agent.
DebtorAgentAccount <DbtrAgtAcct> contains the following AccountIdentificationAndName9
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1190
   IBAN <IBAN> [0..1] IdentifierSet C28 1190
   BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1191
   Other <Othr> [0..1] ± 1191
36.4.15.10.2.4.1  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
36.4.15.10.2.4.2  IBAN <IBAN>
Presence: [0..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of the customer. Further specifications of the format and
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1190 May 2026
```

