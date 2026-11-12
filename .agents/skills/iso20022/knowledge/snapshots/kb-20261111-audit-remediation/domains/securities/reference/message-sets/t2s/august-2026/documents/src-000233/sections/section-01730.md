---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["66 reda.050.001.01 AccountLinkMaintenanceRequestV01", "66.4 Message Building Blocks", "66.4.2 AccountLinkIdentification <AcctLkId>", "66.4.2.1 SecuritiesAccount <SctiesAcct>"]
file_pages: [2378]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.050.001.01"]
---

# 66.4.2.1 SecuritiesAccount <SctiesAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2378 to 2378.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2378

```text
66.4.2.1  SecuritiesAccount <SctiesAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SecuritiesAccount <SctiesAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
66.4.2.2  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 3016 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 3016
   Type <Tp> [0..1] ± 3016
   Name <Nm> [0..1] Text 3016
66.4.2.3  CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which a cash entry is made.
CashAccount <CshAcct> contains the following elements (see "CashAccount38" on page 2828 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 2828
   Type <Tp> [0..1] ± 2828
   Currency <Ccy> [0..1] CodeSet C1 2828
   Name <Nm> [0..1] Text 2829
   Proxy <Prxy> [0..1] ± 2829
66.4.2.4  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the securities account is linked to the cash account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities 2378 August 2026
```

