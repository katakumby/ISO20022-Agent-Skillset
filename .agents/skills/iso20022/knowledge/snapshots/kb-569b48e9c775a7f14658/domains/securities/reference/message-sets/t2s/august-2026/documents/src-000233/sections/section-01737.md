---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["67 reda.051.001.01 AccountLinkStatusAdviceV01", "67.4 Message Building Blocks", "67.4.3 AccountLinkIdentification <AcctLkId>", "67.4.3.1 SecuritiesAccount <SctiesAcct>"]
file_pages: [2386]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.051.001.01"]
---

# 67.4.3.1 SecuritiesAccount <SctiesAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2386 to 2386.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2386

```text
AccountLinkIdentification <AcctLkId> contains the following AccountLink8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccount <SctiesAcct> [0..1] ± 2386
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2386
   CashAccount <CshAcct> [1..1] ± 2387
   ValidFrom <VldFr> [1..1] ± 2387
Constraints
• SecuritiesAccountOrBlockChainAddress1Rule
If SecuritiesAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SecuritiesAccount is present
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
67.4.3.1  SecuritiesAccount <SctiesAcct>
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
67.4.3.2  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities 2386 August 2026
```

