---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.26 PaymentDetails <PmtDtls>", "40.4.15.11.26.2 CreditTransferDetails <CdtTrfDtls>", "40.4.15.11.26.2.9 CreditorAgent <CdtrAgt>", "40.4.15.11.26.2.9.5 ProprietaryIdentification <PrtryId>"]
file_pages: [1667]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.26.2.9.5 ProprietaryIdentification <PrtryId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1667 to 1667.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1667

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
40.4.15.11.26.2.9.5  ProprietaryIdentification <PrtryId>
Presence: [0..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
Datatype: "Max35Text" on page 5403
40.4.15.11.26.2.9.6  BranchIdentification <BrnchId>
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
40.4.15.11.26.2.10  CreditorAgentAccount <CdtrAgtAcct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the creditor agent at its servicing agent to which
a credit entry was made as a result of the payment transaction.
CreditorAgentAccount <CdtrAgtAcct> contains the following AccountIdentificationAndName9
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1667
   IBAN <IBAN> [0..1] IdentifierSet C28 1667
   BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1668
   Other <Othr> [0..1] ± 1668
40.4.15.11.26.2.10.1  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
40.4.15.11.26.2.10.2  IBAN <IBAN>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1667 May 2026
```

