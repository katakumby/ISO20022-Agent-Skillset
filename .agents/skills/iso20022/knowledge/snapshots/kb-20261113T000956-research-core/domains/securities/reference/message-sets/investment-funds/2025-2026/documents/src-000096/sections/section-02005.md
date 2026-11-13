---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.6 InvestmentAccountDetails <InvstmtAcctDtls>", "49.4.5.9.6.7 SubAccountDetails <SubAcctDtls>"]
file_pages: [2827]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.6.7 SubAccountDetails <SubAcctDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2827 to 2827.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2827

```text
CodeName Name Definition
ELIG Eligible Eligible counterparty - MiFID
classification of counterparty. Eligible
customers are the most sophisticated
level of investor, able to opt out of some
the protections afforded by conduct of
business rules defined under MiFID.
RETL Retail Retail client - MiFID classification of
counterparty. Retail customers are the
least sophisticated level of investor.
PROF Professional Professional client - MiFID classification
of counterparty. Professional customers
are, for example, investment firms, credit
institutions, insurance companies.
49.4.5.9.6.7  SubAccountDetails <SubAcctDtls>
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
49.4.5.9.6.8  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
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
49.4.5.9.7  BeneficiaryDetails <BnfcryDtls>
Presence: [0..*]
Definition: Additional information about the investor.
Impacted by: C29 "PersonElementRule"
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2827 May 2026
```

