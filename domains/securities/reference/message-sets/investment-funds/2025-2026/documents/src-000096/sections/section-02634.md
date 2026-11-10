---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.18 CashSettlementDetails <CshSttlmDtls>", "53.4.5.18.1 CashInOrOut <CshInOrOut>", "53.4.5.18.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "53.4.5.18.1.1.2 CreditTransferDetails <CdtTrfDtls>", "53.4.5.18.1.1.2.5 DebtorAgentAccount <DbtrAgtAcct>"]
file_pages: [3712]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.18.1.1.2.5 DebtorAgentAccount <DbtrAgtAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3712 to 3712.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3712

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
53.4.5.18.1.1.2.5  DebtorAgentAccount <DbtrAgtAcct>
Presence: [0..1]
Definition: Identifies the account of the debtor's agent.
DebtorAgentAccount <DbtrAgtAcct> contains the following AccountIdentificationAndName8
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3712
{Or     IBAN <IBAN> [1..1] IdentifierSet C19 3712
Or     BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3713
Or}     Other <Othr> [1..1] ± 3713
   Name <Nm> [0..1] Text 3713
53.4.5.18.1.1.2.5.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following AccountIdentification82Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C19 3712
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3713
Or}   Other <Othr> [1..1] ± 3713
53.4.5.18.1.1.2.5.1.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C19 "IBAN"
Datatype: "IBAN2007Identifier" on page 5394
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3712 May 2026
```

