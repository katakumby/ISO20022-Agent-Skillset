---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["2 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 SecurityCSDLink <SctyCSDLk>", "2.4.2.5 IssuanceAccount <IssncAcct>", "2.4.2.5.1 IssuanceAccount <IssncAcct>"]
file_pages: [14]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 2.4.2.5.1 IssuanceAccount <IssncAcct>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 14 to 14.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 14

```text
Impacted by: C7 "IssuanceAccountOrBlockChainAddress1Rule", C8
"IssuanceAccountOrBlockChainAddress2Rule", C10 "SecuritiesAccountOrBlockChainAddress3Rule"
IssuanceAccount <IssncAcct> contains the following IssuanceAccount3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuanceAccount <IssncAcct> [0..1] ± 14
   IssuanceBlockChainAddressOrWallet
<IssncBlckChainAdrOrWllt>
[0..1] ± 14
   PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 15
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
2.4.2.5.1  IssuanceAccount <IssncAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
IssuanceAccount <IssncAcct> contains the following elements (see "SecuritiesAccount19" on
page 59 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 59
   Type <Tp> [0..1] ± 59
   Name <Nm> [0..1] Text 59
2.4.2.5.2  IssuanceBlockChainAddressOrWallet <IssncBlckChainAdrOrWllt>
Presence: [0..1]
Approved by the Securities SEG on 21 November 2024. reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities - Link Reference Data 14 December 2024
```

