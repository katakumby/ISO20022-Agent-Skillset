---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["2 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 SecurityCSDLink <SctyCSDLk>", "2.4.2.5 IssuanceAccount <IssncAcct>", "2.4.2.5.3 PrimaryAccountIndicator <PmryAcctInd>"]
file_pages: [15]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 2.4.2.5.3 PrimaryAccountIndicator <PmryAcctInd>

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 15 to 15.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 15

```text
Definition: issuance blockchain address or wallet where digital assets are maintained. This is the
equivalent of safekeeping account for digital assets.
IssuanceBlockChainAddressOrWallet <IssncBlckChainAdrOrWllt> contains the following elements
(see "BlockChainAddressWallet3" on page 65 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 65
   Type <Tp> [0..1] ± 65
   Name <Nm> [0..1] Text 65
2.4.2.5.3  PrimaryAccountIndicator <PmryAcctInd>
Presence: [1..1]
Definition: Defines if the related issuance account is the primary account or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 77):
• Meaning When True: Yes
• Meaning When False: No
2.4.2.6  DefaultLink <DfltLk>
Presence: [0..1]
Definition: Specifies whether the security CSD link is the default link.
Usage: when DefaultLink is absent, value is No/false
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 77):
• Meaning When True: True
• Meaning When False: False
2.4.2.7  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the CSD is linked to the security.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 60 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 61
Or}   DateTime <DtTm> [1..1] DateTime 61
2.4.2.8  ValidTo <VldTo>
Presence: [0..1]
Definition: Defines the date until when the CSD is linked to the security.
Approved by the Securities SEG on 21 November 2024. reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities - Link Reference Data 15 December 2024
```

