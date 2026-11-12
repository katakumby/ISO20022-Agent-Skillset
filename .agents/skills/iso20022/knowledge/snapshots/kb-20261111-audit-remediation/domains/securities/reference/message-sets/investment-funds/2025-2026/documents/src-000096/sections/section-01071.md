---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>", "39.4.15.4 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "39.4.15.4.5 TransfereeAccount <TrfeeAcct>", "39.4.15.4.5.7 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [1478]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.15.4.5.7 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1478 to 1478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1478

```text
SubAccountDetails <SubAcctDtls> contains the following elements (see "SubAccount5" on
page 4329 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4329
   Name <Nm> [0..1] Text 4329
   Characteristic <Chrtc> [0..1] Text 4329
39.4.15.4.5.7  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
39.4.15.4.6  Transferor <Trfr>
Presence: [0..1]
Definition: Party and account from which the transferor delivers the financial instrument to the
transferee.
Transferor <Trfr> contains the following Account37 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OwnerIdentification <OwnrId> [0..1] ± 1478
   AccountIdentification <AcctId> [0..1] Text 1479
   Designation <Dsgnt> [0..1] Text 1479
   AccountName <AcctNm> [0..1] Text 1479
   Servicer <Svcr> [0..1] ± 1479
   SubAccountDetails <SubAcctDtls> [0..1] ± 1480
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1480
39.4.15.4.6.1  OwnerIdentification <OwnrId>
Presence: [0..1]
Definition: Party that legally owns the account.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1478 May 2026
```

