---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.10 PaymentDetails <PmtDtls>", "40.4.15.10.2 CreditTransferDetails <CdtTrfDtls>", "40.4.15.10.2.12 CreditorAccount <CdtrAcct>"]
file_pages: [1587]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.10.2.12 CreditorAccount <CdtrAcct>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1587 to 1587.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1587

```text
Creditor <Cdtr> contains the following elements (see "PartyIdentification132" on page 5029 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
40.4.15.10.2.12  CreditorAccount <CdtrAcct>
Presence: [1..1]
Definition: Unambiguous identification of the account of the creditor to which a credit entry was posted
as a result of the payment transaction.
CreditorAccount <CdtrAcct> contains the following AccountIdentificationAndName9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1587
   IBAN <IBAN> [0..1] IdentifierSet C28 1587
   BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1588
   Other <Othr> [0..1] ± 1588
40.4.15.10.2.12.1  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
40.4.15.10.2.12.2  IBAN <IBAN>
Presence: [0..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of the customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C28 "IBAN"
Datatype: "IBAN2007Identifier" on page 5394
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1587 May 2026
```

