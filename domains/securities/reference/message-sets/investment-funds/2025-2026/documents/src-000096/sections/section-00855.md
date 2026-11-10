---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.10 PaymentDetails <PmtDtls>", "36.4.15.10.2 CreditTransferDetails <CdtTrfDtls>", "36.4.15.10.2.1 Debtor <Dbtr>"]
file_pages: [1186]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.10.2.1 Debtor <Dbtr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1186 to 1186.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1186

```text
36.4.15.10.2.1  Debtor <Dbtr>
Presence: [0..1]
Definition: Party that owed an amount of money to the (ultimate) creditor. In the context of the payment
model, the debtor is also the debit account owner.
Debtor <Dbtr> contains the following elements (see "PartyIdentification132" on page 5029 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
36.4.15.10.2.2  DebtorAccount <DbtrAcct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the debtor to which a debit entry was made as a
result of the transaction.
DebtorAccount <DbtrAcct> contains the following AccountIdentificationAndName9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1186
   IBAN <IBAN> [0..1] IdentifierSet C28 1186
   BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1187
   Other <Othr> [0..1] ± 1187
36.4.15.10.2.2.1  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
36.4.15.10.2.2.2  IBAN <IBAN>
Presence: [0..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of the customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C28 "IBAN"
Datatype: "IBAN2007Identifier" on page 5394
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1186 May 2026
```

