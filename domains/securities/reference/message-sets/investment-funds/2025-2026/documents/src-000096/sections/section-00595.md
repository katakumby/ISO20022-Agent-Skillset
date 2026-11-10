---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.4 Message Building Blocks", "32.4.2.8 InvestmentAccountDetails <InvstmtAcctDtls>", "32.4.2.8.8 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [803]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.4.2.8.8 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 803 to 803.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 803

```text
32.4.2.8.8  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
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
32.4.2.9  IntermediaryInformation <IntrmyInf>
Presence: [0..*]
Definition: Identification of a related party or intermediary.
IntermediaryInformation <IntrmyInf> contains the following elements (see "Intermediary48" on
page 5005 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5005
   Account <Acct> [0..1]  5005
     AccountIdentification <AcctId> [0..1] Text 5006
     AccountDesignation <AcctDsgnt> [0..1] Text 5006
     AccountName <AcctNm> [0..1] Text 5006
     AccountServicer <AcctSvcr> [1..1] ± 5006
     RegistrationAddress <RegnAdr> [0..1] ± 5007
   Role <Role> [0..1]  5007
{Or     Code <Cd> [1..1] CodeSet 5007
Or}     Proprietary <Prtry> [1..1] ± 5009
   ContactPerson <CtctPrsn> [0..1] ± 5009
32.4.2.10  QueryInformation <QryInf>
Presence: [0..*]
Definition: Information about the query.
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 803 May 2026
```

