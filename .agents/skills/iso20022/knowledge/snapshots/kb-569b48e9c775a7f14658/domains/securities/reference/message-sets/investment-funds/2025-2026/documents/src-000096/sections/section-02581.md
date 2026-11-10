---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>", "53.4.5.17.4 InvestmentAccountDetails <InvstmtAcctDtls>", "53.4.5.17.4.7 SubAccountDetails <SubAcctDtls>"]
file_pages: [3631]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.17.4.7 SubAccountDetails <SubAcctDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3631 to 3631.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3631

```text
CodeName Name Definition
RETL Retail Retail client - MiFID classification of
counterparty. Retail customers are the
least sophisticated level of investor.
PROF Professional Professional client - MiFID classification
of counterparty. Professional customers
are, for example, investment firms, credit
institutions, insurance companies.
53.4.5.17.4.7  SubAccountDetails <SubAcctDtls>
Presence: [0..1]
Definition: Sub-account of the master or omnibus account.
SubAccountDetails <SubAcctDtls> contains the following elements (see "SubAccount6" on
page 4642 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4642
   Name <Nm> [0..1] Text 4642
   Characteristic <Chrtc> [0..1] Text 4642
   AccountDesignation <AcctDsgnt> [0..1] Text 4642
53.4.5.17.4.8  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
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
53.4.5.17.5  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference1Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
DRIP DividendReinvestment Reinvestment of proceeds into
securities.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3631 May 2026
```

