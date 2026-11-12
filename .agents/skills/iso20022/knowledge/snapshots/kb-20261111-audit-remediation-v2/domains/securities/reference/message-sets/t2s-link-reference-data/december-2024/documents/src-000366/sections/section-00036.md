---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["5 reda.049.001.01 AccountLinkCreationRequestV01", "5.4 Message Building Blocks", "5.4.2 AccountLink <AcctLk>", "5.4.2.1 SecuritiesAccount <SctiesAcct>"]
file_pages: [38]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.049.001.01"]
---

# 5.4.2.1 SecuritiesAccount <SctiesAcct>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 38 to 38.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 38

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
5.4.2.1  SecuritiesAccount <SctiesAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SecuritiesAccount <SctiesAcct> contains the following elements (see "SecuritiesAccount19" on
page 59 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 59
   Type <Tp> [0..1] ± 59
   Name <Nm> [0..1] Text 59
5.4.2.2  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 65 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 65
   Type <Tp> [0..1] ± 65
   Name <Nm> [0..1] Text 65
5.4.2.3  CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which a cash entry is made.
Approved by the Securities SEG on 21 November 2024. reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities - Link Reference Data 38 December 2024
```

