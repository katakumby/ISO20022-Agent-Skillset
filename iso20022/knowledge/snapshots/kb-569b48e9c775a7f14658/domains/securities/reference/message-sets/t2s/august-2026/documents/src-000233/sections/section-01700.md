---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["62 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "62.4 Message Building Blocks", "62.4.2 SecurityCSDLink <SctyCSDLk>", "62.4.2.5 IssuanceAccount <IssncAcct>", "62.4.2.5.1 IssuanceAccount <IssncAcct>"]
file_pages: [2348]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 62.4.2.5.1 IssuanceAccount <IssncAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2348 to 2348.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2348

```text
Impacted by: C7 "IssuanceAccountOrBlockChainAddress1Rule", C8
"IssuanceAccountOrBlockChainAddress2Rule", C10 "SecuritiesAccountOrBlockChainAddress3Rule"
IssuanceAccount <IssncAcct> contains the following IssuanceAccount3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuanceAccount <IssncAcct> [0..1] ± 2348
   IssuanceBlockChainAddressOrWallet
<IssncBlckChainAdrOrWllt>
[0..1] ± 2348
   PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 2349
Constraints
• IssuanceAccountOrBlockChainAddress1Rule
If IssuanceAccount is present, IssuanceBlockChainAddressOrWallet must be absent.
On Condition
    /IssuanceAccount is present
Following Must be True
    /IssuanceBlockChainAddressOrWallet Must be absent
• IssuanceAccountOrBlockChainAddress2Rule
If IssuanceBlockChainAddressOrWallet is present, IssuanceAccount must be absent.
On Condition
    /IssuanceBlockChainAddressOrWallet is present
Following Must be True
    /IssuanceAccount Must be absent
• SecuritiesAccountOrBlockChainAddress3Rule
Either IssuanceAccount or IssuanceBlockChainAddressOrWallet must be present but not both.
Following Must be True
    /IssuanceAccount Must be present
 Or    /IssuanceBlockChainAddressOrWallet Must be present
62.4.2.5.1  IssuanceAccount <IssncAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
IssuanceAccount <IssncAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
62.4.2.5.2  IssuanceBlockChainAddressOrWallet <IssncBlckChainAdrOrWllt>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities 2348 August 2026
```

