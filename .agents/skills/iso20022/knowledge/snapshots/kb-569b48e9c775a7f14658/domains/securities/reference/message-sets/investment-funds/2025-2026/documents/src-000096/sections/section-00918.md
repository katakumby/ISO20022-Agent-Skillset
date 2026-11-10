---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.21 IntermediaryInformation <IntrmyInf>"]
file_pages: [1261]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.21 IntermediaryInformation <IntrmyInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1261 to 1261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1261

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
36.4.15.11.21  IntermediaryInformation <IntrmyInf>
Presence: [0..*]
Definition: Identification of a related party or intermediary.
IntermediaryInformation <IntrmyInf> contains the following elements (see "Intermediary43" on
page 5040 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5040
   Account <Acct> [0..1]  5041
     Identification <Id> [0..1] Text 5041
     AccountServicer <AcctSvcr> [1..1] ± 5041
   Role <Role> [0..1] ± 5041
   ContactPerson <CtctPrsn> [0..1] ± 5041
36.4.15.11.22  RequestedTradeDate <ReqdTradDt>
Presence: [0..1]
Definition: Date to be used as the trade date when securities are settled through an International
Central Securities Depository (ICSD) or Central Securities Depository (CSD).
Datatype: "ISODate" on page 5388
36.4.15.11.23  RequestedSettlementDate <ReqdSttlmDt>
Presence: [0..1]
Definition: Date on which the securities are to be exchanged at the International Central Securities
Depository (ICSD) or Central Securities Depository (CSD).
Datatype: "ISODate" on page 5388
36.4.15.11.24  EffectiveTransferDate <FctvTrfDt>
Presence: [0..1]
Definition: Date and time at which the transfer was executed.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1261 May 2026
```

