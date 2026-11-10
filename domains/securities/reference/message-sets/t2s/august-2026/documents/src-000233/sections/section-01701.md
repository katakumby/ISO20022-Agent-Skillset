---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["62 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "62.4 Message Building Blocks", "62.4.2 SecurityCSDLink <SctyCSDLk>", "62.4.2.5 IssuanceAccount <IssncAcct>", "62.4.2.5.3 PrimaryAccountIndicator <PmryAcctInd>"]
file_pages: [2349]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 62.4.2.5.3 PrimaryAccountIndicator <PmryAcctInd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2349 to 2349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2349

```text
Definition: issuance blockchain address or wallet where digital assets are maintained. This is the
equivalent of safekeeping account for digital assets.
IssuanceBlockChainAddressOrWallet <IssncBlckChainAdrOrWllt> contains the following elements
(see "BlockChainAddressWallet3" on page 3016 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 3016
   Type <Tp> [0..1] ± 3016
   Name <Nm> [0..1] Text 3016
62.4.2.5.3  PrimaryAccountIndicator <PmryAcctInd>
Presence: [1..1]
Definition: Defines if the related issuance account is the primary account or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
62.4.2.6  DefaultLink <DfltLk>
Presence: [0..1]
Definition: Specifies whether the security CSD link is the default link.
Usage: when DefaultLink is absent, value is No/false
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
62.4.2.7  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the CSD is linked to the security.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
62.4.2.8  ValidTo <VldTo>
Presence: [0..1]
Definition: Defines the date until when the CSD is linked to the security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities 2349 August 2026
```

