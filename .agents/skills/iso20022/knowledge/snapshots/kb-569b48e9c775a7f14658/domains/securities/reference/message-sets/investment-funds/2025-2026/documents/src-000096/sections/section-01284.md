---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.19 CashSettlementDetails <CshSttlmDtls>", "41.4.4.8.19.1 PaymentInstrument <PmtInstrm>", "41.4.4.8.19.1.1 CreditTransferDetails <CdtTrfDtls>", "41.4.4.8.19.1.1.5 DebtorAgentAccount <DbtrAgtAcct>"]
file_pages: [1802]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.19.1.1.5 DebtorAgentAccount <DbtrAgtAcct>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1802 to 1802.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1802

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
41.4.4.8.19.1.1.5  DebtorAgentAccount <DbtrAgtAcct>
Presence: [0..1]
Definition: Identifies the account of the debtor's agent.
DebtorAgentAccount <DbtrAgtAcct> contains the following AccountIdentificationAndName8
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1802
{Or     IBAN <IBAN> [1..1] IdentifierSet C20 1802
Or     BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1803
Or}     Other <Othr> [1..1] ± 1803
   Name <Nm> [0..1] Text 1803
41.4.4.8.19.1.1.5.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following AccountIdentification82Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C20 1802
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1803
Or}   Other <Othr> [1..1] ± 1803
41.4.4.8.19.1.1.5.1.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C20 "IBAN"
Datatype: "IBAN2007Identifier" on page 5394
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1802 May 2026
```

