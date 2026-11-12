---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["65 reda.049.001.01 AccountLinkCreationRequestV01", "65.4 Message Building Blocks", "65.4.2 AccountLink <AcctLk>", "65.4.2.1 SecuritiesAccount <SctiesAcct>"]
file_pages: [2372]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.049.001.01"]
---

# 65.4.2.1 SecuritiesAccount <SctiesAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2372 to 2372.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2372

```text
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SecuritiesAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SecuritiesAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SecuritiesAccount Must be absent
• SecuritiesAccountOrBlockChainAddress3Rule
Either SecuritiesAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SecuritiesAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
65.4.2.1  SecuritiesAccount <SctiesAcct>
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
65.4.2.2  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
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
65.4.2.3  CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which a cash entry is made.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities 2372 August 2026
```

